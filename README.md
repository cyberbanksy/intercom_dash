# Intercom Insights

A Flask and Plotly Dash dashboard for analysing Intercom conversations.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # edit with your credentials
flask run
```

## Testing

```bash
pytest
```

The app schedules a nightly job to refresh Intercom data.
