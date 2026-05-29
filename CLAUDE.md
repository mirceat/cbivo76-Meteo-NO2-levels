# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project does

Reads sensor log text files (CSV-formatted, one row per second) and produces a PNG line chart of NO2 level over time for each input file. There is one script: [src/Meteo.py](src/Meteo.py). A parallel Jupyter notebook [src/Meteo.ipynb](src/Meteo.ipynb) exists as the original source the `.py` was derived from — keep them in sync if behavior changes.

## Running the script

Dependencies:

```
pip install pandas matplotlib
```

Run from the `src/` directory (the script uses **relative paths** `../18_0904_0908` and `../18_0904_0908out`, so running it from the repo root will fail or write to the wrong place):

```
cd src
python Meteo.py
```

There are no tests, lint, or build steps.

## Input file format

Each `*.txt` is comma-separated with this header:

```
DateTime,NO2,NH3,CO,T,RH,P,DeviceID,NO2ppb
```

The script skips the header, then for each line splits on `,`, parses `Date` and `Time` from column 0 (space-separated), and reads `NO2` from column 1. Lines with fewer than 6 columns are silently skipped — this is intentional: it filters out truncated/garbage lines.

## Directory layout and conventions

- `18_0904_0908/` — cleaned input batch the script currently processes.
- `18_0904_0908out/` — PNG outputs (one per input `.txt`, same basename).
- `18_0904_0908v1/` — **originals** of the same batch. The raw files contained NUL bytes that broke parsing; bad rows were stripped out before being copied into `18_0904_0908/`. Do not overwrite `v1/` — it is the rescue copy. If you process a new batch and need to strip NULs, follow the same pattern (preserve originals in a `v1`-suffixed folder).
- `Gas_vers_scurta/` — an older, unprocessed batch (August 2025). The script does **not** read from here; if you need to process it, change `input_dir`/`output_dir` in `Meteo.py` or parameterize them.

The `input_dir` and `output_dir` constants at the top of `Meteo.py` are the only knobs — when asked to process a different batch, edit those two lines.

## Prompt log

`prompt-log.md` is a hand-maintained, reverse-chronological log of the prompts the user has issued in this repo (newest entry at the top, dated section headers). When the user gives you a substantive task, append a new entry at the top with the prompt text. Do not edit older entries.

## Notes

- Already-tracked IDE files (`.idea/`) remain in git history despite `.idea` being in `.gitignore`. To untrack without deleting on disk: `git rm -r --cached .idea` and commit.
