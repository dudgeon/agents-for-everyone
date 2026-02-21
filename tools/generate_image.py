#!/usr/bin/env python3
"""
Nano Banana image generation via OpenRouter.

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

Models:
    flash  = Nano Banana (Gemini 2.5 Flash Image)  ~$0.039/image
    pro    = Nano Banana Pro (Gemini 3 Pro Image)  ~$0.134/image

Single images → assets/generated/<name>-<timestamp>.png
Comic frames  → assets/generated/<id>-frame-a-<timestamp>.png
                assets/generated/<id>-frame-b-<timestamp>.png
Costs logged  → assets/generated/image-log.csv
"""

from __future__ import annotations

import argparse
import base64
import csv
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from PIL import Image

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOTENV_PATH = PROJECT_ROOT / ".env"
OUTPUT_DIR = PROJECT_ROOT / "assets" / "generated"
LOG_PATH = OUTPUT_DIR / "image-log.csv"

MODELS = {
    "flash": {
        "id": "google/gemini-2.5-flash-image",
        "cost_per_image": 0.039,
        "label": "Nano Banana (Flash)",
    },
    "pro": {
        "id": "google/gemini-3-pro-image-preview",
        "cost_per_image": 0.134,
        "label": "Nano Banana Pro",
    },
}

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

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


def get_api_key():
    load_env()
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        print("ERROR: OPENROUTER_API_KEY not found in environment or .env")
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
            writer = csv.writer(f)
            writer.writerow([
                "timestamp", "model", "comic_id", "frame", "prompt",
                "aspect_ratio", "filename", "cost_usd", "cumulative_usd",
                "duration_sec", "status",
            ])


def get_cumulative_cost() -> float:
    if not LOG_PATH.exists():
        return 0.0
    total = 0.0
    with open(LOG_PATH, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                total += float(row["cost_usd"])
            except (ValueError, KeyError):
                pass
    return total


def log_generation(model: str, prompt: str, aspect: str, filename: str,
                   cost: float, duration: float, status: str,
                   comic_id: str = "", frame: str = ""):
    cumulative = get_cumulative_cost() + cost
    with open(LOG_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now(timezone.utc).isoformat(timespec="seconds"),
            model, comic_id, frame, prompt[:200], aspect, filename,
            f"{cost:.4f}", f"{cumulative:.4f}", f"{duration:.1f}", status,
        ])
    return cumulative


def encode_image_file(path: str | Path) -> dict:
    """Encode an image file as a base64 data URL content part."""
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
# Core API call — messages-based (supports single-turn and multi-turn)
# ---------------------------------------------------------------------------

def _call_api(messages: list, model_key: str) -> dict:
    """Send a messages array to OpenRouter. Returns {raw, duration} or {error, duration}."""
    api_key = get_api_key()
    model_info = MODELS[model_key]

    payload = {
        "model": model_info["id"],
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


def _build_user_message(prompt: str, reference_images: list[str] | None = None) -> dict:
    """Build a user message dict, optionally with reference images as content parts."""
    if reference_images:
        parts = []
        for ref_path in reference_images:
            parts.append(encode_image_file(ref_path))
        parts.append({"type": "text", "text": prompt})
        return {"role": "user", "content": parts}
    return {"role": "user", "content": prompt}


def _extract_image_and_text(result: dict) -> tuple[str | None, str | None]:
    """Extract base64 image and text from an API result dict."""
    raw = result.get("raw", {})
    choices = raw.get("choices", [])
    if not choices:
        return None, None

    message = choices[0].get("message", {})
    text = message.get("content", "")
    image_b64 = None

    def from_data_url(url: str) -> str | None:
        return url.split(",", 1)[-1] if url.startswith("data:") else None

    # OpenRouter format: message.images[]
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

    # Fallback: content as array of parts
    if not image_b64 and isinstance(message.get("content"), list):
        for part in message["content"]:
            if isinstance(part, dict):
                if part.get("type") == "image_url":
                    image_b64 = from_data_url(part.get("image_url", {}).get("url", ""))
                elif part.get("type") == "image":
                    image_b64 = part.get("data") or part.get("b64_json")

    return image_b64, text


def _build_assistant_message_with_image(result: dict, image_b64: str) -> dict:
    """
    Reconstruct an assistant message to continue a multi-turn conversation.
    Attaches the generated image so the next turn has visual context of frame A.
    """
    text = result.get("raw", {}).get("choices", [{}])[0].get("message", {}).get("content", "")
    return {
        "role": "assistant",
        "content": [
            {"type": "text", "text": text or ""},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{image_b64}"},
            },
        ],
    }


# ---------------------------------------------------------------------------
# High-level generation functions
# ---------------------------------------------------------------------------

def generate_image(prompt: str, model_key: str = "flash",
                   aspect: str = "1:1",
                   system_prompt: str | None = None,
                   reference_images: list[str] | None = None) -> dict:
    """Single-image generation. Returns {raw, duration} or {error, duration}."""
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append(_build_user_message(prompt, reference_images))
    return _call_api(messages, model_key)


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
) -> dict:
    """
    Generate two comic frames sequentially in a linked conversation session.

    Frame A is generated first. Frame A's output image is then attached as a
    visual reference when generating Frame B — so the model sees exactly what
    it produced and can maintain character appearance, setting, and lighting.

    Returns:
        {
          "frame_a": {"image_b64": ..., "path": ..., "duration": ...},
          "frame_b": {"image_b64": ..., "path": ..., "duration": ...},
          "error": "..." (only if failed),
        }
    """
    model_info = MODELS[model_key]
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    ensure_log()

    # --- Frozen blocks (identical across both frames) ---
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
        prompt=frame_a_prompt,
        model_key=model_key,
        aspect=aspect,
        reference_images=reference_images,
    )

    if "error" in frame_a_result:
        return {"error": f"Frame A failed: {frame_a_result['error']}"}

    frame_a_b64, frame_a_text = _extract_image_and_text(frame_a_result)
    if not frame_a_b64:
        return {"error": "Frame A: no image in response"}

    frame_a_name = f"{comic_id}-frame-a-{timestamp}"
    frame_a_path = _save_frame(frame_a_b64, frame_a_name)
    print(f"  [Frame A] Saved: {frame_a_path}")

    log_generation(
        model=model_key, prompt=frame_a_prompt, aspect=aspect,
        filename=frame_a_path.name, cost=model_info["cost_per_image"],
        duration=frame_a_result["duration"], status="ok",
        comic_id=comic_id, frame="a",
    )

    # --- Frame B — multi-turn: conversation history includes frame A ---
    # Build the conversation history so the model sees frame A as its own prior output
    frame_a_message = _build_user_message(frame_a_prompt, reference_images)
    frame_a_assistant = _build_assistant_message_with_image(frame_a_result, frame_a_b64)

    # Frame B user message: attach frame A as explicit visual reference too
    frame_b_prompt = f"""{frozen_preamble}

FRAME B of 2 (continuing directly from Frame A):
{frame_b_desc}

WHAT CHANGED from Frame A: {_delta(frame_a_desc, frame_b_desc)}
WHAT MUST STAY THE SAME: characters' faces and bodies, the setting, the lighting, the art style.

The previous image (Frame A) is attached as visual reference. Match it exactly for all unchanged elements.

Generate Frame B as a clean illustration panel. No speech bubbles or text."""

    # Frame B references: all original refs + frame A output image
    frame_b_refs = list(reference_images or []) + [str(frame_a_path)]

    frame_b_user_message = _build_user_message(frame_b_prompt, frame_b_refs)

    # Send with full conversation history from frame A turn
    frame_b_messages = [frame_a_message, frame_a_assistant, frame_b_user_message]

    print(f"  [Frame B] Generating (with Frame A as visual anchor)...")
    start = time.time()
    frame_b_result = _call_api(frame_b_messages, model_key)
    duration = time.time() - start

    if "error" in frame_b_result:
        return {
            "frame_a": {"image_b64": frame_a_b64, "path": frame_a_path, "duration": frame_a_result["duration"]},
            "error": f"Frame B failed: {frame_b_result['error']}",
        }

    frame_b_b64, _ = _extract_image_and_text(frame_b_result)
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
        comic_id=comic_id, frame="b",
    )

    return {
        "frame_a": {"image_b64": frame_a_b64, "path": frame_a_path, "duration": frame_a_result["duration"]},
        "frame_b": {"image_b64": frame_b_b64, "path": frame_b_path, "duration": frame_b_result["duration"]},
    }


def _delta(frame_a: str, frame_b: str) -> str:
    """Simple heuristic: return frame_b description as the delta (what changed)."""
    # In practice the caller passes specific descriptions; this surfaces it clearly.
    return frame_b


def _save_frame(image_b64: str, name: str) -> Path:
    """Decode and save a PNG frame. Returns the saved path."""
    import io
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    filepath = OUTPUT_DIR / f"{name}.png"
    img_bytes = base64.b64decode(image_b64)
    img = Image.open(io.BytesIO(img_bytes))
    img.save(filepath, "PNG")
    return filepath


# ---------------------------------------------------------------------------
# Image processing (single image)
# ---------------------------------------------------------------------------

def save_and_resize(image_b64: str, name: str, resize: str | None = None) -> Path:
    import io
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
        description="Generate images via Nano Banana / OpenRouter",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # Subcommand-style via mutually exclusive group
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--comic", metavar="COMIC_ID",
                      help="Generate a two-frame comic (use with --frame-a, --frame-b, --setting)")

    parser.add_argument("prompt", nargs="?", help="Image prompt (single-image mode)")
    parser.add_argument("--model", choices=["flash", "pro"], default="flash",
                        help="Model: flash (~$0.04/img) or pro (~$0.13/img)")
    parser.add_argument("--aspect", default="1:1",
                        help="Aspect ratio (1:1, 16:9, 9:16, 3:2, etc.)")
    parser.add_argument("--name", default=None,
                        help="Output filename prefix (single-image mode)")
    parser.add_argument("--resize", default=None,
                        help="Resize to WxH e.g. 800x600 (single-image mode only)")
    parser.add_argument("--ref", action="append", default=None,
                        help="Reference image path(s) — repeatable")
    parser.add_argument("--system", default=None,
                        help="System prompt (single-image mode)")
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

    # ---- COMIC MODE ----
    if args.comic:
        comic_id = args.comic
        cost_estimate = model_info["cost_per_image"] * 2
        print(f"Mode:   Comic ({comic_id})")
        print(f"Model:  {model_info['label']}")
        print(f"Frames: 2  →  estimated cost ~${cost_estimate:.3f}")
        print(f"Aspect: {args.aspect}")
        if args.ref:
            print(f"Refs:   {len(args.ref)} reference image(s)")
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
        parser.error("A prompt is required in single-image mode (or use --comic)")

    name = args.name or slugify(args.prompt)

    print(f"Model:  {model_info['label']} ({model_info['id']})")
    print(f"Cost:   ~${model_info['cost_per_image']:.3f}/image")
    print(f"Prompt: {args.prompt[:100]}...")
    print(f"Aspect: {args.aspect}")
    if args.ref:
        print(f"Refs:   {len(args.ref)} reference image(s)")
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
    )

    if "error" in result:
        print(f"ERROR: {result['error']}")
        log_generation(
            model=args.model, prompt=args.prompt, aspect=args.aspect,
            filename="", cost=0, duration=result["duration"],
            status=f"error: {result['error'][:100]}",
        )
        sys.exit(1)

    image_b64, text = _extract_image_and_text(result)

    if not image_b64:
        print("ERROR: No image in response.")
        print("Raw (first 1000 chars):")
        print(json.dumps(result.get("raw", {}), indent=2)[:1000])
        log_generation(
            model=args.model, prompt=args.prompt, aspect=args.aspect,
            filename="", cost=0, duration=result["duration"],
            status="error: no image in response",
        )
        sys.exit(1)

    if text:
        print(f"  Model said: {text[:200]}")

    filepath = save_and_resize(image_b64, name, args.resize)

    cumulative = log_generation(
        model=args.model, prompt=args.prompt, aspect=args.aspect,
        filename=filepath.name, cost=model_info["cost_per_image"],
        duration=result["duration"], status="ok",
    )

    print()
    print(f"  Cost this image:  ${model_info['cost_per_image']:.3f}")
    print(f"  Cumulative spend: ${cumulative:.3f}")
    print("  Done!")


if __name__ == "__main__":
    main()
