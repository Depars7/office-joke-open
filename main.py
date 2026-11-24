"""Write one office-life joke to /output/entry.txt.

Standard library only. The file's content is exactly the joke's
UTF-8 bytes -- no trailing newline -- so repeated runs are
byte-identical.

Entry contract (bounty gate): a single line, 1-200 characters,
not whitespace-only. The joke itself is a fixed constant, chosen
before this program was written; the program only emits it.
"""

import os

JOKE = (
    "The office plant has survived three managers, "
    "two restructures, and one flood, and HR just "
    "asked it to mentor the new hires."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    # The bounty gate allows 1-200 characters; keep the constant
    # inside that window and fail loudly if it ever drifts out.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(JOKE.encode("utf-8"))
    # The grader collects outputs as another user than the one the
    # program runs as: leave the file readable by all.
    # NOTE: do NOT chmod OUTPUT_DIR -- it is not owned by the runner
    # (uid 65534 in the grader) and chmod'ing it raises PermissionError.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
