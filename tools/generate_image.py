#!/usr/bin/env python3
"""
Image generation via native Gemini SDK (default) or OpenRouter proxy.

Single image:
    python tools/generate_image.py "prompt" --model flash --aspect 16:9 --name my-image

Comic (two frames, sequential session):
    python tools/generate_image.py --comic ch01-bold-claim \\
        --setting "Modern office, whiteboard, warm lighting" \\
        --characters maven skeptic \\
        --frame-a "Maven at whiteboard mid-explanation; Skeptic arms crossed but leaning in" \\
        --frame-b "Skeptic leans forward, pointing; Maven nods, amused" \\
        --ref assets/characters/maven-ref-sheet.png \\
        --ref assets/characters/skeptic-ref-sheet.png \\
        --model pro

Edit existing image:
    python tools/generate_image.py --edit assets/generated/some-image.png "Add a hat"

Backends:
    gemini      = Native Gemini SDK (default) — multi-turn chat, native aspect ratio, labeled refs
    openrouter  = OpenRouter proxy (legacy) — for non-Gemini models or fallback

Models:
    flash  = Nano Banana (Gemini 2.5 Flash Image)  ~$0.039/image
    pro    = Nano Banana Pro (Gemini 3 Pro Image)  ~$0.134/image

Single images → assets/generated/<name>-<timestamp>.png
Comic frames  → assets/generated/<id>-frame-a-<timestamp>.png
                assets/generated/<id>-frame-b-<timestamp>.png
Edited images → assets/generated/<name>-edit-<timestamp>.png
Costs logged  → assets/generated/image-log.csv
"""

from __future__ import annotations

import argparse
import base64
import csv
import io
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from PIL import Image

# Gemini SDK — imported lazily to avoid hard failure if not installed
_genai = None
_genai_types = None
_genai_errors = None


def _ensure_genai():
    """Lazy-import the google-genai SDK."""
    global _genai, _genai_types, _genai_errors
    if _genai is None:
        try:
            from google import genai
            from google.genai import types, errors
            _genai = genai
            _genai_types = types
            _genai_errors = errors
        except ImportError:
            print("ERROR: google-genai package not installed. Run: pip install google-genai")
            sys.exit(1)


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOTENV_PATH = PROJECT_ROOT / ".env"
OUTPUT_DIR = PROJECT_ROOT / "assets" / "generated"
LOG_PATH = OUTPUT_DIR / "image-log.csv"

MODELS = {
    "flash": {
        "openrouter_id": "google/gemini-2.5-flash-image",
        "gemini_id": "gemini-2.5-flash-image",
        "cost_per_image": 0.039,
        "label": "Nano Banana (Flash)",
    },
    "pro": {
        "openrouter_id": "google/gemini-3-pro-image-preview",
        "gemini_id": "gemini-3-pro-image-preview",
        "cost_per_image": 0.134,
        "label": "Nano Banana Pro",
    },
}

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# CSV log columns (backend added — backward-compatible with old logs)
LOG_COLUMNS = [
    "timestamp", "model", "backend", "comic_id", "frame", "prompt",
    "aspect_ratio", "filename", "cost_usd", "cumulative_usd",
    "duration_sec", "status",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_env():
    if DOTENV_PATH.exists():
        for line in DOTENV_PATH.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                os.environ.setdefault(key.strip(), val.strip())


def get_openrouter_key() -> str:
    load_env()
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        print("ERROR: OPENROUTER_API_KEY not found in environment or .env")
        sys.exit(1)
    return key


def get_gemini_key() -> str:
    load_env()
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        print("ERROR: GEMINI_API_KEY not found in environment or .env")
        sys.exit(1)
    return key


def slugify(text: str, max_len: int = 40) -> str:
    import re
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:max_len]


def ensure_log():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    if not LOG_PATH.exists():
        with open(LOG_PATH, "w", newline="") as f:
            csv.writer(f).writerow(LOG_COLUMNS)
    else:
        # Migrate old CSV: add 'backend' column if missing
        with open(LOG_PATH, "r") as f:
            reader = csv.reader(f)
            header = next(reader, None)
        if header and "backend" not in header:
            _migrate_log_add_backend()


def _migrate_log_add_backend():
    """One-time migration: insert 'backend' column after 'model' in existing CSV."""
    rows = []
    with open(LOG_PATH, "r") as f:
        reader = csv.reader(f)
        old_header = next(reader)
        for row in reader:
            rows.append(row)

    # Insert 'backend' at position 2 (after 'model')
    model_idx = old_header.index("model") if "model" in old_header else 1
    new_header = old_header[:model_idx + 1] + ["backend"] + old_header[model_idx + 1:]

    with open(LOG_PATH, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(new_header)
        for row in rows:
            # Insert empty backend for old rows
            new_row = row[:model_idx + 1] + [""] + row[model_idx + 1:]
            writer.writerow(new_row)
    print(f"  [Log migration] Added 'backend' column to {LOG_PATH.name}")


def get_cumulative_cost() -> float:
    if not LOG_PATH.exists():
        return 0.0
    total = 0.0
    with open(LOG_PATH, "r") as f:
        for row in csv.DictReader(f):
            try:
                total += float(row["cost_usd"])
            except (ValueError, KeyError):
                pass
    return total


def log_generation(model: str, prompt: str, aspect: str, filename: str,
                   cost: float, duration: float, status: str,
                   comic_id: str = "", frame: str = "",
                   backend: str = "gemini") -> float:
    cumulative = get_cumulative_cost() + cost
    with open(LOG_PATH, "a", newline="") as f:
        csv.writer(f).writerow([
            datetime.now(timezone.utc).isoformat(timespec="seconds"),
            model, backend, comic_id, frame, prompt[:200], aspect, filename,
            f"{cost:.4f}", f"{cumulative:.4f}", f"{duration:.1f}", status,
        ])
    return cumulative


def encode_image_file(path: str | Path) -> dict:
    """Encode an image file as a base64 data URL content part (OpenRouter format)."""
    ref_file = Path(path)
    if not ref_file.exists():
        raise FileNotFoundError(f"Image not found: {path}")
    with open(ref_file, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()
    mime = "image/png" if ref_file.suffix.lower() == ".png" else "image/jpeg"
    return {
        "type": "image_url",
        "image_url": {"url": f"data:{mime};base64,{img_b64}"},
    }


# ---------------------------------------------------------------------------
# OpenRouter backend (legacy)
# ---------------------------------------------------------------------------

def _call_openrouter(messages: list, model_key: str) -> dict:
    """Send a messages array to OpenRouter. Returns {raw, duration} or {error, duration}."""
    api_key = get_openrouter_key()
    model_info = MODELS[model_key]

    payload = {
        "model": model_info["openrouter_id"],
        "modalities": ["image", "text"],
        "messages": messages,
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/agents-for-everyone",
        "X-Title": "Agents for Everyone",
    }

    start = time.time()
    resp = requests.post(OPENROUTER_URL, json=payload, headers=headers, timeout=120)
    duration = time.time() - start

    if resp.status_code != 200:
        return {"error": f"HTTP {resp.status_code}: {resp.text[:500]}", "duration": duration}

    return {"raw": resp.json(), "duration": duration}


def _build_openrouter_message(prompt: str, reference_images: list[str] | None = None) -> dict:
    """Build a user message dict for OpenRouter, optionally with reference images."""
    if reference_images:
        parts = []
        for ref_path in reference_images:
            parts.append(encode_image_file(ref_path))
        parts.append({"type": "text", "text": prompt})
        return {"role": "user", "content": parts}
    return {"role": "user", "content": prompt}


def _extract_openrouter_image(result: dict) -> tuple[str | None, str | None]:
    """Extract base64 image and text from an OpenRouter result dict."""
    raw = result.get("raw", {})
    choices = raw.get("choices", [])
    if not choices:
        return None, None

    message = choices[0].get("message", {})
    text = message.get("content", "")
    image_b64 = None

    def from_data_url(url: str) -> str | None:
        return url.split(",", 1)[-1] if url.startswith("data:") else None

    for img_data in message.get("images", []) or raw.get("images", []):
        if image_b64:
            break
        if isinstance(img_data, dict):
            if img_data.get("type") == "image_url":
                image_b64 = from_data_url(img_data.get("image_url", {}).get("url", ""))
            if not image_b64:
                image_b64 = img_data.get("b64_json") or img_data.get("data")
            if not image_b64 and "url" in img_data:
                image_b64 = from_data_url(img_data["url"])
        elif isinstance(img_data, str):
            image_b64 = from_data_url(img_data) or img_data

    if not image_b64 and isinstance(message.get("content"), list):
        for part in message["content"]:
            if isinstance(part, dict):
                if part.get("type") == "image_url":
                    image_b64 = from_data_url(part.get("image_url", {}).get("url", ""))
                elif part.get("type") == "image":
                    image_b64 = part.get("data") or part.get("b64_json")

    return image_b64, text


def _build_openrouter_assistant_with_image(result: dict, image_b64: str) -> dict:
    """Reconstruct an assistant message with the generated image for multi-turn."""
    text = result.get("raw", {}).get("choices", [{}])[0].get("message", {}).get("content", "")
    return {
        "role": "assistant",
        "content": [
            {"type": "text", "text": text or ""},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_b64}"}},
        ],
    }


# ---------------------------------------------------------------------------
# Gemini backend (native SDK)
# ---------------------------------------------------------------------------

def _get_gemini_client():
    """Create and return a Gemini SDK client."""
    _ensure_genai()
    api_key = get_gemini_key()
    return _genai.Client(api_key=api_key)


def _build_gemini_contents(prompt: str, reference_images: list[str] | None = None) -> list:
    """Build a contents array with interleaved reference images and labels."""
    contents = []
    if reference_images:
        for ref_path in reference_images:
            ref_file = Path(ref_path)
            if not ref_file.exists():
                raise FileNotFoundError(f"Image not found: {ref_path}")
            contents.append(Image.open(ref_file))
            # Derive a readable name from the filename
            name = ref_file.stem.replace("-ref-sheet", "").replace("-", " ").title()
            contents.append(f"Above is the {name} reference. Match this character exactly.")
    contents.append(prompt)
    return contents


def _make_gemini_config(aspect: str = "1:1", resolution: str | None = None,
                        system_prompt: str | None = None,
                        use_system_instructions: bool = False):
    """Build a GenerateContentConfig for the Gemini SDK."""
    _ensure_genai()

    image_kwargs = {"aspect_ratio": aspect}
    if resolution:
        image_kwargs["image_size"] = resolution

    config_kwargs = {
        "response_modalities": ["TEXT", "IMAGE"],
        "image_config": _genai_types.ImageConfig(**image_kwargs),
    }

    if use_system_instructions and system_prompt:
        config_kwargs["system_instruction"] = system_prompt

    return _genai_types.GenerateContentConfig(**config_kwargs)


def _call_gemini(contents: list, model_key: str, config) -> dict:
    """Single-turn generation via native Gemini SDK."""
    client = _get_gemini_client()
    model_info = MODELS[model_key]

    start = time.time()
    try:
        response = client.models.generate_content(
            model=model_info["gemini_id"],
            contents=contents,
            config=config,
        )
        duration = time.time() - start
        return {"raw": response, "duration": duration}
    except Exception as e:
        duration = time.time() - start
        return {"error": str(e), "duration": duration}


def _extract_gemini_image(response) -> tuple[str | None, str | None]:
    """Extract base64-encoded image and text from a Gemini SDK response."""
    text_parts = []
    image_b64 = None
    for part in response.parts:
        if part.text is not None:
            text_parts.append(part.text)
        elif part.inline_data is not None:
            # Use raw bytes from inline_data, then re-encode via PIL to ensure PNG
            raw_bytes = part.inline_data.data
            pil_img = Image.open(io.BytesIO(raw_bytes))
            buf = io.BytesIO()
            pil_img.save(buf, "PNG")
            image_b64 = base64.b64encode(buf.getvalue()).decode()
    text = "\n".join(text_parts) if text_parts else None
    return image_b64, text


# ---------------------------------------------------------------------------
# High-level generation functions
# ---------------------------------------------------------------------------

def generate_image(prompt: str, model_key: str = "flash",
                   aspect: str = "1:1",
                   system_prompt: str | None = None,
                   reference_images: list[str] | None = None,
                   backend: str = "gemini",
                   resolution: str | None = None,
                   use_system_instructions: bool = False) -> dict:
    """Single-image generation. Returns {raw, duration} or {error, duration}."""
    if backend == "gemini":
        config = _make_gemini_config(
            aspect=aspect,
            resolution=resolution,
            system_prompt=system_prompt,
            use_system_instructions=use_system_instructions,
        )
        contents = _build_gemini_contents(prompt, reference_images)
        # If system prompt provided but not using system_instructions, prepend to prompt
        if system_prompt and not use_system_instructions:
            contents[-1] = f"{system_prompt}\n\n{contents[-1]}"
        return _call_gemini(contents, model_key, config)
    else:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append(_build_openrouter_message(prompt, reference_images))
        return _call_openrouter(messages, model_key)


def generate_comic_frames(
    comic_id: str,
    setting: str,
    frame_a_desc: str,
    frame_b_desc: str,
    style_block: str,
    character_blocks: str,
    model_key: str = "pro",
    aspect: str = "16:9",
    reference_images: list[str] | None = None,
    backend: str = "gemini",
    resolution: str | None = None,
    use_system_instructions: bool = False,
) -> dict:
    """
    Generate two comic frames sequentially in a linked conversation session.

    With the Gemini backend, uses native chat sessions that preserve thought
    signatures for character consistency. With OpenRouter, manually reconstructs
    conversation history.
    """
    if backend == "gemini":
        return _generate_comic_gemini(
            comic_id, setting, frame_a_desc, frame_b_desc,
            style_block, character_blocks, model_key, aspect,
            reference_images, resolution, use_system_instructions,
        )
    else:
        return _generate_comic_openrouter(
            comic_id, setting, frame_a_desc, frame_b_desc,
            style_block, character_blocks, model_key, aspect,
            reference_images,
        )


def _generate_comic_gemini(
    comic_id, setting, frame_a_desc, frame_b_desc,
    style_block, character_blocks, model_key, aspect,
    reference_images, resolution, use_system_instructions,
) -> dict:
    """Generate comic frames using native Gemini chat session."""
    _ensure_genai()
    client = _get_gemini_client()
    model_info = MODELS[model_key]
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    ensure_log()

    # --- Build config ---
    image_kwargs = {"aspect_ratio": aspect}
    if resolution:
        image_kwargs["image_size"] = resolution

    config_kwargs = {
        "response_modalities": ["TEXT", "IMAGE"],
        "image_config": _genai_types.ImageConfig(**image_kwargs),
    }

    # Move frozen blocks to system instructions if enabled
    if use_system_instructions and (style_block or character_blocks):
        sys_parts = []
        if style_block:
            sys_parts.append(style_block)
        if character_blocks:
            sys_parts.append(character_blocks)
        sys_parts.append(
            "CONSTRAINTS: Do not change any character's face, facial features, "
            "skin tone, body shape, or identity. Maintain identical art style, "
            "color palette, and lighting across frames."
        )
        config_kwargs["system_instruction"] = "\n\n".join(sys_parts)

    chat = client.chats.create(
        model=model_info["gemini_id"],
        config=_genai_types.GenerateContentConfig(**config_kwargs),
    )

    # --- Build frozen preamble (included in user message unless using system instructions) ---
    if use_system_instructions:
        frozen_preamble = f"SETTING (identical in both frames): {setting}"
    else:
        frozen_preamble = f"""{style_block}

{character_blocks}

SETTING (identical in both frames): {setting}

CONSTRAINTS: Do not change any character's face, facial features, skin tone, body shape, or identity. Maintain identical art style, color palette, and lighting across frames. Frames are part of a continuous two-panel comic sequence."""

    # --- Frame A ---
    frame_a_prompt = f"""{frozen_preamble}

FRAME A of 2: {frame_a_desc}

Generate Frame A as a clean illustration panel. No speech bubbles or text — dialogue will be added in post-production."""

    # Build Frame A contents with interleaved refs
    frame_a_contents = []
    if reference_images:
        for ref_path in reference_images:
            ref_file = Path(ref_path)
            if not ref_file.exists():
                raise FileNotFoundError(f"Image not found: {ref_path}")
            frame_a_contents.append(Image.open(ref_file))
            name = ref_file.stem.replace("-ref-sheet", "").replace("-", " ").title()
            frame_a_contents.append(f"Above is the {name} reference. Match this character exactly.")
    frame_a_contents.append(frame_a_prompt)

    print(f"  [Frame A] Generating...")
    start = time.time()
    try:
        response_a = chat.send_message(frame_a_contents)
    except Exception as e:
        return {"error": f"Frame A failed: {e}"}
    duration_a = time.time() - start

    frame_a_b64, _ = _extract_gemini_image(response_a)
    if not frame_a_b64:
        return {"error": "Frame A: no image in response"}

    frame_a_name = f"{comic_id}-frame-a-{timestamp}"
    frame_a_path = _save_frame(frame_a_b64, frame_a_name)
    print(f"  [Frame A] Saved: {frame_a_path}")

    log_generation(
        model=model_key, prompt=frame_a_prompt, aspect=aspect,
        filename=frame_a_path.name, cost=model_info["cost_per_image"],
        duration=duration_a, status="ok",
        comic_id=comic_id, frame="a", backend="gemini",
    )

    # --- Frame B — conversation context carries character identity ---
    frame_b_prompt = f"""{frozen_preamble}

FRAME B of 2 (continuing directly from Frame A):
{frame_b_desc}

WHAT MUST STAY THE SAME: characters' faces and bodies, the setting, the lighting, the art style.

Generate Frame B as a clean illustration panel. No speech bubbles or text."""

    print(f"  [Frame B] Generating (with conversation context from Frame A)...")
    start = time.time()
    try:
        response_b = chat.send_message(frame_b_prompt)
    except Exception as e:
        return {
            "frame_a": {"image_b64": frame_a_b64, "path": frame_a_path, "duration": duration_a},
            "error": f"Frame B failed: {e}",
        }
    duration_b = time.time() - start

    frame_b_b64, _ = _extract_gemini_image(response_b)
    if not frame_b_b64:
        return {
            "frame_a": {"image_b64": frame_a_b64, "path": frame_a_path, "duration": duration_a},
            "error": "Frame B: no image in response",
        }

    frame_b_name = f"{comic_id}-frame-b-{timestamp}"
    frame_b_path = _save_frame(frame_b_b64, frame_b_name)
    print(f"  [Frame B] Saved: {frame_b_path}")

    log_generation(
        model=model_key, prompt=frame_b_prompt, aspect=aspect,
        filename=frame_b_path.name, cost=model_info["cost_per_image"],
        duration=duration_b, status="ok",
        comic_id=comic_id, frame="b", backend="gemini",
    )

    return {
        "frame_a": {"image_b64": frame_a_b64, "path": frame_a_path, "duration": duration_a},
        "frame_b": {"image_b64": frame_b_b64, "path": frame_b_path, "duration": duration_b},
    }


def _generate_comic_openrouter(
    comic_id, setting, frame_a_desc, frame_b_desc,
    style_block, character_blocks, model_key, aspect,
    reference_images,
) -> dict:
    """Generate comic frames using OpenRouter (legacy manual conversation reconstruction)."""
    model_info = MODELS[model_key]
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    ensure_log()

    frozen_preamble = f"""{style_block}

{character_blocks}

SETTING (identical in both frames): {setting}

CONSTRAINTS: Do not change any character's face, facial features, skin tone, body shape, or identity. Maintain identical art style, color palette, and lighting across frames. Frames are part of a continuous two-panel comic sequence."""

    # --- Frame A ---
    frame_a_prompt = f"""{frozen_preamble}

FRAME A of 2: {frame_a_desc}

Generate Frame A as a clean illustration panel. No speech bubbles or text — dialogue will be added in post-production."""

    print(f"  [Frame A] Generating...")
    frame_a_result = generate_image(
        prompt=frame_a_prompt, model_key=model_key, aspect=aspect,
        reference_images=reference_images, backend="openrouter",
    )

    if "error" in frame_a_result:
        return {"error": f"Frame A failed: {frame_a_result['error']}"}

    frame_a_b64, _ = _extract_openrouter_image(frame_a_result)
    if not frame_a_b64:
        return {"error": "Frame A: no image in response"}

    frame_a_name = f"{comic_id}-frame-a-{timestamp}"
    frame_a_path = _save_frame(frame_a_b64, frame_a_name)
    print(f"  [Frame A] Saved: {frame_a_path}")

    log_generation(
        model=model_key, prompt=frame_a_prompt, aspect=aspect,
        filename=frame_a_path.name, cost=model_info["cost_per_image"],
        duration=frame_a_result["duration"], status="ok",
        comic_id=comic_id, frame="a", backend="openrouter",
    )

    # --- Frame B — manual multi-turn ---
    frame_a_message = _build_openrouter_message(frame_a_prompt, reference_images)
    frame_a_assistant = _build_openrouter_assistant_with_image(frame_a_result, frame_a_b64)

    frame_b_prompt = f"""{frozen_preamble}

FRAME B of 2 (continuing directly from Frame A):
{frame_b_desc}

WHAT CHANGED from Frame A: {frame_b_desc}
WHAT MUST STAY THE SAME: characters' faces and bodies, the setting, the lighting, the art style.

The previous image (Frame A) is attached as visual reference. Match it exactly for all unchanged elements.

Generate Frame B as a clean illustration panel. No speech bubbles or text."""

    frame_b_refs = list(reference_images or []) + [str(frame_a_path)]
    frame_b_user_message = _build_openrouter_message(frame_b_prompt, frame_b_refs)
    frame_b_messages = [frame_a_message, frame_a_assistant, frame_b_user_message]

    print(f"  [Frame B] Generating (with Frame A as visual anchor)...")
    start = time.time()
    frame_b_result = _call_openrouter(frame_b_messages, model_key)
    duration = time.time() - start

    if "error" in frame_b_result:
        return {
            "frame_a": {"image_b64": frame_a_b64, "path": frame_a_path, "duration": frame_a_result["duration"]},
            "error": f"Frame B failed: {frame_b_result['error']}",
        }

    frame_b_b64, _ = _extract_openrouter_image(frame_b_result)
    if not frame_b_b64:
        return {
            "frame_a": {"image_b64": frame_a_b64, "path": frame_a_path, "duration": frame_a_result["duration"]},
            "error": "Frame B: no image in response",
        }

    frame_b_name = f"{comic_id}-frame-b-{timestamp}"
    frame_b_path = _save_frame(frame_b_b64, frame_b_name)
    print(f"  [Frame B] Saved: {frame_b_path}")

    log_generation(
        model=model_key, prompt=frame_b_prompt, aspect=aspect,
        filename=frame_b_path.name, cost=model_info["cost_per_image"],
        duration=frame_b_result["duration"], status="ok",
        comic_id=comic_id, frame="b", backend="openrouter",
    )

    return {
        "frame_a": {"image_b64": frame_a_b64, "path": frame_a_path, "duration": frame_a_result["duration"]},
        "frame_b": {"image_b64": frame_b_b64, "path": frame_b_path, "duration": frame_b_result["duration"]},
    }


# ---------------------------------------------------------------------------
# Image editing (Gemini only)
# ---------------------------------------------------------------------------

def edit_image(image_path: str, edit_prompt: str, model_key: str = "pro",
               aspect: str | None = None, resolution: str | None = None) -> dict:
    """
    Edit an existing image using native Gemini SDK.

    Sends the image + edit prompt to the model and returns the modified image.
    Returns {raw, duration, image_b64} or {error, duration}.
    """
    _ensure_genai()
    client = _get_gemini_client()
    model_info = MODELS[model_key]

    img_path = Path(image_path)
    if not img_path.exists():
        return {"error": f"Image not found: {image_path}", "duration": 0}

    pil_img = Image.open(img_path)
    contents = [pil_img, edit_prompt]

    image_kwargs = {}
    if aspect:
        image_kwargs["aspect_ratio"] = aspect
    if resolution:
        image_kwargs["image_size"] = resolution

    config_kwargs = {
        "response_modalities": ["TEXT", "IMAGE"],
    }
    if image_kwargs:
        config_kwargs["image_config"] = _genai_types.ImageConfig(**image_kwargs)

    config = _genai_types.GenerateContentConfig(**config_kwargs)

    start = time.time()
    try:
        response = client.models.generate_content(
            model=model_info["gemini_id"],
            contents=contents,
            config=config,
        )
        duration = time.time() - start
    except Exception as e:
        duration = time.time() - start
        return {"error": str(e), "duration": duration}

    image_b64, text = _extract_gemini_image(response)
    if not image_b64:
        return {"error": "No image in edit response", "duration": duration}

    return {"raw": response, "duration": duration, "image_b64": image_b64, "text": text}


# ---------------------------------------------------------------------------
# Image processing helpers
# ---------------------------------------------------------------------------

def _save_frame(image_b64: str, name: str) -> Path:
    """Decode and save a PNG frame. Returns the saved path."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    filepath = OUTPUT_DIR / f"{name}.png"
    img_bytes = base64.b64decode(image_b64)
    img = Image.open(io.BytesIO(img_bytes))
    img.save(filepath, "PNG")
    return filepath


def save_and_resize(image_b64: str, name: str, resize: str | None = None) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{name}-{timestamp}.png"
    filepath = OUTPUT_DIR / filename

    img_bytes = base64.b64decode(image_b64)
    img = Image.open(io.BytesIO(img_bytes))
    img.save(filepath, "PNG")
    print(f"  Saved: {filepath} ({img.size[0]}x{img.size[1]})")

    if resize:
        w, h = map(int, resize.split("x"))
        resized = img.resize((w, h), Image.LANCZOS)
        resized_path = OUTPUT_DIR / f"{name}-{timestamp}-{resize}.png"
        resized.save(resized_path, "PNG")
        print(f"  Resized: {resized_path} ({w}x{h})")

    return filepath


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Generate images via native Gemini SDK or OpenRouter",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # Mode selection (mutually exclusive)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--comic", metavar="COMIC_ID",
                      help="Generate a two-frame comic (use with --frame-a, --frame-b, --setting)")
    mode.add_argument("--edit", metavar="IMAGE_PATH",
                      help="Edit an existing image (Gemini backend only)")

    parser.add_argument("prompt", nargs="?", help="Image prompt (single-image mode) or edit prompt (--edit mode)")
    parser.add_argument("--model", choices=["flash", "pro"], default="flash",
                        help="Model: flash (~$0.04/img) or pro (~$0.13/img)")
    parser.add_argument("--backend", choices=["gemini", "openrouter"], default="gemini",
                        help="Backend: gemini (default, native SDK) or openrouter (legacy)")
    parser.add_argument("--aspect", default="1:1",
                        help="Aspect ratio (1:1, 16:9, 9:16, 3:2, etc.)")
    parser.add_argument("--resolution", choices=["1K", "2K", "4K"], default=None,
                        help="Image resolution (Gemini backend only)")
    parser.add_argument("--name", default=None,
                        help="Output filename prefix (single-image mode)")
    parser.add_argument("--resize", default=None,
                        help="Resize to WxH e.g. 800x600 (single-image mode only)")
    parser.add_argument("--ref", action="append", default=None,
                        help="Reference image path(s) — repeatable")
    parser.add_argument("--system", default=None,
                        help="System prompt")
    parser.add_argument("--use-system-instructions", action="store_true",
                        help="Pass --system as Gemini system_instruction (experimental)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be sent without calling the API")

    # Comic-specific args
    parser.add_argument("--setting", default="",
                        help="[Comic] Frozen setting description (shared by both frames)")
    parser.add_argument("--frame-a", dest="frame_a", default="",
                        help="[Comic] Frame A action/expression description")
    parser.add_argument("--frame-b", dest="frame_b", default="",
                        help="[Comic] Frame B action/expression description (what changed)")
    parser.add_argument("--style", default="",
                        help="[Comic] Art style block (overrides style guide lookup)")
    parser.add_argument("--characters", default="",
                        help="[Comic] Character description block")

    args = parser.parse_args()
    model_info = MODELS[args.model]
    backend = args.backend

    # ---- EDIT MODE ----
    if args.edit:
        if backend == "openrouter":
            print("ERROR: --edit mode requires the Gemini backend (--backend gemini)")
            sys.exit(1)
        if not args.prompt:
            parser.error("An edit prompt is required in --edit mode")

        print(f"Mode:     Edit")
        print(f"Model:    {model_info['label']}")
        print(f"Backend:  {backend}")
        print(f"Source:   {args.edit}")
        print(f"Prompt:   {args.prompt[:100]}...")
        print(f"Cost:     ~${model_info['cost_per_image']:.3f}")
        print()

        if args.dry_run:
            print("[DRY RUN] No API call made.")
            return

        ensure_log()
        print("Editing...")

        result = edit_image(
            image_path=args.edit,
            edit_prompt=args.prompt,
            model_key=args.model,
            aspect=args.aspect if args.aspect != "1:1" else None,
            resolution=args.resolution,
        )

        if "error" in result:
            print(f"ERROR: {result['error']}")
            log_generation(
                model=args.model, prompt=args.prompt, aspect=args.aspect,
                filename="", cost=0, duration=result.get("duration", 0),
                status=f"error: {result['error'][:100]}",
                frame="edit", backend=backend,
            )
            sys.exit(1)

        if result.get("text"):
            print(f"  Model said: {result['text'][:200]}")

        # Save edited image
        source_stem = Path(args.edit).stem
        edit_name = f"{source_stem}-edit"
        filepath = save_and_resize(result["image_b64"], edit_name, args.resize)

        cumulative = log_generation(
            model=args.model, prompt=args.prompt, aspect=args.aspect,
            filename=filepath.name, cost=model_info["cost_per_image"],
            duration=result["duration"], status="ok",
            frame="edit", backend=backend,
        )

        print()
        print(f"  Cost this edit:   ${model_info['cost_per_image']:.3f}")
        print(f"  Cumulative spend: ${cumulative:.3f}")
        print("  Done!")
        return

    # ---- COMIC MODE ----
    if args.comic:
        comic_id = args.comic
        cost_estimate = model_info["cost_per_image"] * 2
        print(f"Mode:    Comic ({comic_id})")
        print(f"Model:   {model_info['label']}")
        print(f"Backend: {backend}")
        print(f"Frames:  2  →  estimated cost ~${cost_estimate:.3f}")
        print(f"Aspect:  {args.aspect}")
        if args.resolution:
            print(f"Resolution: {args.resolution}")
        if args.ref:
            print(f"Refs:    {len(args.ref)} reference image(s)")
        print()

        if not args.frame_a or not args.frame_b:
            print("ERROR: --frame-a and --frame-b are required in comic mode")
            sys.exit(1)

        if args.dry_run:
            print("[DRY RUN] No API call made.")
            print(f"  Would generate: {comic_id}-frame-a.png + {comic_id}-frame-b.png")
            return

        ensure_log()
        result = generate_comic_frames(
            comic_id=comic_id,
            setting=args.setting,
            frame_a_desc=args.frame_a,
            frame_b_desc=args.frame_b,
            style_block=args.style,
            character_blocks=args.characters,
            model_key=args.model,
            aspect=args.aspect,
            reference_images=args.ref,
            backend=backend,
            resolution=args.resolution,
            use_system_instructions=args.use_system_instructions,
        )

        if "error" in result and "frame_a" not in result:
            print(f"ERROR: {result['error']}")
            sys.exit(1)

        if "error" in result:
            print(f"WARNING: {result['error']}")
            print("Frame A was saved. Frame B failed.")

        total_cost = model_info["cost_per_image"] * (2 if "frame_b" in result else 1)
        cumulative = get_cumulative_cost()
        print()
        print(f"  Cost this comic:  ${total_cost:.3f}")
        print(f"  Cumulative spend: ${cumulative:.3f}")
        print("  Done!")
        return

    # ---- SINGLE IMAGE MODE ----
    if not args.prompt:
        parser.error("A prompt is required in single-image mode (or use --comic / --edit)")

    name = args.name or slugify(args.prompt)

    print(f"Model:   {model_info['label']}")
    print(f"Backend: {backend}")
    print(f"Cost:    ~${model_info['cost_per_image']:.3f}/image")
    print(f"Prompt:  {args.prompt[:100]}...")
    print(f"Aspect:  {args.aspect}")
    if args.resolution:
        print(f"Resolution: {args.resolution}")
    if args.ref:
        print(f"Refs:    {len(args.ref)} reference image(s)")
    print()

    if args.dry_run:
        print("[DRY RUN] No API call made.")
        return

    ensure_log()

    print("Generating...")
    result = generate_image(
        prompt=args.prompt,
        model_key=args.model,
        aspect=args.aspect,
        system_prompt=args.system,
        reference_images=args.ref,
        backend=backend,
        resolution=args.resolution,
        use_system_instructions=args.use_system_instructions,
    )

    if "error" in result:
        print(f"ERROR: {result['error']}")
        log_generation(
            model=args.model, prompt=args.prompt, aspect=args.aspect,
            filename="", cost=0, duration=result["duration"],
            status=f"error: {result['error'][:100]}",
            backend=backend,
        )
        sys.exit(1)

    # Extract image based on backend
    if backend == "gemini":
        image_b64, text = _extract_gemini_image(result["raw"])
    else:
        image_b64, text = _extract_openrouter_image(result)

    if not image_b64:
        print("ERROR: No image in response.")
        if backend == "openrouter":
            print("Raw (first 1000 chars):")
            print(json.dumps(result.get("raw", {}), indent=2)[:1000])
        log_generation(
            model=args.model, prompt=args.prompt, aspect=args.aspect,
            filename="", cost=0, duration=result["duration"],
            status="error: no image in response",
            backend=backend,
        )
        sys.exit(1)

    if text:
        print(f"  Model said: {text[:200]}")

    filepath = save_and_resize(image_b64, name, args.resize)

    cumulative = log_generation(
        model=args.model, prompt=args.prompt, aspect=args.aspect,
        filename=filepath.name, cost=model_info["cost_per_image"],
        duration=result["duration"], status="ok",
        backend=backend,
    )

    print()
    print(f"  Cost this image:  ${model_info['cost_per_image']:.3f}")
    print(f"  Cumulative spend: ${cumulative:.3f}")
    print("  Done!")


if __name__ == "__main__":
    main()
