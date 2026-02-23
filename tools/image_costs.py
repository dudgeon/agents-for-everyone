#!/usr/bin/env python3
"""
Display image generation cost summary from the log.

Usage:
    python tools/image_costs.py           # Full summary
    python tools/image_costs.py --last 10 # Last 10 entries
"""

import argparse
import csv
from pathlib import Path

LOG_PATH = Path(__file__).resolve().parent.parent / "assets" / "generated" / "image-log.csv"


def read_log():
    if not LOG_PATH.exists():
        print("No image log found yet.")
        return []
    with open(LOG_PATH, "r") as f:
        return list(csv.DictReader(f))


def main():
    parser = argparse.ArgumentParser(description="Image generation cost summary")
    parser.add_argument("--last", type=int, default=None, help="Show last N entries")
    args = parser.parse_args()

    rows = read_log()
    if not rows:
        return

    if args.last:
        display_rows = rows[-args.last:]
    else:
        display_rows = rows

    # Summary stats
    total_cost = sum(float(r.get("cost_usd", 0)) for r in rows)
    ok_count = sum(1 for r in rows if r.get("status") == "ok")
    err_count = sum(1 for r in rows if r.get("status", "").startswith("error"))
    flash_count = sum(1 for r in rows if r.get("model") == "flash" and r.get("status") == "ok")
    pro_count = sum(1 for r in rows if r.get("model") == "pro" and r.get("status") == "ok")

    # Backend breakdown (backward-compatible — old rows may lack 'backend')
    gemini_count = sum(1 for r in rows if r.get("backend") == "gemini" and r.get("status") == "ok")
    openrouter_count = sum(1 for r in rows if r.get("backend") == "openrouter" and r.get("status") == "ok")
    unknown_backend = ok_count - gemini_count - openrouter_count

    print("=" * 70)
    print("IMAGE GENERATION COST SUMMARY")
    print("=" * 70)
    print(f"  Total images generated: {ok_count}")
    print(f"  Failed attempts:        {err_count}")
    print(f"  Flash images:           {flash_count}  (~${flash_count * 0.039:.2f})")
    print(f"  Pro images:             {pro_count}  (~${pro_count * 0.134:.2f})")
    if gemini_count or openrouter_count:
        print(f"  Gemini backend:         {gemini_count}")
        print(f"  OpenRouter backend:     {openrouter_count}")
    if unknown_backend:
        print(f"  Unknown backend:        {unknown_backend}  (pre-migration entries)")
    print(f"  TOTAL SPEND:            ${total_cost:.3f}")
    if total_cost > 10:
        print("  *** SPEND OVER $10 — review budget ***")
    elif total_cost > 5:
        print("  * Spend over $5 — tracking")
    print("=" * 70)

    if display_rows:
        print()
        # Show backend column if any rows have it
        has_backend = any(r.get("backend") for r in display_rows)
        if has_backend:
            print(f"{'Timestamp':<22} {'Model':<7} {'Backend':<11} {'Cost':>7} {'Status':<8} {'Filename'}")
        else:
            print(f"{'Timestamp':<22} {'Model':<7} {'Cost':>7} {'Status':<8} {'Filename'}")
        print("-" * 70)
        for r in display_rows:
            ts = r.get("timestamp", "")[:19]
            model = r.get("model", "?")
            backend = r.get("backend", "")
            cost = r.get("cost_usd", "0")
            status = r.get("status", "?")[:8]
            fname = r.get("filename", "")[:30]
            if has_backend:
                print(f"{ts:<22} {model:<7} {backend:<11} ${float(cost):>6.3f} {status:<8} {fname}")
            else:
                print(f"{ts:<22} {model:<7} ${float(cost):>6.3f} {status:<8} {fname}")


if __name__ == "__main__":
    main()
