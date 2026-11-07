# Research

## Repository evaluation (2026-11-07)

Metadata from the GitHub API on 2026-11-07. "Last push" is the most recent
push to any branch. Good-first-issue counts use the `good first issue` label.

| Repository | Lang | License | Stars | Last push | GFI | Fit and notes |
|---|---|---|---|---|---|---|
| SigmaHQ/sigma | YAML/Python | DRL 1.1 (rules) | 11.4k | 2026-11-07 | 0 | **Selected for contributions.** SOC detection rules; clear CONTRIBUTING with local test scripts (`test_rules.py`, `sigma check`). Approachable via FP fixes. |
| secdev/scapy | Python | GPL-2.0 | 12.7k | 2026-11-04 | 0 | Strong runner-up; core library of the flagship. Requires `AI-Assisted:` commit trailer; no AI-written replies or docs. Better after months with Scapy internals. |
| mandiant/capa | Python | Apache-2.0 | 6.3k | 2026-11-06 | 1 | Capability detection in executables. Good code quality; steep learning curve (binary analysis). |
| mandiant/capa-rules | YAML | Apache-2.0 | 0.8k | 2026-11-06 | 16 | Many labelled starter issues, but rule testing needs malware samples: only in an isolated lab. Later candidate. |
| zeek/zeek | C++ | BSD-3 | 8.2k | 2026-11-06 | n/a | Network security monitor; reference for flow/log design. Large C++ codebase. |
| OISF/suricata | C/Rust | GPL-2.0 | 6.8k | 2026-11-05 | n/a | IDS/IPS; Redmine-based contribution workflow. Use as comparison engine for pcap-triage. |
| VirusTotal/yara-x | Rust | BSD-3 | 1.4k | 2026-11-06 | n/a | Rust rewrite of YARA; Rust knowledge needed. |
| projectdiscovery/nuclei-templates | YAML | MIT | 13.3k | 2026-11-07 | n/a | Very active; templates need authorised targets to validate. |
| OWASP/CheatSheetSeries | Markdown | CC-BY-SA-4.0 | 33.9k | 2026-11-05 | 0 | Documentation contributions; useful for web security learning. |
| Yamato-Security/hayabusa | Rust | AGPL-3.0 | 3.4k | 2026-11-06 | 0 | Windows event-log fast forensics using Sigma rules. Rust. |
| Neo23x0/signature-base | YARA | DRL | 3.1k | 2026-11-06 | n/a | YARA/IOC set; samples needed for validation. |
| mitre-attack/attack-stix-data | JSON | n/a | 0.7k | 2026-11-05 | n/a | ATT&CK data; consumable by pcap-triage for technique names later. |

### Selection rationale

- **Flagship, original `pcap-triage`:** the GitHub account had no security
  engineering code. A traffic-analysis tool matches the stated SOC Analyst
  goal, exercises Python + Scapy + detection logic, and can be validated
  safely with synthetic and self-recorded lab traffic. It complements Zeek and
  Suricata rather than duplicating them: small, explainable detectors with
  evidence in every finding.
- **Contribution target `SigmaHQ/sigma`:** detection rules are what SOC teams
  use daily; the repo has documented local validation and frequent merges.
- **Supporting `Cybersecurity-Journey`:** existing personal notes repo; stays
  the user's own writing.

## Discoveries

- 2026-11-07 — Scapy needs no libpcap/Npcap to read or write capture files, but building `ARP()` / `Ether()` without explicit MACs makes it resolve a local interface, which fails on Windows without Npcap. Tests set MACs explicitly.
- 2026-11-07 — On a `slots=True` dataclass, `Cls.field` is a slot descriptor rather than the default value. Read defaults from an instance.
- 2026-11-07 — secdev/scapy's CONTRIBUTING requires an `AI-Assisted: yes/no (tool)` trailer on every commit, adapted from Wireshark's AI policy.
