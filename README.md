# Intercom Insights

A Flask and Plotly Dash dashboard for analysing Intercom conversations.

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

[![CI](https://github.com/cyberbanksy/intercom_dash/actions/workflows/ci.yml/badge.svg)](https://github.com/cyberbanksy/intercom_dash/actions/workflows/ci.yml)
[![Latest release](https://img.shields.io/github/v/release/cyberbanksy/intercom_dash?include_prereleases&sort=semver)](https://github.com/cyberbanksy/intercom_dash/releases)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/cyberbanksy/intercom_dash/badge)](https://scorecard.dev/viewer/?uri=github.com/cyberbanksy/intercom_dash)

Changes are recorded in [CHANGELOG.md](CHANGELOG.md) and tagged `vX.Y.Z` with
[Semantic Versioning](https://semver.org/). There are no prebuilt downloads; run it from source (see above).

- **Cadence:** changes ship when they are ready, with at least one maintenance pass a month while the project
  is in active development. Security fixes ship within 7 days of a confirmed report.
- **Support:** only the latest version on `main` gets fixes.

