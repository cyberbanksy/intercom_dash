<div align="center">

# Intercom Insights

**A Flask and Plotly Dash dashboard for analysing Intercom conversations.**

[![CI](https://img.shields.io/github/actions/workflow/status/cyberbanksy/intercom_dash/ci.yml?branch=main&style=flat-square&label=CI)](https://github.com/cyberbanksy/intercom_dash/actions/workflows/ci.yml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/cyberbanksy/intercom_dash/badge)](https://scorecard.dev/viewer/?uri=github.com/cyberbanksy/intercom_dash)
[![License: MIT](https://img.shields.io/badge/license-MIT-2ea44f?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3-3776ab?style=flat-square&logo=python&logoColor=white)](requirements.txt)

[Setup](#setup) · [Testing](#testing) · [Releases](#releases)

</div>

---

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # edit with your credentials
# fetch conversations (defaults to last 12 months)
python etl.py --months 12
# run the dashboard
flask --app app:app.server run
# or in production
# gunicorn app:app.server
```

Keep your `.env` file private and never commit it to version control.

## Testing

```bash
pytest
```

The app schedules a nightly job to refresh Intercom data.

## Releases

Changes are recorded in [CHANGELOG.md](CHANGELOG.md) and tagged `vX.Y.Z` with
[Semantic Versioning](https://semver.org/). There are no prebuilt downloads; run it from source (see above).

- **Cadence:** changes ship when they are ready, with at least one maintenance pass a month while the project
  is in active development. Security fixes ship within 7 days of a confirmed report.
- **Support:** only the latest version on `main` gets fixes.

## License

MIT, see [LICENSE](LICENSE).
