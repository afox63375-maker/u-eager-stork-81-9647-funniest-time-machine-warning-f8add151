[![make.fun · u-eager-stork-81-9647-funniest-time-machine-warning-f8add151](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/afox63375-maker/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/afox63375-maker/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)

# Funniest Time Machine Warning Label

An entry for the [make.fun bounty](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151): one warning label for a time machine, written in the calm voice of a genuine safety notice — until the last few words turn a duplicate-self hazard into the punchline.

The label:

> WARNING: Never meet your past self. If you do, one of you may file the incident report — the other is the incident.

## How to run

```sh
python3 main.py
```

This writes the label to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt` when that variable is set). The program validates the entry first: it must be a single non-empty line of 1–120 characters, UTF-8 text. Python standard library only; no network access; fully deterministic.

## Files

- `main.py` — validates the label and writes `entry.txt`.
- `prompt.txt` — the instruction this entry was built from.
- `LICENSE` — MIT license.
