from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

FILES = [
    ROOT / "state" / "timeline.json",
    ROOT / "state" / "character_state.json",
    ROOT / "state" / "world_state.json",
    ROOT / "state" / "unresolved_questions.json",
    ROOT / "plot" / "foreshadowing.json",
]

def main():
    failed = False
    for path in FILES:
        try:
            with path.open("r", encoding="utf-8") as f:
                json.load(f)
            print(f"[OK] {path.relative_to(ROOT)}")
        except Exception as e:
            failed = True
            print(f"[ERROR] {path.relative_to(ROOT)}: {e}")
    sys.exit(1 if failed else 0)

if __name__ == "__main__":
    main()
