# Project state

_Last updated: 2026-11-11 (session 5)_

## Selected projects

| Project | Role | Stage | Repo |
|---|---|---|---|
| pcap-triage | Flagship (original) | v0.2.0 on `main`: port scans, DNS tunnelling, DGA, beaconing (77 tests) | [GitHub](https://github.com/Hiresh2007/pcap-triage), CI green |
| SigmaHQ/sigma | Open-source contribution | First change prepared locally (DNS base64 rule); fork not created | local clone `../sigma` |
| Cybersecurity-Journey | Supporting (Hiresh's notes) | Days 1–5 | [GitHub](https://github.com/Hiresh2007/Cybersecurity-Journey) |
| security-engineering-portfolio | Tracking + dashboard | [Live dashboard](https://hiresh2007.github.io/security-engineering-portfolio/) | [GitHub](https://github.com/Hiresh2007/security-engineering-portfolio) |
| Hiresh2007 (profile) | Profile README | Animated terminal, 3D calendar, snake | [GitHub](https://github.com/Hiresh2007/Hiresh2007) |

All three repos were deleted and recreated on 2026-11-07 (session 1, with
Hiresh's approval) to remove tool attribution from history; PR numbers
restarted at #1.

## Last completed tasks

- Session 5: pcap-triage allow-lists (96 tests).
- Session 4: Sigma setup and validation; first contribution prepared.
- Session 3: beaconing detector (77 tests), threshold simulation.
- Session 2: DNS tunnelling + NXDOMAIN detection (57 tests), profile asset
  build race fix, dashboard support for several sessions per day.
- Session 1: audit, project selection, pcap-triage v0.1, tracking system,
  dashboard, profile redesign.

## Branches

All repos: `main` only (plus the generated `output` branch in Hiresh2007).
Local only: `../sigma` branch `rule-update-dns-b64-single-padding` @ `a5f78ab`.

## Open pull requests

- pcap-triage #4: allow-lists (CI green)
- security-engineering-portfolio #4: state sync + session 5 records

Previously: Merged on 2026-11-10 with Hiresh's approval: pcap-triage #1 (DNS) and
#3 (beaconing; replaces #2, which GitHub closed when its base branch was
deleted), portfolio #1–#3, profile #1.

## Blockers

- No Docker on this machine; WSL is present. Needed for lab targets.
- Real-traffic validation needs a capture from Hiresh's own VM (exercise 4).
- The permission classifier blocks force-pushes and repo deletion even with
  chat approval; those commands must be run by Hiresh.

## Pending work

- UDP / NULL / FIN / Xmas scan detection
- Sigma: fork and open the prepared PR (needs approval)
- Pin pcap-triage and security-engineering-portfolio on the profile (manual)
