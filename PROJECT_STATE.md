# Project state

_Last updated: 2026-11-17_

## Projects

| Project | Role | Stage | Repo |
|---|---|---|---|
| pcap-triage | Flagship | `main`: port scans (SYN, NULL, FIN, Xmas, UDP), DNS tunnelling, DGA, beaconing, allow-lists; 104 tests | [GitHub](https://github.com/Hiresh2007/pcap-triage) |
| SigmaHQ/sigma | Open-source contribution | [#6630](https://github.com/SigmaHQ/sigma/pull/6630) open, first review answered | fork `Hiresh2007/sigma` |
| Cybersecurity-Journey | Study notes | Days 1–5 | [GitHub](https://github.com/Hiresh2007/Cybersecurity-Journey) |
| security-engineering-portfolio | Tracking + dashboard | [Live dashboard](https://hiresh2007.github.io/security-engineering-portfolio/) | [GitHub](https://github.com/Hiresh2007/security-engineering-portfolio) |
| Hiresh2007 | Profile README | Animated terminal, 3D calendar, snake | [GitHub](https://github.com/Hiresh2007/Hiresh2007) |

## Recent work

- 2026-11-17: answered the first review on Sigma #6630 (benign-data check, reference tool analysis).
- 2026-11-15: NULL / FIN / Xmas / UDP scan detection; submitted Sigma #6630.
- 2026-11-11: allow-lists with mandatory reasons.
- 2026-11-10: Sigma set-up and validation; DNS base64 rule fix prepared.
- 2026-11-09: beaconing detector with measured detection rates.
- 2026-11-07: pcap-triage v0.1 and DNS detection; portfolio, dashboard and profile set up.

## Open pull requests

- SigmaHQ/sigma #6630: DNS base64 rule, single padding
- security-engineering-portfolio #5: Sigma records

## Blockers

- No Docker on this machine (WSL is available). Needed for lab targets.
- Real-traffic validation needs captures from a lab VM.

## Next

- Cleartext credential detector (HTTP Basic, FTP, Telnet)
- Follow up on Sigma #6630 review
