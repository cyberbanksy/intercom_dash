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
