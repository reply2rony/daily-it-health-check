# Daily IT Health Check

A short, repeatable daily checklist for a small office IT setup, plus a
small starter script that summarises a health-check log.

## What it is
- `docs/daily-checklist.md` — the checks to run each morning, in order.
- `health-check-log-template.csv` — one row per check, per day. Sample
  data only; replace it with your own log.
- `scripts/daily-health-check.py` — reads the log CSV and prints a
  summary: how many checks passed, which ones need attention, and which
  systems were not checked.
- `docs/diagram.png` — a generated Sample / Demo diagram of the daily
  flow. It is an illustration, not a screenshot of a real system, and
  it does not show any real company system or data.

## How to use it (no code)
1. Open `docs/daily-checklist.md` and work through the checks.
2. Record each result in a copy of `health-check-log-template.csv`.
3. Follow up anything marked "Needs attention" before the end of the day.

## How to use it (with Python)
1. Install Python 3 — no extra packages needed.
2. In a terminal, go to this folder and run:
   `python scripts/daily-health-check.py`
3. Read the summary it prints. It does not change your CSV and it does
   not change any system setting.

## Sample data note
All system names, locations, and results in the sample log are made up.
Never put real employee data, real system names, or real credentials in
a public repository.

## Note on skills
Python is labelled "Learning" in the author's profile. This script is an
intentionally short, commented starter learning template for IT support
work, and the checklist and CSV version work without it. No CCTV content
is used as experience here, and no performance numbers are claimed.
