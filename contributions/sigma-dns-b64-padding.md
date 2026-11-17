# Sigma contribution: DNS base64 rule misses single-padded labels

| | |
|---|---|
| Upstream | [SigmaHQ/sigma](https://github.com/SigmaHQ/sigma) |
| Rule | `rules/network/dns/net_dns_susp_b64_queries.yml` (id `4153a907-2451-4e4f-a578-c52bb6881432`) |
| Local branch | `rule-update-dns-b64-single-padding` in `../sigma`, commit `a5f78ab` |
| Status | Submitted 2026-11-15 as [SigmaHQ/sigma#6630](https://github.com/SigmaHQ/sigma/pull/6630) from fork `Hiresh2007/sigma`. Open, awaiting maintainer review |
| Prior discussion | None found (issues/PRs searched by rule id and title, 2026-11-10) |

## The problem

The rule matches `query|contains: '==.'`, i.e. a base64 chunk that ends in
two padding characters followed by the next label. Base64 output ends in `==`,
`=` or nothing depending on input length mod 3, each one third of the time
(checked for input lengths 1–300: 100 / 100 / 100). The rule therefore only
fires on one third of padded or unpadded base64 labels, and on none of the
single-padded ones.

| Encoded data | Query | Matches `==.` | Matches `=.` |
|---|---|---|---|
| `hostname=ws01` | `aG9zdG5hbWU9d3MwMQ==.t.example.net` | yes | yes |
| `user=bob` | `dXNlcj1ib2I=.t.example.net` | **no** | yes |
| `secret` | `c2VjcmV0.t.example.net` | no | no |

## The change

`'==.'` → `'=.'`. `'=.'` is a superset of `'==.'`, so nothing previously
detected is lost. `modified` updated.

Unpadded base64 cannot be recognised by padding at all; that needs
statistical features (length, entropy) across many queries, which is out of
scope for this single-event rule.

**False-positive reasoning.** `=` is not a valid hostname character
(letters, digits, hyphen only; RFC 952 / RFC 1123), so legitimate hostnames
should not contain it. The rule already depends on `=` appearing in a query;
the change only stops requiring two of them.

## Validation

- `sigma check --fail-on-error --fail-on-issues --validation-config tests/sigma_cli_conf.yml`
  on `rules/network/dns/` with `pySigma-validators-sigmahq==0.21.*` (the
  version pinned in upstream CI): 0 errors, 0 issues.
- Full repository check with the same settings before the change: 0 issues.
- Not run: `tests/test_rules.py` / `tests/test_logsource.py`. These are code
  from the cloned repository and were not run locally; upstream CI runs them
  on the PR (both passed on #6630).

---

## PR text as submitted

### Summary of the Pull Request

The rule only matched base64 chunks ending in `==`. Base64 ends in `==`, `=`
or nothing with equal frequency, so labels ending in a single `=` (one third
of padded/unpadded encodings, half of padded ones) were missed. Matching `=.`
covers both padding forms and still includes every case matched before.

### Changelog

update: Suspicious DNS Query with B64 Encoded String - also match single padding

### Example Log Event

```
query: dXNlcj1ib2I=.t.example.net   (base64 of "user=bob")
```

### Fixed Issues

None

### SigmaHQ Rule Creation Conventions

- If your PR adds new rules, please consider following and applying these [conventions](https://github.com/SigmaHQ/sigma-specification/blob/main/sigmahq/)

---

## Review round 1 (2026-11-17)

Reviewer: Varunpoojari. All 16
upstream CI checks passed, including `test-sigma-legacy` (the repo's
`test_rules.py`) and the clean Windows baseline checks.

### Questions and evidence

**1. Checked against benign DNS data?**
Cisco Umbrella Top 1M (downloaded 2026-11-17; the most-queried DNS names
on OpenDNS, including full hostnames such as CDN and tracking subdomains):
1,000,000 names, **0 contain `=` anywhere**, so 0 matches for both `==.` and
`=.`. Caveat: a popularity list may drop malformed names, so this shows
normal traffic does not contain `=`, not that unusual traffic never does.

**2. Description / what was tested.**
Prepared in commit `1046bb9`: description now says the
rule matches a base64 label ending with one or two padding characters;
`modified` updated. `falsepositives: Unknown` left as is: no benign source was
found, and naming an invented one would be worse.

**3. Real sample?**
The rule's own reference, `krmaxwell/dns-exfiltration`, encodes
`struct.pack('L8s', part, data)`: 16 bytes on 64-bit Linux (`==` padding,
which is why the rule used `==.`), but 12 bytes on Windows / 32-bit (**no
padding**). Padding depends only on payload length, and tools use fixed
chunk sizes, so a tool's queries all share one padding. A tool whose payload
length is 2 mod 3 (e.g. 14 or 17 bytes) produces `=` on *every* query and was
never detected by `==.`, not just one query in three.
