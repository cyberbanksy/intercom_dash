import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from etl import flatten

sample_conv = {
    'id': 1,
    'created_at': 0,
    'updated_at': 0,
    'assignee': {'id': 2, 'name': 'Kris'},
    'tags': {'tags': [{'name': 'sales'}]},
    'title': 'Hello',
    'source': {'body': 'Need a quote'},
    'conversation_url': 'http://example.com'
}

def test_flatten_basic():
    data = flatten(sample_conv)
    assert data['assignee_name'] == 'Kris'
    assert data['tags'] == ['sales']
    assert data['subject'] == 'Hello'
