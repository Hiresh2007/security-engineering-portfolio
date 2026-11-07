# security-engineering-portfolio

Tracking repository and dashboard for Hiresh Yadav's cybersecurity
engineering work. Each working session is recorded in `journal/`.

| File | Purpose |
|---|---|
| [PROJECT_STATE.md](PROJECT_STATE.md) | Current state: projects, branches, PRs, blockers |
| [ROADMAP.md](ROADMAP.md) | Per-project milestones (checkboxes feed the dashboard) |
| [DEVELOPMENT_LOG.md](DEVELOPMENT_LOG.md) | Chronological engineering log |
| [RESEARCH.md](RESEARCH.md) | Repository evaluation and discoveries |
| [LEARNING/PROGRESS.md](LEARNING/PROGRESS.md) | Concepts introduced / practised, exercises |
| [journal/](journal/) | One file per session |
| [dashboard/](dashboard/) | Static dashboard (`index.html` + generated `data.json`) |

## Projects

- [pcap-triage](https://github.com/Hiresh2007/pcap-triage): flagship, offline PCAP triage and detection
- [SigmaHQ/sigma](https://github.com/SigmaHQ/sigma): open-source contribution target
- [Cybersecurity-Journey](https://github.com/Hiresh2007/Cybersecurity-Journey): study notes

## Dashboard

```bash
python scripts/build_dashboard.py      # reads tracking files + git history
cd dashboard && python -m http.server  # open http://localhost:8000
```

On push to `main`, `.github/workflows/pages.yml` tests the builder, rebuilds
`data.json` and deploys to GitHub Pages. Nothing in `data.json` is typed by
hand; it is derived from the files above and from git.
