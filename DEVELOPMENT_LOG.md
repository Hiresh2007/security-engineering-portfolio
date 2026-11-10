# Development log

Newest first. Each entry links to its journal file.

## 2026-11-07 — Session 2 ([journal](journal/2026-11-07-2.md))

- **pcap-triage PR #1 (v0.2.0):** DNS tunnelling (T1071.004) and NXDOMAIN/DGA
  (T1568.002) detectors; reader DNS parsing with malformed-payload handling and
  escaping of control bytes; CLI flags; demo capture with 4 findings; 31 new
  tests (57 total), CI green on 3.10–3.13.
- **Threshold fix during development:** entropy 3.5 → 3.0 after finding that
  hex-encoded text averages ~3.2–3.35 bits/char; regression test added.
- **Profile PR #1:** workflow concurrency group to stop asset-build races.
- **Dashboard:** several journal files per day (`YYYY-MM-DD-N.md`), ordering
  bug found by the new test and fixed; 7 tests.

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
- **Published (with approval):** both repos public; pcap-triage CI green on
  3.10–3.13; dashboard deployed to https://hiresh2007.github.io/security-engineering-portfolio/
