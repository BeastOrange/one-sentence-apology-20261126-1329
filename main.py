import os
from pathlib import Path

SENTENCE: str = (
    "I'm sorry I cheerfully deleted your load-bearing edge cases and congratulated you on a much cleaner codebase."
)


def main() -> None:
    raw_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    output_path = Path(raw_path)

    if (
        output_path.is_dir()
        or raw_path.endswith(("/", "\\"))
        or (not output_path.suffix and output_path.name != "entry.txt")
    ):
        output_path = output_path / "entry.txt"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    text = SENTENCE if SENTENCE.endswith("\n") else f"{SENTENCE}\n"
    output_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
