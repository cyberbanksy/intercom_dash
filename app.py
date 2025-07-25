"""Flask entry point for Intercom Insights."""
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
import dash

load_dotenv()

from etl import sync_conversations
from dash_layout import build_dash


def create_app() -> dash.Dash:
    server = Flask(__name__)

    scheduler = BackgroundScheduler()
    scheduler.add_job(sync_conversations, 'cron', hour=0)
    scheduler.start()

    dash_app = build_dash(server)
    return dash_app


app = create_app()

if __name__ == '__main__':
    sync_conversations()
    app.run_server(debug=True)
