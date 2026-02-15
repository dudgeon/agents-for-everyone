#!/usr/bin/env python3
"""
Nano Banana image generation via OpenRouter.

Usage:
    python tools/generate_image.py "a watercolor painting of a penguin reading a book" \
        --model flash --aspect 16:9 --name penguin-reading

Models:
    flash   = Nano Banana (Gemini 2.5 Flash Image)  ~$0.039/image
    pro     = Nano Banana Pro (Gemini 3 Pro Image)   ~$0.134/image (1K/2K), ~$0.24/image (4K)

Images saved to: assets/generated/<name>-<timestamp>.png
Cost logged to:  assets/generated/image-log.csv
"""

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
        "cost_per_image": 0.134,  # 1K/2K default
        "label": "Nano Banana Pro",
    },
}

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_env():
    """Load .env file manually (avoid hard dep on dotenv at import time)."""
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
    """Create the CSV log file with headers if it doesn't exist."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    if not LOG_PATH.exists():
        with open(LOG_PATH, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp", "model", "prompt", "aspect_ratio",
                "resize", "filename", "cost_usd", "cumulative_usd",
                "duration_sec", "status",
            ])


def get_cumulative_cost() -> float:
    """Read the log and sum up costs so far."""
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


def log_generation(model: str, prompt: str, aspect: str, resize: str,
                   filename: str, cost: float, duration: float, status: str):
    cumulative = get_cumulative_cost() + cost
    with open(LOG_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now(timezone.utc).isoformat(timespec="seconds"),
            model, prompt[:200], aspect, resize, filename,
            f"{cost:.4f}", f"{cumulative:.4f}", f"{duration:.1f}", status,
        ])
    return cumulative


# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------

def generate_image(prompt: str, model_key: str = "flash",
                   aspect: str = "1:1",
                   system_prompt: str | None = None,
                   reference_images: list[str] | None = None) -> dict:
    """Call OpenRouter and return {raw, duration} or {error, duration}.

    Args:
        reference_images: List of file paths to reference images (for character consistency).
                         These get sent as base64-encoded image parts in the user message.
    """
    api_key = get_api_key()
    model_info = MODELS[model_key]

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})

    # Build user message — text + optional reference images
    if reference_images:
        import io as _io
        content_parts = []
        for ref_path in reference_images:
            ref_file = Path(ref_path)
            if not ref_file.exists():
                return {"error": f"Reference image not found: {ref_path}", "duration": 0}
            with open(ref_file, "rb") as f:
                img_b64 = base64.b64encode(f.read()).decode()
            mime = "image/png" if ref_file.suffix == ".png" else "image/jpeg"
            content_parts.append({
                "type": "image_url",
                "image_url": {"url": f"data:{mime};base64,{img_b64}"},
            })
        content_parts.append({"type": "text", "text": prompt})
        messages.append({"role": "user", "content": content_parts})
    else:
        messages.append({"role": "user", "content": prompt})

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
        return {
            "error": f"HTTP {resp.status_code}: {resp.text[:500]}",
            "duration": duration,
        }

    data = resp.json()
    return {
        "raw": data,
        "duration": duration,
    }


def extract_image(response_data: dict) -> tuple[str | None, str | None]:
    """Extract base64 image and text from OpenRouter response.
    Returns (image_b64_or_none, text_or_none)."""
    raw = response_data.get("raw", {})
    choices = raw.get("choices", [])
    if not choices:
        return None, None

    message = choices[0].get("message", {})

    # Text content
    text = message.get("content", "")

    image_b64 = None

    def extract_from_data_url(url: str) -> str | None:
        if url.startswith("data:"):
            return url.split(",", 1)[-1]
        return None

    # Format 1: message.images[] — OpenRouter's actual format
    # Structure: {"type": "image_url", "image_url": {"url": "data:image/png;base64,..."}}
    images = message.get("images", [])
    if not images:
        images = raw.get("images", [])

    for img_data in images:
        if image_b64:
            break
        if isinstance(img_data, dict):
            # Nested image_url format (observed from OpenRouter)
            if img_data.get("type") == "image_url":
                url = img_data.get("image_url", {}).get("url", "")
                image_b64 = extract_from_data_url(url)
            # Direct b64 fields
            if not image_b64:
                image_b64 = img_data.get("b64_json") or img_data.get("data")
            # Direct url field
            if not image_b64 and "url" in img_data:
                image_b64 = extract_from_data_url(img_data["url"])
        elif isinstance(img_data, str):
            image_b64 = extract_from_data_url(img_data) or img_data

    # Format 2: content as array of parts
    if not image_b64 and isinstance(message.get("content"), list):
        for part in message["content"]:
            if isinstance(part, dict):
                if part.get("type") == "image_url":
                    url = part.get("image_url", {}).get("url", "")
                    image_b64 = extract_from_data_url(url)
                elif part.get("type") == "image":
                    image_b64 = part.get("data") or part.get("b64_json")

    return image_b64, text


# ---------------------------------------------------------------------------
# Image processing
# ---------------------------------------------------------------------------

def save_and_resize(image_b64: str, name: str, resize: str | None = None) -> Path:
    """Decode base64, save PNG, optionally resize. Returns output path."""
    import io
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{name}-{timestamp}.png"
    filepath = OUTPUT_DIR / filename

    # Decode and open
    img_bytes = base64.b64decode(image_b64)
    img = Image.open(io.BytesIO(img_bytes))

    # Save original
    img.save(filepath, "PNG")
    print(f"  Saved: {filepath} ({img.size[0]}x{img.size[1]})")

    # Resize if requested
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
    parser = argparse.ArgumentParser(description="Generate images via Nano Banana / OpenRouter")
    parser.add_argument("prompt", help="Image generation prompt")
    parser.add_argument("--model", choices=["flash", "pro"], default="flash",
                        help="Model: flash (~$0.04) or pro (~$0.13)")
    parser.add_argument("--aspect", default="1:1",
                        help="Aspect ratio (1:1, 16:9, 9:16, 3:2, 2:3, 4:3, 3:4, etc.)")
    parser.add_argument("--name", default=None,
                        help="Output filename prefix (default: slugified prompt)")
    parser.add_argument("--resize", default=None,
                        help="Resize to WxH (e.g., 800x600)")
    parser.add_argument("--ref", action="append", default=None,
                        help="Reference image path(s) for character consistency (repeatable)")
    parser.add_argument("--system", default=None,
                        help="Optional system prompt for style/character consistency")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be sent without making the API call")
    args = parser.parse_args()

    name = args.name or slugify(args.prompt)
    model_info = MODELS[args.model]

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
            resize=args.resize or "", filename="", cost=0,
            duration=result["duration"], status=f"error: {result['error'][:100]}",
        )
        sys.exit(1)

    image_b64, text = extract_image(result)

    if not image_b64:
        print("ERROR: No image in response.")
        print("Response keys:", list(result.get("raw", {}).keys()))
        if result.get("raw"):
            print("Raw response (first 1000 chars):")
            print(json.dumps(result["raw"], indent=2)[:1000])
        log_generation(
            model=args.model, prompt=args.prompt, aspect=args.aspect,
            resize=args.resize or "", filename="", cost=0,
            duration=result["duration"], status="error: no image in response",
        )
        sys.exit(1)

    if text:
        print(f"  Model said: {text[:200]}")

    filepath = save_and_resize(image_b64, name, args.resize)

    cumulative = log_generation(
        model=args.model, prompt=args.prompt, aspect=args.aspect,
        resize=args.resize or "", filename=filepath.name,
        cost=model_info["cost_per_image"], duration=result["duration"],
        status="ok",
    )

    print()
    print(f"  Cost this image:  ${model_info['cost_per_image']:.3f}")
    print(f"  Cumulative spend: ${cumulative:.3f}")
    print("  Done!")


if __name__ == "__main__":
    main()
