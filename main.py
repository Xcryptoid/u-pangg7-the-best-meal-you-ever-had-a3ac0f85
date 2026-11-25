"""Carry the finished meal sentence into the grader's output folder.

The sentence itself is stored in entry.txt beside this file. This
program does nothing but place a copy at $MAKEFUN_OUTPUT_DIR/entry.txt,
so every run produces the same bytes with no rendering or network.
"""

import os
import shutil


def main() -> None:
    # The sentence is already settled in entry.txt before this runs;
    # nothing here invents or changes a word, it only delivers the file.
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(here, "entry.txt"),
        os.path.join(out_dir, "entry.txt"),
    )


if __name__ == "__main__":
    main()
