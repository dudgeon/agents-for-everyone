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

    print("=" * 70)
    print("IMAGE GENERATION COST SUMMARY")
    print("=" * 70)
    print(f"  Total images generated: {ok_count}")
    print(f"  Failed attempts:        {err_count}")
    print(f"  Flash images:           {flash_count}  (~${flash_count * 0.039:.2f})")
    print(f"  Pro images:             {pro_count}  (~${pro_count * 0.134:.2f})")
    print(f"  TOTAL SPEND:            ${total_cost:.3f}")
    print("=" * 70)

    if display_rows:
        print()
        print(f"{'Timestamp':<22} {'Model':<7} {'Cost':>7} {'Status':<8} {'Filename'}")
        print("-" * 70)
        for r in display_rows:
            ts = r.get("timestamp", "")[:19]
            model = r.get("model", "?")
            cost = r.get("cost_usd", "0")
            status = r.get("status", "?")[:8]
            fname = r.get("filename", "")[:30]
            print(f"{ts:<22} {model:<7} ${float(cost):>6.3f} {status:<8} {fname}")


if __name__ == "__main__":
    main()
