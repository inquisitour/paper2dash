from dash import html, dcc
from styles import styles

def create_header():
    return html.Header([
        html.Div([
            html.Img(src='/assets/logo.png', alt='Logo', className='logo'),
            html.H1('Characterising Equilibrium Logic and Nested Logic Programs: Reductions and Complexity', className='header-title')
        ], className='header-left', style={'display': 'flex', 'alignItems': 'center', 'flex': '1'}),
        html.Div([
            html.Div([
                dcc.Input(
                    id='search-input',
                    type='text',
                    placeholder='Search references...',
                    style=styles['input']
                )
            ], **{'aria-label': 'Search references'}),
            html.Button('Search', id='search-button', style=styles['button'], **{'aria-label': 'Perform search'}),
            html.Button('Toggle Sidebar', id='sidebar-toggle', className='toggle-btn', style=styles['button'], **{'aria-label': 'Toggle sidebar visibility'}),
            html.Button('Toggle Dark Mode', id='dark-mode-toggle', n_clicks=0, style=styles['button'], **{'aria-label': 'Toggle dark mode'})
        ], className='header-right', style={'display': 'flex', 'alignItems': 'center'})
    ], className='header', id='header', style=styles['header'], **{'aria-label': 'Page header'})