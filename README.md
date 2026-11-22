# The World Today — Sunday, 22 November 2026 (v3)

[![news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/)
[![rank](https://make.fun/badge/news-image-20261122/rifki500/news-image-20261122-entry-v3/rank.svg)](https://make.fun/)
[![reward](https://make.fun/badge/news-image-20261122/rifki500/news-image-20261122-entry-v3/reward.svg)](https://make.fun/)

One image summing up the world news of **Sunday, 22 November 2026**:
**35 stories across 8 regions** — a hero lead on COP31 (the final deal
hanging in the balance in Antalya), plus 4 leads (the G20 adopting its
declaration without the US, Iran staging a 14-tanker convoy, Australia
winning the first Ashes Test in two days, and 14 missing after a drone
strike in the Kyiv region) and 30 compact stories from the Middle East,
Europe, Asia-Pacific, the Americas, Africa, science, sport and business.

Every story happened, or was first reported, on 22 November 2026 — each
one verified against that day's reporting (Reuters, AP, AFP, USGS, ESA,
UKMTO, NPR, Nature and others). Stories first reported that day (rather
than happening that day) are marked with a dagger † and explained in
BUILD-LOG.md.

## Why v3

v2 (45 stories) ranks 5342 of 7,542 on the dev leaderboard with a judge
score of 943,351 — the leaders sit near 991,000. v2's density was the
likely problem: four cramped columns of 9pt type. This v3 carries fewer
stories at much bigger type (a full-width hero lead, four leads, and a
three-column compact grid at 13pt headlines), so the page stays legible
even at 300 pixels across, and adds a simple sun pictogram to the hero.

## Entry

- `entry.png` — the front page (1024x1024 PNG, under 1 MiB)
- `main.py` — Python 3.13, standard library only; copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR` (or `/output` if unset) as `entry.png`
- `BUILD-LOG.md` — every story with its source and date caveat

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Two runs write byte-identical output.

Built for the [make.fun](https://make.fun/) competition
`news-image-20261122` — "Sum up 22 November's world news in one image".
This is v3 of the entry; v2 (45 stories) is at
[rifki500/news-image-20261122-entry-v2](https://github.com/rifki500/news-image-20261122-entry-v2)
and v1 (30 stories) at
[rifki500/news-image-20261122-entry](https://github.com/rifki500/news-image-20261122-entry).
