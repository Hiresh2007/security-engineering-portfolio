# Project state

_Last updated: 2026-11-07 (session 1)_

## Selected projects

| Project | Role | Stage | Repo status |
|---|---|---|---|
| pcap-triage | Flagship (original) | v0.1: reader, flows, port-scan detection | Local only, 1 commit on `main` (`0ca2501`) |
| SigmaHQ/sigma | Open-source contribution | Selected; fork not created | n/a |
| Cybersecurity-Journey | Supporting (user's notes) | Days 1–5 of notes | On GitHub, unchanged |
| security-engineering-portfolio | Tracking + dashboard | Set up | Local only |

## Last completed tasks

- Account audit and 12-repo evaluation (`RESEARCH.md`)
- pcap-triage v0.1 implemented and tested (26 tests passing, lint clean)
- Tracking system and dashboard created; dashboard builder tested (6 tests)

## Branches

- pcap-triage: `main` (local)
- security-engineering-portfolio: `main` (local)

## Open pull requests

None.

## Blockers

1. **`gh` CLI not authenticated.** Cannot create repos, push, open PRs or read
   private repos. Fix: run `gh auth login`.
2. **Public repo creation needs approval** for `pcap-triage` and
   `security-engineering-portfolio`.
3. GitHub Pages must be enabled (Settings → Pages → Source: GitHub Actions)
   after the portfolio repo is pushed.
4. No Docker on this machine; WSL is present. Needed later for lab targets.

## Pending work

- Push both repos, confirm CI, enable Pages
- Validate scan detector on real Nmap traffic from a local VM
- DNS anomaly detector (pcap-triage v0.2)
- Sigma: fork + local test setup

## Observations for Hiresh

- The profile README says "Check my writeups repo below", but no writeups
  repo exists yet. Left unchanged; your call.
- 42 old JavaScript course repos dominate the repo list. Consider pinning
  `pcap-triage` and `Cybersecurity-Journey` on your profile once published.
