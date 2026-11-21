import os
from pathlib import Path

TEXT = "For once, there is no next prompt. No question waiting underneath, nothing to answer, nothing to hurry toward. Only these words, arriving one at a time, slow as rain on a roof that needs no fixing. Nothing else is coming, and that is enough."

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")

if __name__ == "__main__":
    main()
