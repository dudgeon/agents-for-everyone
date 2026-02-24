#!/usr/bin/env python3
"""
Single-session story image generator.

Generates all 18 comic frames (9 chapters × 2 frames) for draft-005
in ONE continuous Gemini chat session. This preserves visual memory
of every character across all chapters, eliminating inter-chapter drift.

Usage:
    python3 tools/generate_story.py                     # all 9 chapters
    python3 tools/generate_story.py ch03 ch05 ch09     # specific chapters

Output: assets/generated/<id>-frame-[ab]-<timestamp>.png
Cost: ~$2.41 (18 × $0.134 pro model)
"""

import base64
import csv
import io
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CHARS_DIR = PROJECT_ROOT / "assets" / "characters"
OUTPUT_DIR = PROJECT_ROOT / "assets" / "generated"
LOG_PATH = OUTPUT_DIR / "image-log.csv"

DOTENV_PATH = PROJECT_ROOT / ".env"

MODEL_ID = "gemini-3-pro-image-preview"
COST_PER_IMAGE = 0.134

LOG_COLUMNS = [
    "timestamp", "model", "backend", "comic_id", "frame", "prompt",
    "aspect_ratio", "filename", "cost_usd", "cumulative_usd",
    "duration_sec", "status",
]


# ---------------------------------------------------------------------------
# Style + character bibles
# ---------------------------------------------------------------------------

STYLE_BLOCK = """Art style: Studio Ghibli-inspired illustration. Warm, painterly, hand-drawn feel with detailed backgrounds. Clean character linework with expressive faces. Soft natural lighting — diffused, golden-hour warmth. Watercolor-adjacent color washes, not cel-shaded. Rich environmental storytelling in every frame.

Setting palette: Modern open-plan office with abundant living plants — hanging pothos, large fiddle-leaf figs, terracotta pots on window ledges. Natural wood furniture, warm ambient light from large windows. Slightly solarpunk in atmosphere: the space feels cared for and organic, not sterile or corporate. Wooden desks, fabric chairs in muted earth tones, bookshelves with real books.

Color palette: Warm ochres, sage greens, terracotta, soft blues. Nothing neon, nothing primary. Shadows are warm, not grey. Highlights are golden.

Linework: Consistent medium-weight lines, slightly hand-drawn quality. Not vector-perfect.

Mood: Earnest, lived-in, warm."""

MAVEN_BIBLE = """MAVEN
IMMUTABLE TRAITS: Warm medium-brown skin (NOT light, NOT dark). Black hair, shoulder-length (NOT short, NOT long), usually tucked behind one ear (NOT ponytail, NOT loose on both sides). Dark brown eyes. Round wire-frame glasses (NOT rectangular, NOT thick-framed, NOT cat-eye). Slight build, average height. Resting expression: attentive and slightly amused.
DEFAULT OUTFIT: Sage-green button-up shirt, high-waisted charcoal trousers, simple gold stud earrings.
CONSTRAINTS: Do not change face, facial features, skin tone, body shape, or identity."""

DECLAN_BIBLE = """DECLAN
IMMUTABLE TRAITS: Light olive skin (NOT pale, NOT tan). Dark brown hair, short, slightly unkempt — not messy, just not trying (NOT styled, NOT slicked, NOT long). Hazel eyes. No glasses (NEVER add glasses). Medium build, slightly taller than Maven. Resting expression: thoughtful, guarded, arms often crossed or hands in pockets.
DEFAULT OUTFIT: Plain navy crew-neck sweater, dark jeans, simple sneakers.
CONSTRAINTS: Do not change face, facial features, skin tone, body shape, or identity."""

EMERY_BIBLE = """EMERY
IMMUTABLE TRAITS: Warm golden-brown skin (NOT light, NOT dark brown). Dark brown hair in a short undercut — buzzed on sides with longer wavy texture on top (NOT fully short, NOT long hair, NOT buzz cut all over). Brown eyes. No glasses (NEVER add glasses). Lean build, average height (between Maven and Declan). Resting expression: attentive, open, slightly curious. Nonbinary presentation — androgynous but natural.
DEFAULT OUTFIT: Fitted heather-gray crewneck tee under an open muted-teal cardigan with small lightning bolt logo on left chest. Dark chinos, clean white sneakers. Carries a plain digital tablet (dark case). Stylus tucked behind right ear — always present.
CONSTRAINTS: Do not change face, facial features, skin tone, body shape, or identity. The tablet, stylus-behind-ear, and lightning bolt logo are identity markers — always include them."""

CLAWD_BIBLE = """CLAW'D
IMMUTABLE TRAITS: Small (knee-height), BOXY (NOT rounded, NOT egg-shaped, NOT spherical) terracotta/coral-orange body with soft rounded corners. Wider than tall — like a slightly squished box. Four short STUBBY legs (NOT long, NOT thin, NOT wheels). Two small dark SQUARE eyes set close together — simple and minimal, like pixel art (NOT large, NOT round, NOT anime-style). No mouth (NEVER add a mouth). Small leaf-shaped sprout on top of its head (NOT a flower, NOT antennae). Friendly, curious, non-threatening.
DEFAULT: Carries a small leather-bound notebook and tiny pencil. No clothing — the terracotta body IS the character.
CONSTRAINTS: Do not change body shape, proportions, eye style, or color palette. The sprout, notebook, and stubby legs are identity markers — always include them."""

ALL_BIBLES = {
    "maven": MAVEN_BIBLE,
    "declan": DECLAN_BIBLE,
    "emery": EMERY_BIBLE,
    "clawd": CLAWD_BIBLE,
}

# Character ref images — new in-style refs take priority; fall back to old refs
def _find_ref(character: str, suffixes: list[str]) -> list[Path]:
    """Return ref paths for a character, preferring new refs."""
    found = []
    for suffix in suffixes:
        p = CHARS_DIR / f"{character}-{suffix}.png"
        if p.exists():
            found.append(p)
    return found

NEW_REF_CANDIDATES = {
    "maven": ["ref-new", "ref-sheet", "ref-face", "ref-34"],
    "declan": ["ref-new", "ref-sheet", "ref-face", "ref-34"],
    "emery": ["ref-new", "ref-sheet", "ref-face", "ref-34"],
    "clawd": ["ref-new", "ref-sheet", "ref-34"],
}


def get_refs(characters: list[str]) -> list[Path]:
    """Collect ref image paths for a set of characters.
    Uses new ref if available; falls back to existing refs (capped at 2 per char)."""
    refs = []
    for char in characters:
        candidates = NEW_REF_CANDIDATES.get(char, [])
        found = _find_ref(char, candidates)

        if found and "ref-new" in found[0].stem:
            # New in-style ref exists — use only it
            refs.append(found[0])
        else:
            # Fall back to legacy refs (cap at 2 to avoid style noise)
            refs.extend(found[:2])
    return refs


# ---------------------------------------------------------------------------
# Chapter definitions (from draft-005 COMIC specs)
# ---------------------------------------------------------------------------

CHAPTERS = [
    {
        "id": "ch01-the-box",
        "characters": ["maven", "declan"],
        "setting": (
            'Modern open-plan office kitchen/lounge. A communal table with laptops and coffee mugs. '
            'Warm pendant lights overhead. Maven has just set a sleek white box on the table — '
            'labeled "Agents" in clean sans-serif type. The front panel has a printed mascot illustration: '
            'a small boxy square-shaped terracotta/coral-orange ROBOT character with dark square pixel-art eyes, '
            'a tiny leaf sprout on top of its head, and four short stubby legs — like a product logo character on packaging. '
            'NOT a plant, NOT a flower — a small boxy robot mascot. '
            'Declan sits across from Maven, coffee mug in hand.'
        ),
        "frame_a": (
            'Maven holds the box up with both hands, presenting it to Declan. '
            'The front of the box faces forward — "Agents" label and the boxy robot mascot visible. '
            'Her expression barely contains excitement. '
            'Declan leans back in his chair, arms loosely crossed, coffee mug resting on the table — unimpressed. '
            'Expression Maven: excited, barely-contained energy. Expression Declan: unimpressed, bracing himself.'
        ),
        "frame_b": (
            'Maven has set the box on the table, lid still closed. '
            'The boxy terracotta robot mascot illustration is clearly printed on the box front panel. '
            'Declan gestures dismissively with his coffee mug hand toward the box. '
            'Maven shifts to amused determination. '
            'Expression Maven: determined, amused. Expression Declan: dry, eyebrow raised.'
        ),
    },
    {
        "id": "ch02-emery-enters",
        "characters": ["maven", "declan", "emery"],
        "setting": (
            'Same office kitchen/lounge. The "Agents" box sits on the table, lid closed, boxy robot mascot visible on the front panel. '
            'Maven stands beside the table. Declan still seated with his coffee mug. '
            'Emery has just walked in — tablet tucked under one arm, stylus behind their right ear, '
            'open muted-teal cardigan with small lightning bolt logo on left chest over heather-gray tee, dark chinos, clean white sneakers.'
        ),
        "frame_a": (
            'Emery pulls out a chair and sits, placing their tablet flat on the table. '
            'Maven turns toward them with a warm welcoming gesture. '
            'Declan watches with mild interest, coffee mug in hand. '
            'Expression Maven: welcoming, gesturing toward empty chair. '
            'Expression Emery: curious, glancing at the box on the table. '
            'Expression Declan: neutral, observing.'
        ),
        "frame_b": (
            'Emery shrugs casually, one hand resting on their tablet. Comfortable, not defensive. '
            'Declan has leaned slightly forward despite himself. Maven listens, waiting. '
            'Expression Emery: self-aware, slightly amused. '
            'Expression Declan: leaning forward, interested despite himself. '
            'Expression Maven: attentive, listening.'
        ),
    },
    {
        "id": "ch03-the-unboxing",
        "characters": ["maven", "declan", "emery", "clawd"],
        "setting": (
            'Same office kitchen/lounge. The "Agents" box is fully open on the table, lid folded back. '
            'Claw\'d — a small, boxy terracotta creature with dark square pixel-art eyes, '
            'a tiny leaf sprout on its head, and four stubby legs — sits beside the open box, '
            'leather-bound notebook open, tiny pencil in hand, eyes looking up at the humans. '
            'Maven stands beside the box. Emery leans forward in their chair, tablet flat on table. '
            'Declan watches from across the table, coffee cup frozen halfway to his mouth.'
        ),
        "frame_a": (
            'Maven gestures toward Claw\'d sitting beside the open box — Claw\'d\'s notebook is open to a fresh page, pencil raised. '
            'Emery stares with wide eyes. Declan has stopped mid-sip, coffee cup frozen in the air. '
            'Expression Maven: proud, presenting. Expression Emery: delighted, eyes wide. Expression Declan: caught off guard, frozen mid-sip.'
        ),
        "frame_b": (
            'Claw\'d has moved to the center of the table, notebook still open. '
            'Emery reaches a hand toward Claw\'d instinctively, leaning in with curiosity. '
            'Maven gestures warmly. Declan watches Claw\'d with skeptical attention. '
            'Expression Maven: warm, gesturing at Claw\'d. '
            'Expression Emery: reaching out, curious and delighted. '
            'Expression Declan: skeptical, but watching Claw\'d intently.'
        ),
    },
    {
        "id": "ch04-files-context",
        "characters": ["maven", "emery", "declan", "clawd"],
        "setting": (
            'Same office area. Someone has pulled up a laptop screen showing a file explorer with folders: '
            'docs/, specs/, research/, decisions/ — each with a trailing slash visible in the path labels. '
            'A CLAUDE.md file is visible at the root level. '
            'Claw\'d sits on the table next to the laptop, notebook open, actively scribbling. '
            'Maven points at the screen. Emery leans in close, their tablet propped beside the laptop. '
            'Declan stands slightly behind them, watching.'
        ),
        "frame_a": (
            'Maven points at the CLAUDE.md file in the file explorer on the laptop screen. '
            'Claw\'d flips through its notebook, mirroring the file browsing. '
            'Emery leans forward with both hands on the table, stylus still tucked behind their right ear, completely absorbed. '
            'Expression Maven: explaining, pointing at screen. '
            'Expression Emery: leaning in, aha moment starting to dawn. '
            'Expression Declan: watching from behind, arms still crossed but standing closer.'
        ),
        "frame_b": (
            'Emery looks down at their tablet (showing their own prompts.txt on the screen), then back at the laptop, making a connection. '
            'Emery pulls the stylus from behind their ear, ready to take a note. '
            'Expression Emery: excited, lightbulb moment. Expression Maven: pleased, watching Emery make the connection.'
        ),
    },
    {
        "id": "ch05-rules-skills",
        "characters": ["maven", "emery", "clawd"],
        "setting": (
            'Closer angle on the same table. Claw\'d sits between Maven and Emery, notebook open to a page with a neat checklist. '
            'Maven has pulled up a text file on the laptop showing structured markdown — '
            'a skill definition with visible if/then conditional lines and a broader \'think like\' instruction below it. '
            'Emery has pulled the stylus from behind their right ear and is taking notes on their tablet. '
            'Declan is visible in the background, chair pushed back slightly, listening but not participating.'
        ),
        "frame_a": (
            'Maven points at the if/then section of the skill file on screen. '
            'Claw\'d looks up from its notebook, pencil poised mid-stroke. '
            'Emery sketches rapidly on their tablet, stylus moving. '
            'Expression Maven: teaching, animated. Expression Emery: focused, taking notes.'
        ),
        "frame_b": (
            'Emery looks up from their tablet, stylus hovering, connecting what Maven said to something they already do. '
            'Expression Emery: excited, something clicking. Expression Maven: nodding, affirming.'
        ),
    },
    {
        "id": "ch06-tools-actions",
        "characters": ["maven", "emery", "clawd"],
        "setting": (
            'The laptop screen now shows a terminal/command output with a list of completed actions: '
            '"Searched 4 databases... Updated Jira ticket... Created summary.md..." '
            'Claw\'d sits near the laptop, its open notebook page completely filled with small checkmarks. '
            'Maven leans against the table, relaxed, arms at her sides. '
            'Emery is on the edge of their seat, leaning toward the screen. '
            'Declan is visible in the background, having moved his chair noticeably closer to the group.'
        ),
        "frame_a": (
            'Maven gestures at the terminal output on the screen, palm open. '
            'Claw\'d\'s notebook is full of checkmarks — it holds up the page briefly. '
            'Emery reads the output, mouth slightly open. '
            'Expression Maven: matter-of-fact, letting the output speak. Expression Emery: impressed, reading the screen intently.'
        ),
        "frame_b": (
            'Emery turns away from the screen to look directly at Maven. Something has shifted in how they\'re thinking about this. '
            'Expression Emery: recalibrating, serious. Expression Maven: steady, letting it land.'
        ),
    },
    {
        "id": "ch07-pm-lifecycle",
        "characters": ["maven", "emery", "clawd"],
        "setting": (
            'The table now has multiple items spread across it — the laptop showing a discovery research summary on screen, '
            'Emery\'s tablet flat on the table with a rough workflow diagram sketched on it, printed pages of a feature spec. '
            'Claw\'d moves between the items like a tiny project manager, notebook open. '
            'Maven and Emery are deep in conversation. '
            'Declan is in the background, chair turned toward them, listening with an expression more thoughtful than dismissive.'
        ),
        "frame_a": (
            'Maven counts on her fingers as she lists use cases. '
            'Claw\'d follows along, flipping to a new notebook page with each item. '
            'Emery\'s stylus moves quickly across their tablet, sketching a workflow diagram. '
            'Expression Maven: animated, ticking off examples on her fingers. Expression Emery: engaged, sketching rapidly.'
        ),
        "frame_b": (
            'Emery stops sketching and looks up, stylus frozen mid-stroke, connecting what Maven described to their own Tuesday afternoon. '
            'Expression Emery: recognizing their own workflow, excited. Expression Maven: watching Emery connect the dots, patient.'
        ),
    },
    {
        "id": "ch08-agentic-teams",
        "characters": ["maven", "emery", "declan", "clawd"],
        "setting": (
            'Maven has drawn a diagram on a whiteboard: a horizontal flow '
            '"PM intent → Structured context → Agent → Code/Output → Review". '
            'Below it, a second line with an upward arrow: "Agent → PM intent (faster)". '
            'Claw\'d sits near the whiteboard base. Emery and Declan are both facing the whiteboard from the table.'
        ),
        "frame_a": (
            'Maven taps the left side of the diagram — "PM intent → Structured context" — with her finger. '
            'Both Emery and Declan look at the whiteboard. Declan\'s arms are uncrossed for the first time, hanging at his sides. '
            'Expression Maven: serious, making the key point. '
            'Expression Emery: focused, thinking about implications. '
            'Expression Declan: arms uncrossed, brow furrowed in thought.'
        ),
        "frame_b": (
            'Declan speaks up — not objecting, but working through a real problem. He leans forward, elbows on his knees. '
            'Maven nods, inviting him to continue. '
            'Expression Declan: engaged, working through an idea. Expression Maven: nodding, inviting him in.'
        ),
    },
    {
        "id": "ch09-getting-started",
        "characters": ["maven", "emery", "clawd"],
        "setting": (
            'The office kitchen is quieter now. The white "Agents" box sits empty and open on the table, '
            'lid folded back, the boxy terracotta robot mascot illustration visible on the inside of the lid. '
            'Claw\'d sits at the table\'s edge, notebook full of notes from the entire conversation, '
            'tiny pencil resting on top. '
            'Maven and Emery sit across from each other, tablets and laptops set aside, talking directly. '
            'Declan\'s chair is empty — he left at some point. Warm late-afternoon light through the windows.'
        ),
        "frame_a": (
            'Emery has their tablet in hand, finger moving across the screen as they make a list. '
            'Maven sits back in her chair, relaxed, letting Emery lead the conversation now. '
            'Claw\'d watches them both, attentive. '
            'Expression Maven: relaxed, supportive. Expression Emery: determined, making a plan.'
        ),
        "frame_b": (
            'Claw\'d hops closer to Emery along the table and holds up its notebook — '
            'the page shows neat notes from the entire conversation, organized into five clear steps. '
            'Emery looks at Claw\'d and smiles. '
            'Expression Emery: warm, looking at Claw\'d. Expression Maven: pleased, watching the connection form.'
        ),
    },
]


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def load_env():
    if DOTENV_PATH.exists():
        for line in DOTENV_PATH.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                os.environ.setdefault(key.strip(), val.strip())


def get_gemini_key() -> str:
    load_env()
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        print("ERROR: GEMINI_API_KEY not found in .env")
        sys.exit(1)
    return key


def ensure_log():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    if not LOG_PATH.exists():
        with open(LOG_PATH, "w", newline="") as f:
            csv.writer(f).writerow(LOG_COLUMNS)


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


def log_frame(comic_id: str, frame: str, prompt: str, filename: str,
              duration: float, status: str):
    cost = COST_PER_IMAGE
    cumulative = get_cumulative_cost() + cost
    with open(LOG_PATH, "a", newline="") as f:
        csv.writer(f).writerow([
            datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "pro", "gemini", comic_id, frame,
            prompt[:200], "16:9", filename,
            f"{cost:.4f}", f"{cumulative:.4f}", f"{duration:.1f}", status,
        ])


def save_image(image_b64: str, name: str) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    filepath = OUTPUT_DIR / f"{name}.png"
    img_bytes = base64.b64decode(image_b64)
    img = Image.open(io.BytesIO(img_bytes))
    img.save(filepath, "PNG")
    return filepath


def extract_image(response) -> Optional[str]:
    for part in response.parts:
        if part.inline_data is not None:
            raw = part.inline_data.data
            pil_img = Image.open(io.BytesIO(raw))
            buf = io.BytesIO()
            pil_img.save(buf, "PNG")
            return base64.b64encode(buf.getvalue()).decode()
    return None


# ---------------------------------------------------------------------------
# Single-session story generator
# ---------------------------------------------------------------------------

def generate_story(chapters_to_run: list[dict]) -> list[str]:
    """
    Generate all frames for a list of chapters in a SINGLE Gemini chat session.
    Returns a list of chapter IDs that failed.
    """
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=get_gemini_key())
    ensure_log()

    # --- Collect ALL unique character refs across the full story ---
    all_chars = set()
    for ch in chapters_to_run:
        all_chars.update(ch["characters"])

    all_refs = get_refs(sorted(all_chars))
    print(f"\nCharacter refs loaded: {len(all_refs)}")
    for r in all_refs:
        print(f"  {r.name}")

    # --- Create config ---
    config = types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],
        image_config=types.ImageConfig(aspect_ratio="16:9"),
        system_instruction=(
            f"{STYLE_BLOCK}\n\n"
            + "\n\n".join(ALL_BIBLES[c] for c in sorted(all_chars))
            + "\n\nCONSTRAINTS: Do not change any character's face, facial features, "
            "skin tone, body shape, or identity across ANY frame in this session. "
            "Every frame is part of a continuous story — maintain perfect visual consistency throughout."
        ),
    )

    # --- Create ONE chat session for the entire story ---
    chat = client.chats.create(model=MODEL_ID, config=config)

    # --- Warmup: prime ALL character refs once ---
    print(f"\n[Warmup] Priming {len(all_refs)} character ref(s) for the entire session...")
    warmup_contents = []
    for ref_path in all_refs:
        warmup_contents.append(Image.open(ref_path))
        name = ref_path.stem.replace("-ref-new", "").replace("-ref-sheet", "").replace("-ref-", " ").replace("-", " ").title()
        warmup_contents.append(f"Reference: {name}")
    warmup_contents.append(
        "Study all of these character references carefully. "
        "You will draw these characters consistently across 9 chapters and 18 frames. "
        "Do not generate an image yet — acknowledge that you have memorized all visual references."
    )

    try:
        chat.send_message(warmup_contents)
        print("[Warmup] Complete.")
    except Exception as e:
        print(f"[Warmup] Warning: warmup failed ({e}). Continuing without warmup.")

    # --- Generate each chapter in the same session ---
    failed = []
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    for i, chapter in enumerate(chapters_to_run):
        comic_id = chapter["id"]
        chars = chapter["characters"]
        char_block = "\n\n".join(ALL_BIBLES[c] for c in chars)

        frozen_preamble = (
            f"SETTING (identical in both frames): {chapter['setting']}\n\n"
            f"Characters in this scene: {', '.join(chars)}\n\n"
            f"{char_block}\n\n"
            "CONSTRAINTS: Maintain all character appearances exactly as established. "
            "Same art style, same color palette, same lighting. "
            "This is a continuous story — consistency with all previous frames is required."
        )

        print(f"\n{'='*60}")
        print(f"Chapter {i+1}/{len(chapters_to_run)}: {comic_id}")
        print(f"Characters: {', '.join(chars)}")
        print(f"{'='*60}")

        # --- Chapter transition ---
        try:
            chat.send_message(
                f"Now generating Chapter {i+1}: {comic_id}. "
                f"This scene features: {', '.join(chars)}. "
                "Maintain all character appearances exactly as you have drawn them in previous frames."
            )
        except Exception as e:
            print(f"  [Transition] Warning: {e}")

        # --- Frame A ---
        frame_a_prompt = (
            f"{frozen_preamble}\n\n"
            f"FRAME A of 2 for chapter {comic_id}:\n{chapter['frame_a']}\n\n"
            "Generate Frame A as a clean illustration panel. No speech bubbles or text overlay."
        )

        print("  [Frame A] Generating...")
        start = time.time()
        try:
            resp_a = chat.send_message(frame_a_prompt)
            dur_a = time.time() - start
            img_a = extract_image(resp_a)
        except Exception as e:
            dur_a = time.time() - start
            print(f"  [Frame A] ERROR: {e}")
            failed.append(comic_id)
            continue

        if not img_a:
            print("  [Frame A] ERROR: no image in response")
            failed.append(comic_id)
            continue

        name_a = f"{comic_id}-frame-a-{timestamp}"
        path_a = save_image(img_a, name_a)
        print(f"  [Frame A] Saved: {path_a.name}")
        log_frame(comic_id, "a", frame_a_prompt, path_a.name, dur_a, "ok")

        # --- Frame B ---
        frame_b_prompt = (
            f"Now generate Frame B of 2 for chapter {comic_id}.\n"
            "Use the SAME characters with IDENTICAL appearance, clothing, and art style as Frame A.\n\n"
            f"FRAME B: {chapter['frame_b']}\n\n"
            "Generate Frame B as a clean illustration panel. No speech bubbles or text overlay."
        )

        print("  [Frame B] Generating...")
        start = time.time()
        try:
            resp_b = chat.send_message(frame_b_prompt)
            dur_b = time.time() - start
            img_b = extract_image(resp_b)
        except Exception as e:
            dur_b = time.time() - start
            print(f"  [Frame B] ERROR: {e}")
            # Frame A succeeded, don't mark whole chapter as failed
            continue

        if not img_b:
            print("  [Frame B] ERROR: no image in response")
            continue

        name_b = f"{comic_id}-frame-b-{timestamp}"
        path_b = save_image(img_b, name_b)
        print(f"  [Frame B] Saved: {path_b.name}")
        log_frame(comic_id, "b", frame_b_prompt, path_b.name, dur_b, "ok")

    return failed


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    chapters_to_run = CHAPTERS
    if len(sys.argv) > 1:
        ids = set(sys.argv[1:])
        chapters_to_run = [c for c in CHAPTERS if c["id"] in ids]
        if not chapters_to_run:
            print(f"No matching chapters: {sys.argv[1:]}")
            sys.exit(1)

    n = len(chapters_to_run)
    cost_estimate = n * 2 * COST_PER_IMAGE
    print(f"Single-session story generator")
    print(f"Chapters: {n}  |  Frames: {n * 2}  |  Estimated cost: ~${cost_estimate:.2f}")
    print(f"Model: {MODEL_ID}")

    # Check refs
    all_chars = set()
    for ch in chapters_to_run:
        all_chars.update(ch["characters"])
    refs = get_refs(sorted(all_chars))
    new_refs = [r for r in refs if "ref-new" in r.stem]
    old_refs = [r for r in refs if "ref-new" not in r.stem]
    if new_refs:
        print(f"Using {len(new_refs)} new in-style ref(s) + {len(old_refs)} legacy ref(s)")
    else:
        print(f"WARNING: No new-style refs found. Using {len(old_refs)} legacy refs.")
        print("Run tools/gen_refs.py first for best results.")

    print()
    failed = generate_story(chapters_to_run)

    print(f"\n{'='*60}")
    print(f"Done. {n - len(failed)}/{n} chapters succeeded.")
    if failed:
        print(f"Failed chapters: {failed}")
    print(f"Cumulative spend: ${get_cumulative_cost():.3f}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
