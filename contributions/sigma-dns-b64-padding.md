# Sigma contribution: DNS base64 rule misses single-padded labels

| | |
|---|---|
| Upstream | [SigmaHQ/sigma](https://github.com/SigmaHQ/sigma) |
| Rule | `rules/network/dns/net_dns_susp_b64_queries.yml` (id `4153a907-2451-4e4f-a578-c52bb6881432`) |
| Local branch | `rule-update-dns-b64-single-padding` in `../sigma`, commit `a5f78ab` |
| Status | Prepared and validated locally. **Not submitted**: fork + PR need Hiresh's approval |
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
  from the cloned repository, and running them was blocked by the local
  permission policy. Upstream CI runs them on the PR.

## Notes for Hiresh (read before submitting)

- You should be able to explain in your own words why base64 ends in
  `==`, `=` or nothing (every 3 input bytes become 4 output characters; the
  remainder is padded). Exercise 10 in `LEARNING/PROGRESS.md`.
- Reviewer questions are yours to answer. A likely one: "any real-world FP
  with a single `=`?" Honest answer: none known; `=` is invalid in hostnames;
  no production DNS logs were available to measure against.
- Local validator tip: the latest `pySigma-validators-sigmahq` (0.30.0)
  reports 55 issues on upstream main (UUID v1 rule ids). Upstream CI pins
  0.21.*, under which there are 0. Use the pinned version.

---

## Draft PR text (Sigma template)

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
