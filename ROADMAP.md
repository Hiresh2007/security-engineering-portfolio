# Roadmap

Checkboxes are parsed by `scripts/build_dashboard.py`: `[x]` items appear as
completed milestones, the first open items per project as upcoming tasks.
Keep one `## <project id>` heading per project (ids match `data/projects.json`).

## pcap-triage

Phase 1: core analysis (v0.1)
- [x] Streaming pcap/pcapng reader (IPv4/IPv6, TCP/UDP/ICMP)
- [x] Directional flow summary, top talkers, text/JSON report
- [x] TCP vertical scan and horizontal sweep detection (T1046) with tests
- [x] CI workflow (ruff + pytest, Python 3.10-3.13)
- [x] Publish repo to GitHub and confirm CI is green
- [ ] Record real Nmap scans against a local VM / Docker target and validate the detector on them

Phase 2: more detectors (v0.2)
- [ ] DNS anomaly detector: long / high-entropy query names, high NXDOMAIN rate (T1071.004, T1568.002). Implemented and tested in pcap-triage PR #1, awaiting merge
- [ ] Beaconing detector: low-jitter periodic connections (T1071). Implemented and tested in pcap-triage PR #2, awaiting merge
- [ ] ARP spoofing detector: IP-to-MAC binding changes (T1557.002)
- [ ] Cleartext credential detector: HTTP Basic, FTP USER/PASS, Telnet (T1040 context)
- [ ] UDP / NULL / FIN / Xmas scan detection

Phase 3: usability (v0.3)
- [ ] YAML config file and allow-lists per detector
- [ ] Markdown/HTML report output
- [ ] Cross-check findings against Suricata `eve.json` from the same capture
- [ ] Benchmark on a large public capture; document throughput

## sigma

- [ ] Fork SigmaHQ/sigma, set up sigma-cli and run `tests/test_rules.py` locally
- [ ] Read rule creation guide and 10 existing rules in one log-source family
- [ ] Find a reproducible false-positive or missing-field issue to fix
- [ ] Test the change locally (Windows VM + Sysmon where log evidence is needed)
- [ ] Open the first PR with evidence and references

## cybersecurity-journey

- [ ] Continue daily notes
- [ ] Add a writeups/ folder for completed TryHackMe/HTB rooms (profile README links to writeups that do not exist yet)

## portfolio

- [x] Tracking files: PROJECT_STATE.md, ROADMAP.md, DEVELOPMENT_LOG.md, LEARNING/, journal/
- [x] Dashboard generated from tracking files and git history
- [x] Publish repo and enable GitHub Pages deployment
