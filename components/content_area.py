from dash import html
from styles import styles

def create_content_area():
    return html.Div(id='content-area', children=[
        html.Div(id='page-content', style={'display': 'block', 'width': '100%'})
    ], style=styles['content_area'])
