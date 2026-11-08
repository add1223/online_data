"""Contract rejection probe for lab02: a string token value must be rejected."""
import json
import sys
from pathlib import Path

COURSE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(COURSE_ROOT))

from coursekit.pipeline import validate_event

mode = sys.argv[1]
row = json.loads((COURSE_ROOT / "data/raw/events.jsonl").read_text(encoding="utf-8").splitlines()[0])
row["event_id"] = "contract-probe-" + mode
row["input_tokens"] = "100" if mode == "bad" else 100
reason = validate_event(row)
print("mode=", mode)
print("input_tokens=", repr(row["input_tokens"]))
print("validate_event=", reason)
if mode == "bad":
    print("CONTRACT_REJECTED", reason)
else:
    print("CONTRACT_RECOVERED", "accepted" if reason is None else reason)
