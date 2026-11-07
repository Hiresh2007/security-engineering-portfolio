import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location(
    "build_dashboard", ROOT / "scripts/build_dashboard.py"
)
bd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bd)


def test_front_matter():
    text = "---\ndate: 2026-11-07\nobjective: a: b\n---\n# body"
    assert bd.parse_front_matter(text) == {"date": "2026-11-07", "objective": "a: b"}
    assert bd.parse_front_matter("# no front matter") == {}
    assert bd.parse_front_matter("---\ndate: x\n") == {}  # unterminated


def test_roadmap_sections_phases_and_checkboxes():
    text = "# Roadmap\n\n## alpha\n\nPhase 1\n- [x] one\n- [ ] two\n\n## beta\n- [X] three\n"
    r = bd.parse_roadmap(text)
    assert r["alpha"] == [
        {"text": "one", "done": True, "phase": "Phase 1"},
        {"text": "two", "done": False, "phase": "Phase 1"},
    ]
    assert r["beta"] == [{"text": "three", "done": True, "phase": None}]


def test_markdown_table():
    text = "intro\n\n| A | B |\n|---|---|\n| 1 | 2 |\n| 3 | 4 |\n\nafter | not table"
    assert bd.parse_markdown_table(text) == [{"A": "1", "B": "2"}, {"A": "3", "B": "4"}]
    assert bd.parse_markdown_table("no table") == []
    assert bd.parse_markdown_table(text, after_heading="## Missing") == []


def test_discoveries_only_from_section():
    text = "## Other\n- 2026-01-01 — ignored\n## Discoveries\n- 2026-11-07 — found `x`\n- junk\n"
    assert bd.parse_discoveries(text) == [{"date": "2026-11-07", "text": "found `x`"}]


def test_testing_status_keeps_latest_per_project():
    sessions = [
        {"date": "2026-11-07", "project": "p", "tests_passed": "10", "tests_failed": "1"},
        {"date": "2026-11-08", "project": "p", "tests_passed": "12", "tests_failed": "0"},
        {"date": "2026-11-08", "project": "q"},
    ]
    (status,) = bd.testing_status(sessions)
    assert (status["date"], status["passed"], status["failed"]) == ("2026-11-08", 12, 0)


def test_build_offline_on_real_repo_files():
    data = bd.build(offline=True)
    json.dumps(data)
    assert data["overview"]["projects"] == len(data["projects"])
    assert all(s["date"] for s in data["sessions"])
    assert data["overview"]["concepts"] == len(data["learning"]) > 0
