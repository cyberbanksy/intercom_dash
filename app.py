"""Flask entry point for Intercom Insights."""
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

from etl import sync_conversations
from dash_layout import build_dash


def create_app() -> Flask:
    app = Flask(__name__)

    scheduler = BackgroundScheduler()
    scheduler.add_job(sync_conversations, 'cron', hour=0)
    scheduler.start()

    build_dash(app)
    return app


app = create_app()

if __name__ == '__main__':
    sync_conversations()
    app.run(debug=True)
