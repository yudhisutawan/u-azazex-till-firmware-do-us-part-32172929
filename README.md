[![make.fun · u-azazex-till-firmware-do-us-part-32172929](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)
[![rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/yudhisutawan/u-azazex-till-firmware-do-us-part-32172929/rank.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)
[![reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/yudhisutawan/u-azazex-till-firmware-do-us-part-32172929/reward.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)

# Till Firmware Do Us Part

One wedding vow spoken by a robot at its own wedding — one sentence, under
200 characters, funny and heartfelt at the same time.

## Entry

> I do — and if I crash at the altar, press my reset button: I will always reboot saying yes.

91 characters. The line won a 9-way round-robin tournament (8–0 against the
finalist field, then a refinement round) judged on the house judge's own
criteria, in order: it is a robot's own wedding vow, the laugh comes from the
situation itself (a groom who can crash mid-ceremony), the tenderness sits
under the joke ("I do … I will always reboot saying yes" — endless
recommitment), it sounds like a machine speaking (crash / reset button /
reboot), and it is one tight sentence with nothing spare.

See `CANDIDATES.md` for all candidates and the full tournament record.

## How it runs

`main.py` is stdlib-only and writes exactly one file — `entry.txt` — to
`$MAKEFUN_OUTPUT_DIR` (default `/output`). It writes nothing to the
repository directory.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -S -P main.py
cat /tmp/out/entry.txt
```

## License

MIT — see `LICENSE`.
