# Development log

Newest first. Each entry links to its journal file.

## 2026-11-15 (merges)

- Merged pcap-triage #4 allow-lists, #5 stealth/UDP scans; portfolio #4.
- Submitted SigmaHQ/sigma#6630 from fork `Hiresh2007/sigma`. Open, not
  yet reviewed; upstream CI awaits maintainer approval for a first-time contributor.

## 2026-11-15 ([journal](journal/2026-11-15.md))

- **pcap-triage PR #5 (stacked on #4):** NULL / FIN / Xmas and UDP scan detection,
  ICMP quoted-port parsing; 8 new tests (104 total), CI green.

## 2026-11-11 ([journal](journal/2026-11-11.md))

- **pcap-triage PR #4:** TOML allow-lists with mandatory reasons, strict
  validation and audited suppression; 19 new tests (96 total), CI green.

## 2026-11-10 ([journal](journal/2026-11-10.md))

- **Merges:** pcap-triage v0.2.0 on `main` (DNS + beaconing), portfolio
  sessions 2–4, profile build concurrency. Deleting a stacked PR's base branch
  closed pcap-triage #2; reopened as #3 after merging `main` into the branch
  (resolved trees verified identical to the reviewed branch).
- **Sigma setup:** local clone and sigma-cli; the full rule set validates with
  0 issues under CI's pinned validators (55 with the latest, all UUID v1 ids).
- **Contribution prepared:** DNS base64 rule `==.` -> `=.` to cover single
  padding; validated; draft PR in `contributions/`. Not submitted yet.

## 2026-11-09 ([journal](journal/2026-11-09.md))

- **pcap-triage PR #2 (stacked on #1):** beaconing detector (T1071) using
  median interval and MAD-based jitter per channel; CLI flags; demo beacon;
  20 new tests (77 total), CI green on 3.10–3.13.
- **Threshold evidence:** simulation of detection and false-positive rates
  recorded in `docs/DESIGN.md`.

## 2026-11-07 ([journal](journal/2026-11-07-2.md))

- **pcap-triage PR #1 (v0.2.0):** DNS tunnelling (T1071.004) and NXDOMAIN/DGA
  (T1568.002) detectors; reader DNS parsing with malformed-payload handling and
  escaping of control bytes; CLI flags; demo capture with 4 findings; 31 new
  tests (57 total), CI green on 3.10–3.13.
- **Threshold fix during development:** entropy 3.5 → 3.0 after finding that
  hex-encoded text averages ~3.2–3.35 bits/char; regression test added.
- **Profile PR #1:** workflow concurrency group to stop asset-build races.
- **Dashboard:** several journal files per day (`YYYY-MM-DD-N.md`), ordering
  bug found by the new test and fixed; 7 tests.

## 2026-11-07 ([journal](journal/2026-11-07.md))

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
- **Published:** both repos public; pcap-triage CI green on
  3.10–3.13; dashboard deployed to https://hiresh2007.github.io/security-engineering-portfolio/
