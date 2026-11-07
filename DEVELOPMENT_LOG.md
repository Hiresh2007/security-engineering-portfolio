# Development log

Newest first. Each entry links to its journal file.

## 2026-11-07 — Session 1 ([journal](journal/2026-11-07.md))

- **Audit:** 47 public repos via the GitHub API; no security engineering code yet.
- **Research:** evaluated 12 security repos for maintenance, licence and
  contribution path. Selected pcap-triage (new), SigmaHQ/sigma, Cybersecurity-Journey.
- **pcap-triage `0ca2501`:** streaming pcap/pcapng reader, directional flow
  summary, vertical + horizontal TCP SYN scan detection (T1046) with
  sliding-window counting and open-port evidence, text/JSON CLI, 26 tests,
  ruff (incl. bandit rules), GitHub Actions matrix 3.10–3.13, design doc.
- **Portfolio:** tracking files, dashboard (`dashboard/index.html`), data
  builder `scripts/build_dashboard.py` (6 tests), Pages workflow.
- **Tests:** pcap-triage 26/26 passed; portfolio 6/6 passed; ruff clean in both.
  CI not run: repos not yet on GitHub.
- **Blocked:** push / PR / Pages, because `gh` is not authenticated and public repo
  creation needs approval.
