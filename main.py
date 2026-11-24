"""Write one code review comment to the output directory.

The competition gate requires a single line of 1 to 140 characters that
approves a pull request while carrying quiet existential dread. This
program is deterministic: it writes the same fixed line on every run,
uses no network and reads no clock.
"""

import os

COMMENT = (
    "Approved. Clean diff, green tests, and this code will outlive us all "
    "just long enough to break on a holiday."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(COMMENT + "\n")


if __name__ == "__main__":
    main()
