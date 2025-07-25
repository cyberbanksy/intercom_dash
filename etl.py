"""ETL utilities for Intercom Insights."""
import pandas as pd
from typing import List, Dict, Any

from models import SessionLocal, Conversation
from intercom_client import fetch_conversations_months


def sync_conversations(months: int = 12) -> int:
    """Fetch conversations and persist raw JSON to SQLite.

    Returns number of new conversations stored."""
    session = SessionLocal()
    new = 0
    for conv in fetch_conversations_months(months):
        if not session.get(Conversation, conv['id']):
            session.add(Conversation(id=conv['id'], data=conv))
            new += 1
    session.commit()
    session.close()
    return new


def flatten(conv: Dict[str, Any]) -> Dict[str, Any]:
    """Flatten raw conversation JSON for analytics."""
    first_msg = conv.get('source', {}).get('body', '')
    assignee = conv.get('assignee', {}) or {}
    return {
        'id': conv.get('id'),
        'created_at': pd.to_datetime(conv.get('created_at'), unit='s'),
        'updated_at': pd.to_datetime(conv.get('updated_at'), unit='s'),
        'assignee_id': assignee.get('id'),
        'assignee_name': assignee.get('name'),
        'tags': [t.get('name') for t in conv.get('tags', {}).get('tags', [])],
        'subject': conv.get('title'),
        'body': first_msg,
        'conversation_url': conv.get('conversation_url'),
    }


def load_conversations() -> pd.DataFrame:
    """Load stored conversations as DataFrame."""
    session = SessionLocal()
    rows = session.query(Conversation).all()
    session.close()
    data = [flatten(r.data) for r in rows]
    return pd.DataFrame(data)
