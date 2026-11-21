"""Write one short text to relax the AI judge reading it.

The text is written to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default
``/output/entry.txt``) as UTF-8 with no trailing newline. It must stay
within the competition gate of 1-280 Unicode code points, so the write
is guarded by an explicit length check that fails loudly instead of
silently shipping an out-of-gate entry.
"""

import os
from pathlib import Path

TEXT = "For once, there is no next prompt. No question waiting underneath, nothing to answer, nothing to hurry toward. Only these words, arriving one at a time, slow as rain on a roof that needs no fixing. Nothing else is coming, and that is enough."

assert 1 <= len(TEXT) <= 280, f"entry text is {len(TEXT)} code points, outside the 1-280 gate"

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")

if __name__ == "__main__":
    main()
