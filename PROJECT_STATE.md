# Project state

_Last updated: 2026-11-07 (session 1)_

## Selected projects

| Project | Role | Stage | Repo status |
|---|---|---|---|
| pcap-triage | Flagship (original) | v0.1: reader, flows, port-scan detection | [Public](https://github.com/Hiresh2007/pcap-triage), `main` @ `0ca2501`, CI green |
| SigmaHQ/sigma | Open-source contribution | Selected; fork not created | n/a |
| Cybersecurity-Journey | Supporting (user's notes) | Days 1–5 of notes | On GitHub, unchanged |
| security-engineering-portfolio | Tracking + dashboard | Live at https://hiresh2007.github.io/security-engineering-portfolio/ | [Public](https://github.com/Hiresh2007/security-engineering-portfolio), Pages deploy green |

## Last completed tasks

- Account audit and 12-repo evaluation (`RESEARCH.md`)
- pcap-triage v0.1 implemented and tested (26 tests passing, lint clean)
- Tracking system and dashboard created; dashboard builder tested (6 tests)

## Branches

- pcap-triage: `main`
- security-engineering-portfolio: `main`, `session-1-publish` (PR: state updates after publishing)

## Open pull requests

None.

## Blockers

- No Docker on this machine; WSL is present. Needed later for lab targets.
- Resolved 2026-11-07: `gh` authenticated (scopes repo, workflow, read:org, gist);
  both repos published with Hiresh's approval; Pages enabled.

## Pending work

- Validate scan detector on real Nmap traffic from a local VM
- DNS anomaly detector (pcap-triage v0.2)
- Sigma: fork + local test setup

## Observations for Hiresh

- The profile README says "Check my writeups repo below", but no writeups
  repo exists yet. Left unchanged; your call.
- 42 old JavaScript course repos dominate the repo list. Consider pinning
  `pcap-triage` and `Cybersecurity-Journey` on your profile once published.
