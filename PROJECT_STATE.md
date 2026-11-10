# Project state

_Last updated: 2026-11-09 (session 3)_

## Selected projects

| Project | Role | Stage | Repo |
|---|---|---|---|
| pcap-triage | Flagship (original) | v0.1 on `main`; v0.2 in review: DNS detection (PR #1), beaconing (PR #2, stacked) | [GitHub](https://github.com/Hiresh2007/pcap-triage), CI green |
| SigmaHQ/sigma | Open-source contribution | Selected; fork not created | n/a |
| Cybersecurity-Journey | Supporting (Hiresh's notes) | Days 1–5 | [GitHub](https://github.com/Hiresh2007/Cybersecurity-Journey) |
| security-engineering-portfolio | Tracking + dashboard | [Live dashboard](https://hiresh2007.github.io/security-engineering-portfolio/) | [GitHub](https://github.com/Hiresh2007/security-engineering-portfolio) |
| Hiresh2007 (profile) | Profile README | Animated terminal, 3D calendar, snake | [GitHub](https://github.com/Hiresh2007/Hiresh2007) |

All three repos were deleted and recreated on 2026-11-07 (session 1, with
Hiresh's approval) to remove tool attribution from history; PR numbers
restarted at #1.

## Last completed tasks

- Session 3: beaconing detector (77 tests), threshold simulation.
- Session 2: DNS tunnelling + NXDOMAIN detection (57 tests), profile asset
  build race fix, dashboard support for several sessions per day.
- Session 1: audit, project selection, pcap-triage v0.1, tracking system,
  dashboard, profile redesign.

## Branches

- pcap-triage: `main`, `feature/dns-anomaly-detector`, `feature/beaconing-detector`
- Hiresh2007: `main`, `output` (generated assets), `fix-assets-concurrency`
- security-engineering-portfolio: `main`, `session-2-dns-detector`, `session-3-beaconing`

## Open pull requests (awaiting Hiresh's merge approval)

- pcap-triage #1: DNS tunnelling and NXDOMAIN (DGA) detection (v0.2.0)
- pcap-triage #2: beaconing detection (stacked on #1; merge #1 first)
- Hiresh2007 #1: run profile asset builds one at a time
- security-engineering-portfolio #1: session 2 records; session 3 records (stacked)

## Blockers

- No Docker on this machine; WSL is present. Needed for lab targets.
- Real-traffic validation needs a capture from Hiresh's own VM (exercise 4).
- The permission classifier blocks force-pushes and repo deletion even with
  chat approval; those commands must be run by Hiresh.

## Pending work

- Per-detector allow-lists / config file (pcap-triage v0.3)
- Sigma: fork + local test setup
- Pin pcap-triage and security-engineering-portfolio on the profile (manual)
