---
name: image-costs
description: Show cumulative image generation spend from the cost log. Use when the user asks about image costs, budget, or spending.
---

Show the current image generation cost summary.

Run: `python3 tools/image_costs.py`

Display the results to the user. If the cumulative spend is over $5, flag it. If over $10, flag it prominently.
