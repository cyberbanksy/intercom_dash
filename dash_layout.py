"""Dash app layout and callbacks."""
import yaml
import pandas as pd
import dash
from dash import html, dcc, dash_table
import plotly.express as px
from datetime import datetime

from etl import load_conversations


def load_theme_mapping(path='themes.yml'):
    with open(path) as f:
        data = yaml.safe_load(f) or {}
    mapping = {}
    for theme, keywords in data.items():
        for kw in keywords:
            mapping[kw.lower()] = theme
    return mapping


def categorize_themes(df: pd.DataFrame, mapping: dict) -> pd.DataFrame:
    df = df.copy()
    if df.empty or 'body' not in df.columns:
        df['theme'] = pd.Series(dtype=object)
        return df
    themes = []
    for body in df['body'].fillna(''):
        found = None
        low = body.lower()
        for kw, theme in mapping.items():
            if kw in low:
                found = theme
                break
        themes.append(found or 'other')
    df['theme'] = themes
    return df


def detect_sales(df: pd.DataFrame, keywords_path='sales_keywords.yml') -> pd.DataFrame:
    with open(keywords_path) as f:
        kws = [k.lower() for k in yaml.safe_load(f)]
    df = df.copy()
    if df.empty:
        df['is_sales'] = pd.Series(dtype=bool)
        return df
    tags_col = df['tags'] if 'tags' in df.columns else pd.Series([[]]*len(df))
    df['is_sales'] = tags_col.apply(lambda tags: bool(set(tags) & {'sales'}))
    def kw_match(text):
        t = str(text).lower()
        return any(kw in t for kw in kws)
    if 'body' in df.columns:
        df.loc[~df['is_sales'], 'is_sales'] = df['body'].fillna('').apply(kw_match)
    return df


def build_dash(server):
    df = load_conversations()
    if df.empty:
        df = pd.DataFrame(columns=['id', 'created_at', 'updated_at', 'assignee_id',
                                   'assignee_name', 'tags', 'subject', 'body',
                                   'conversation_url'])
    mapping = load_theme_mapping()
    df = categorize_themes(df, mapping)
    df = detect_sales(df)

    if 'created_at' in df.columns and not df.empty:
        volume = df.groupby(df['created_at'].dt.date).size().reset_index(name='count')
    else:
        volume = pd.DataFrame({'created_at': [], 'count': []})
    fig_volume = px.line(volume, x='created_at', y='count', title='Conversations per day')

    sales_share = df['is_sales'].mean()*100 if not df.empty else 0

    app = dash.Dash(server=server, title="Intercom Insights", external_stylesheets=[
        'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css'
    ])

    app.layout = html.Div([
        dcc.Tabs([
            dcc.Tab(label='Overview', children=[
                html.H3(f"Sales share: {sales_share:.1f}%"),
                dcc.Graph(figure=fig_volume)
            ]),
            dcc.Tab(label='Themes', children=[
                dcc.Graph(figure=px.bar(
                    df['theme'].value_counts().reset_index(name='count') if ('theme' in df.columns and not df.empty) else
                    pd.DataFrame({'theme': [], 'count': []}),
                    x='theme', y='count', title='Theme counts')),
            ]),
            dcc.Tab(label='Team', children=[
                dash_table.DataTable(
                    data=(df.groupby(['assignee_name']).size().reset_index(name='count').to_dict('records')
                          if ('assignee_name' in df.columns and not df.empty) else []),
                    columns=[{'name':'Assignee','id':'assignee_name'}, {'name':'Conversations','id':'count'}])
            ]),
            dcc.Tab(label='Drill-down', children=[
                dash_table.DataTable(
                    data=df.to_dict('records'),
                    columns=[{"name": i, "id": i, "presentation": 'markdown' if i=='conversation_url' else None} for i in df.columns]
                )
            ])
        ])
    ])
    return app
