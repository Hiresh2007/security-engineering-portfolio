"""Build dashboard/data.json from the tracking files and real git history.

Sources (nothing is typed in by hand):

* data/projects.json        project metadata and stack
* ROADMAP.md                [x] / [ ] items per ``## <project id>`` section
* journal/*.md              front matter of each session (date, tests, commits)
* LEARNING/PROGRESS.md      concept table
* RESEARCH.md               "## Discoveries" bullets
* git history               ``git log`` of each project's local clone; if a clone
                            is missing, the public GitHub commits API is used
                            (set GITHUB_TOKEN to raise the rate limit)

Usage:  python scripts/build_dashboard.py [--offline]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
GIT_FIELDS = "%H%x1f%h%x1f%aI%x1f%s"
MAX_COMMITS = 200


# --- parsers (pure functions, unit-tested) ---------------------------------


def parse_front_matter(text: str) -> dict[str, str]:
    """Parse a minimal ``---`` delimited ``key: value`` block at the top of a file."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    meta: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return meta
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip()
    return {}  # unterminated block


def parse_roadmap(text: str) -> dict[str, list[dict[str, Any]]]:
    """Map ``## <project id>`` -> list of {text, done, phase} checkbox items."""
    result: dict[str, list[dict[str, Any]]] = {}
    current: str | None = None
    phase: str | None = None
    for line in text.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            phase = None
            result[current] = []
            continue
        if current is None:
            continue
        m = re.match(r"^\s*- \[([ xX])\] (.+)$", line)
        if m:
            result[current].append(
                {"text": m.group(2).strip(), "done": m.group(1) != " ", "phase": phase}
            )
        elif line.strip() and not line.startswith(("#", "-", " ")):
            phase = line.strip()
    return result


def parse_markdown_table(text: str, after_heading: str | None = None) -> list[dict[str, str]]:
    """Return rows of the first pipe table (optionally the first after a heading)."""
    lines = text.splitlines()
    if after_heading:
        try:
            lines = lines[lines.index(after_heading) + 1 :]
        except ValueError:
            return []
    rows: list[list[str]] = []
    for line in lines:
        if line.lstrip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.append(cells)
        elif rows:
            break
    if len(rows) < 2:
        return []
    header, body = rows[0], [r for r in rows[2:]]  # rows[1] is the --- separator
    return [dict(zip(header, r, strict=False)) for r in body]


def parse_discoveries(text: str) -> list[dict[str, str]]:
    out = []
    in_section = False
    for line in text.splitlines():
        if line.startswith("## "):
            in_section = line.strip() == "## Discoveries"
            continue
        m = re.match(r"^- (\d{4}-\d{2}-\d{2}) [—-] (.+)$", line) if in_section else None
        if m:
            out.append({"date": m.group(1), "text": m.group(2).strip()})
    return out


def strip_md(text: str) -> str:
    """Remove the inline markdown the dashboard does not render (bold, code ticks)."""
    return re.sub(r"\*\*|`", "", text)


# --- git / GitHub ---------------------------------------------------------


def local_commits(path: Path) -> list[dict[str, str]] | None:
    git = shutil.which("git")
    if git is None or not (path / ".git").exists():
        return None
    proc = subprocess.run(  # noqa: S603 - fixed argv, no shell, path from our own config
        [git, "-C", str(path), "log", f"-n{MAX_COMMITS}", f"--pretty=format:{GIT_FIELDS}"],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:  # e.g. repository with no commits yet
        return []
    commits = []
    for line in proc.stdout.splitlines():
        sha, short, date, subject = line.split("\x1f", 3)
        commits.append({"sha": sha, "short": short, "date": date, "subject": subject})
    return commits


def github_commits(repo: str) -> list[dict[str, str]] | None:
    url = f"https://api.github.com/repos/{repo}/commits?per_page=100"
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})  # noqa: S310
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:  # noqa: S310 - fixed https host
            data = json.load(resp)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return None
    return [
        {
            "sha": c["sha"],
            "short": c["sha"][:7],
            "date": c["commit"]["author"]["date"],
            "subject": c["commit"]["message"].splitlines()[0],
        }
        for c in data
        if isinstance(c, dict) and "sha" in c
    ]


def collect_commits(project: dict[str, Any], offline: bool) -> tuple[list[dict], str]:
    local = local_commits((ROOT / project["local_path"]).resolve())
    if local is not None:
        return local, "local git"
    if offline or project.get("role") == "Open-source contribution":
        return [], "unavailable"
    remote = github_commits(project.get("fork") or project["repo"])
    return (remote, "GitHub API") if remote is not None else ([], "unavailable")


# --- assembly ---------------------------------------------------------------


def load_journal(journal_dir: Path) -> list[dict[str, Any]]:
    sessions = []
    for path in sorted(journal_dir.glob("????-??-??.md")):
        meta = parse_front_matter(path.read_text(encoding="utf-8"))
        if not meta:
            continue
        meta["file"] = f"journal/{path.name}"
        sessions.append(meta)
    return sessions


def testing_status(sessions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Latest recorded test run per project, taken from journal front matter."""
    latest: dict[str, dict[str, Any]] = {}
    for s in sessions:  # chronological, so later sessions overwrite earlier ones
        if "tests_passed" not in s:
            continue
        latest[s.get("project", "unknown")] = {
            "project": s.get("project", "unknown"),
            "date": s["date"],
            "passed": int(s.get("tests_passed", 0)),
            "failed": int(s.get("tests_failed", 0)),
            "lint": s.get("lint", "not run"),
            "ci": s.get("ci", "not run"),
        }
    return list(latest.values())


def build(offline: bool = False) -> dict[str, Any]:
    projects_cfg = json.loads((ROOT / "data/projects.json").read_text(encoding="utf-8"))
    roadmap = parse_roadmap((ROOT / "ROADMAP.md").read_text(encoding="utf-8"))
    sessions = load_journal(ROOT / "journal")
    learning = parse_markdown_table((ROOT / "LEARNING/PROGRESS.md").read_text(encoding="utf-8"))
    discoveries = parse_discoveries((ROOT / "RESEARCH.md").read_text(encoding="utf-8"))

    projects, all_commits, milestones, upcoming = [], [], [], []
    stack: dict[str, list[str]] = {}
    for p in projects_cfg["projects"]:
        commits, source = collect_commits(p, offline)
        items = roadmap.get(p["id"], [])
        done = [i for i in items if i["done"]]
        todo = [i for i in items if not i["done"]]
        projects.append(
            {
                **{k: p[k] for k in ("id", "name", "role", "summary", "repo", "stage", "areas")},
                "stack": p["stack"],
                "url": f"https://github.com/{p['repo']}",
                "commit_count": len(commits),
                "commit_source": source,
                "last_commit": commits[0]["date"] if commits else None,
                "roadmap_done": len(done),
                "roadmap_total": len(items),
            }
        )
        for c in commits:
            all_commits.append(
                {
                    **c,
                    "project": p["name"],
                    "url": f"https://github.com/{p['repo']}/commit/{c['sha']}",
                }
            )
        milestones += [{"project": p["name"], "text": strip_md(i["text"])} for i in done]
        upcoming += [{"project": p["name"], "text": strip_md(i["text"])} for i in todo[:3]]
        for tech in p["stack"]:
            stack.setdefault(tech, []).append(p["name"])

    all_commits.sort(key=lambda c: c["date"], reverse=True)
    per_day: dict[str, int] = {}
    for c in all_commits:
        day = c["date"][:10]
        per_day[day] = per_day.get(day, 0) + 1

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "owner": projects_cfg["owner"],
        "github_user": projects_cfg["github_user"],
        "overview": {
            "projects": len(projects),
            "sessions": len(sessions),
            "commits": len(all_commits),
            "concepts": len(learning),
            "milestones_done": len(milestones),
            "milestones_total": sum(p["roadmap_total"] for p in projects),
        },
        "projects": projects,
        "sessions": [
            {k: s.get(k) for k in ("date", "project", "objective", "file")} for s in sessions
        ][::-1],
        "commits_per_day": [{"date": d, "count": n} for d, n in sorted(per_day.items())],
        "recent_commits": all_commits[:12],
        "learning": [
            {
                "concept": strip_md(r.get("Concept", "")),
                "area": r.get("Area", ""),
                "introduced": r.get("Introduced", ""),
                "status": r.get("Status", ""),
            }
            for r in learning
        ],
        "stack": [{"name": k, "projects": v} for k, v in sorted(stack.items())],
        "milestones": milestones,
        "upcoming": upcoming,
        "discoveries": [{**d, "text": strip_md(d["text"])} for d in discoveries][::-1],
        "testing": testing_status(sessions),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--offline", action="store_true", help="never call the GitHub API")
    parser.add_argument("--out", type=Path, default=ROOT / "dashboard/data.json")
    args = parser.parse_args()
    data = build(offline=args.offline)
    args.out.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    o = data["overview"]
    print(
        f"wrote {args.out.relative_to(ROOT)}: {o['projects']} projects, {o['sessions']} sessions, "
        f"{o['commits']} commits, {o['concepts']} concepts"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
