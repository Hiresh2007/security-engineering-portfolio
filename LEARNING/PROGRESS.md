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
| DNS message structure: question, QR flag, rcode (NOERROR / NXDOMAIN) | Network Traffic Analysis | 2026-11-07 | introduced | pcap-triage `reader.py` |
| DNS tunnelling and exfiltration via subdomain labels | Threat Intelligence | 2026-11-07 | introduced | `detectors/dns.py` |
| Shannon entropy as a randomness signal, and its limits on short strings | Detection Engineering | 2026-11-07 | introduced | `docs/DESIGN.md` |
| Domain generation algorithms (DGA) and NXDOMAIN bursts | Threat Intelligence | 2026-11-07 | introduced | `detectors/dns.py` |
| Registered domains vs public suffixes (example.co.uk) | Network Security | 2026-11-07 | introduced | `split_name()` |
| Terminal escape injection from untrusted input | Python Security Engineering | 2026-11-07 | introduced | `_printable_name()` |
| Regression tests that pin a threshold decision | Detection Engineering | 2026-11-07 | introduced | `test_detects_hex_encoded_text_tunnel` |
| C2 beaconing and jitter as an evasion technique | Threat Intelligence | 2026-11-09 | introduced | `detectors/beacon.py` |
| Robust statistics: median and median absolute deviation (MAD) | Detection Engineering | 2026-11-09 | introduced | `interval_stats()` |
| Measuring detection and false-positive rates by simulation | Detection Engineering | 2026-11-09 | introduced | `docs/DESIGN.md` beacon table |
| Stacked pull requests | Security Automation | 2026-11-09 | introduced | pcap-triage PR #2 on #1 |
| Sigma rule structure: logsource, selection, condition, value modifiers | Detection Engineering | 2026-11-10 | introduced | `contributions/sigma-dns-b64-padding.md` |
| Base64 padding (3 bytes -> 4 chars, `=` / `==` remainder) | Network Traffic Analysis | 2026-11-10 | introduced | same |
| Pinning validator versions to match upstream CI | Security Automation | 2026-11-10 | introduced | journal 2026-11-10 |
| Open-source contribution etiquette (assigned issues, templates, changelog tags) | SOC Engineering | 2026-11-10 | introduced | same |
| Alert suppression and allow-list hygiene (reasons, auditability, fail-closed parsing) | SOC Engineering | 2026-11-11 | introduced | pcap-triage `allowlist.py` |
| CIDR matching with Python `ipaddress` | Network Security | 2026-11-11 | introduced | same |

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
5. In Wireshark, open the demo capture and filter `dns.flags.rcode == 3`. Count the
   NXDOMAIN replies and compare with `nxdomain_replies` in the JSON report.
6. By hand, compute the Shannon entropy of `abab` and `abcd`. Then explain why a
   4-character name can never exceed 2 bits/char, and why the tunnel detector also
   requires a minimum length.
7. Take one tunnel query from the demo report (e.g. `006c6162...`), strip the
   first two characters (the sequence number) and decode the rest from hex. What was
   exfiltrated?

8. Intervals of 60, 61, 59, 60, 300 s: compute the mean, standard deviation, median and
   MAD by hand. Which pair is still describing "every 60 s" after the 300 s outlier?
9. Name three legitimate programs on your own PC that probably beacon (check Task
   Manager or `netstat -abon` every minute). How would you allow-list them without
   hiding a real implant?
10. Base64-encode `a`, `ab` and `abc` (e.g. `python -c "import base64; print(base64.b64encode(b'ab'))"`).
    Explain why the padding is `==`, `=` and nothing, and why changing the Sigma rule from `==.`
    to `=.` doubles what it catches but still misses a third.
11. Write an allow-list rule for one benign program you found in exercise 9. Then explain
    what an attacker could do if the rule only set `port = 443`.

## Exercises completed

None yet.

## Needs revision

None recorded yet.
