from dash import html, dcc
from components.sidebar import create_sidebar
from components.header import create_header
from components.content_area import create_content_area
from styles import styles

def create_layout():
    return html.Div([
        dcc.Location(id='url', refresh=False),
        dcc.Store(id='dark-mode-store', data={'dark_mode': False}),
        html.Div([
            create_header(),
            html.Div([
                create_sidebar(),
                create_content_area()
            ], className='main-container', style=styles['main_container']),
            html.Footer([
                html.P('© 2024 paper2dash'),
                html.P('Last Updated: July 7, 2024')
            ], id='footer', style=styles['footer'])
        ], id='body')
    ])