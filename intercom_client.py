import os
import time
from datetime import datetime, timedelta
from typing import Generator, Dict, Any

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = 'https://api.intercom.io'
TOKEN = os.getenv('INTERCOM_TOKEN')
APP_ID = os.getenv('APP_ID')

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Accept': 'application/json',
    'User-Agent': 'intercom-insights/1.0'
}

def fetch_conversations_months(months: int = 12) -> Generator[Dict[str, Any], None, None]:
    """Yield conversations from the last `months` months."""
    since = int((datetime.utcnow() - timedelta(days=30*months)).timestamp())
    url = f"{BASE_URL}/conversations"
    params = {'per_page': 50, 'sort': 'created_at', 'order': 'desc'}

    while url:
        resp = requests.get(url, headers=HEADERS, params=params)
        if resp.status_code == 429:
            reset = int(resp.headers.get('X-RateLimit-Reset', '1'))
            time.sleep(reset)
            continue
        resp.raise_for_status()
        data = resp.json()
        for conv in data.get('conversations', []):
            if conv.get('created_at', 0) >= since:
                conv['conversation_url'] = (
                    f"https://app.intercom.com/a/apps/{APP_ID}/inbox/inbox/all/conversations/{conv['id']}"
                )
                yield conv
        url = data.get('pages', {}).get('next')
        params = None  # next already encoded in URL
        time.sleep(0.5)
