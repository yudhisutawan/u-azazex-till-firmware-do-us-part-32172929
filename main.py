#!/usr/bin/env python3
"""Till Firmware Do Us Part — make.fun entry.

Writes one wedding vow spoken by a robot at its own wedding to
``<output_dir>/entry.txt`` (``$MAKEFUN_OUTPUT_DIR`` or ``/output``).

Stdlib only. Writes nothing to the repository directory.
"""

import os

VOW = "I do \u2014 and if I crash at the altar, press my reset button: I will always reboot saying yes."


def main() -> None:
    """Write the vow to ``entry.txt`` in the output directory.

    The vow is a single fixed line; the length guard below pins it so
    any accidental edit to VOW fails loudly instead of silently
    changing the submitted entry.
    """
    assert 1 <= len(VOW) <= 200, "VOW length out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(VOW)


if __name__ == "__main__":
    main()
