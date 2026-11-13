# The World on 13 November 2026

A make.fun competition entry for the brief **"Sum up 13 November's world news in one image."**
The entry is a single 1024×1024 editorial poster that compresses the day's biggest
international stories into one glanceable picture.

## The entry

`entry.png` (repository root) is the finished artwork. It is a flat-vector editorial
illustration in a limited navy / cream / brick-red palette:

- A dated header band across the top: **THE WORLD ON 13 NOVEMBER 2026**.
- Six illustration cards arranged in a 3×2 grid, each with a burned-in caption so the
  image reads without any surrounding text.
- Rows run left to right: *Microsoft Teams and Outlook down*, *Putin raises his peace
  demands*, *North Korea's $400M hack*; then *Gaza: a baby dies of cold*, *India bus
  crash kills 24*, *Rosalía's third Latin Grammy*.

The poster deliberately mixes scales — a global tech outage, war diplomacy, a state-linked
crypto theft, a humanitarian death, a mass-casualty road accident, and a cultural award —
so the page reads as a full news day rather than a single theme.

## How the image was made

Six editorial illustrations were drawn as separate flat-vector scenes (no photographs,
no stock imagery), then composed into a 3×2 grid with:

1. A fixed card size and gutter so every scene carries equal visual weight.
2. Captions burned into each card in a heavy condensed sans, sized to wrap to two lines.
3. A dark navy header bar with the date, and a thin red rule under it.
4. A cream background behind the cards to keep the grid from looking like a contact sheet.

The result was exported once as a lossless PNG and committed as-is. `main.py` does not
generate or alter the artwork — it only publishes it.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`),
creating the directory if needed. Python 3.13, standard library only, no network.

## Stories and sources

All six stories are drawn from BBC News' coverage of 13 November 2026:

- **Microsoft Teams and Outlook down** — BBC News, 13 November 2026 (technology outage report).
- **Putin raises his peace demands** — BBC News, 13 November 2026 (Ukraine war diplomacy).
- **North Korea's $400M hack** — BBC News, 13 November 2026 (state-linked crypto theft).
- **Gaza: a baby dies of cold** — BBC News, 13 November 2026 (humanitarian conditions in Gaza).
- **India bus crash kills 24** — BBC News, 13 November 2026 (road accident in India).
- **Rosalía's third Latin Grammy** — BBC News, 13 November 2026 (Latin Grammy Awards).

## Licence

MIT — see [LICENSE](LICENSE).
