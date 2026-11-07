# Learning progress

Status meanings: **introduced** = seen and explained in a session;
**practised** = Hiresh has used it independently (exercise or own change);
**needs revision** = revisit. Nothing is marked mastered. Code that exists in a
project but has not been reproduced independently counts as *introduced* only.

The table below is parsed by the dashboard; keep the column order.

| Concept | Area | Introduced | Status | Where |
|---|---|---|---|---|
| TCP three-way handshake & flags (SYN, SYN-ACK, RST) | Network Security | 2026-11-07 | introduced | pcap-triage `reader.py` |
| SYN (half-open) port scanning & how replies reveal open/closed ports | Network Security | 2026-11-07 | introduced | pcap-triage `detectors/portscan.py` |
| Vertical scan vs horizontal sweep | Intrusion Detection | 2026-11-07 | introduced | pcap-triage `docs/DESIGN.md` |
| Sliding-window distinct counting (two pointers) | Detection Engineering | 2026-11-07 | introduced | `detectors/base.py` |
| Detection thresholds, false positives & evasion (slow scans) | SOC Engineering | 2026-11-07 | introduced | `docs/DESIGN.md` |
| MITRE ATT&CK mapping (T1046 Network Service Discovery) | Threat Intelligence | 2026-11-07 | introduced | finding `attack_technique` |
| pcap vs pcapng formats; streaming reads with Scapy PcapReader | Network Traffic Analysis | 2026-11-07 | introduced | `reader.py` |
| Building synthetic test traffic with Scapy | Python Security Engineering | 2026-11-07 | introduced | `tests/conftest.py` |
| Static security linting (ruff / flake8-bandit S rules) | Python Security Engineering | 2026-11-07 | introduced | `pyproject.toml` |
| CI with GitHub Actions test matrix | Security Automation | 2026-11-07 | introduced | `.github/workflows/ci.yml` |

## Exercises for Hiresh

Small tasks to turn *introduced* into *practised*. Do them yourself; ask for review afterwards.

1. Open `samples/demo_scan.pcap` in Wireshark. Apply `tcp.flags.syn==1 && tcp.flags.ack==0`
   and confirm the packet count matches `syn_packets` in the JSON report.
2. Explain in your own words (in `Cybersecurity-Journey`) why a SYN-ACK reply means
   *open* and RST means *closed* in a SYN scan.
3. Change `scripts/make_demo_pcap.py` so the scan probes one port every 5 seconds.
   Predict whether the default 60 s window flags it, then run the tool to check.
4. In a lab VM you own, run `nmap -sS -p 1-200 <your-vm>` while capturing with
   Wireshark, and analyse the capture with `pcap-triage`.

## Exercises completed

None yet.

## Needs revision

None recorded yet.
