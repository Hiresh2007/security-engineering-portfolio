# Project state

_Last updated: 2026-11-07 (session 2)_

## Selected projects

| Project | Role | Stage | Repo |
|---|---|---|---|
| pcap-triage | Flagship (original) | v0.1 on `main`; v0.2 (DNS detection) in PR #1 | [GitHub](https://github.com/Hiresh2007/pcap-triage), CI green |
| SigmaHQ/sigma | Open-source contribution | Selected; fork not created | n/a |
| Cybersecurity-Journey | Supporting (Hiresh's notes) | Days 1–5 | [GitHub](https://github.com/Hiresh2007/Cybersecurity-Journey) |
| security-engineering-portfolio | Tracking + dashboard | [Live dashboard](https://hiresh2007.github.io/security-engineering-portfolio/) | [GitHub](https://github.com/Hiresh2007/security-engineering-portfolio) |
| Hiresh2007 (profile) | Profile README | Animated terminal, 3D calendar, snake | [GitHub](https://github.com/Hiresh2007/Hiresh2007) |

All three repos were deleted and recreated on 2026-11-07 (session 1, with
Hiresh's approval) to remove tool attribution from history; PR numbers
restarted at #1.

## Last completed tasks

- Session 2: DNS tunnelling + NXDOMAIN detection (57 tests), profile asset
  build race fix, dashboard support for several sessions per day.
- Session 1: audit, project selection, pcap-triage v0.1, tracking system,
  dashboard, profile redesign.

## Branches

- pcap-triage: `main`, `feature/dns-anomaly-detector`
- Hiresh2007: `main`, `output` (generated assets), `fix-assets-concurrency`
- security-engineering-portfolio: `main`, `session-2-dns-detector`

## Open pull requests (awaiting Hiresh's merge approval)

- pcap-triage #1: DNS tunnelling and NXDOMAIN (DGA) detection (v0.2.0)
- Hiresh2007 #1: run profile asset builds one at a time
- security-engineering-portfolio: session 2 records

## Blockers

- No Docker on this machine; WSL is present. Needed for lab targets.
- Real-traffic validation needs a capture from Hiresh's own VM (exercise 4).
- The permission classifier blocks force-pushes and repo deletion even with
  chat approval; those commands must be run by Hiresh.

## Pending work

- Beaconing detector (pcap-triage v0.2 roadmap)
- Sigma: fork + local test setup
- Pin pcap-triage and security-engineering-portfolio on the profile (manual)
