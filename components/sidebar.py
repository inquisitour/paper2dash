from dash import html, dcc
from styles import styles

def create_sidebar():
    return html.Div([
        html.Div([
            html.H2('Navigation', id='nav-title'),
            html.Nav(
                [
                    html.Div([dcc.Link('Overview', href='/overview', className='sidebar-link')], **{'aria-label': 'Go to Overview'}),
                    html.Div([dcc.Link('Background', href='/background', className='sidebar-link')], **{'aria-label': 'Go to Background'}),
                    html.Div([dcc.Link('Encodings', href='/encodings', className='sidebar-link')], **{'aria-label': 'Go to Encodings'}),
                    html.Div([dcc.Link('Complexity', href='/complexity', className='sidebar-link')], **{'aria-label': 'Go to Complexity'}),
                    html.Div([dcc.Link('Equivalence', href='/equivalence', className='sidebar-link')], **{'aria-label': 'Go to Equivalence'}),
                    html.Div([dcc.Link('Circumscription', href='/circumscription', className='sidebar-link')], **{'aria-label': 'Go to Circumscription'}),
                    html.Div([dcc.Link('Strong Negation', href='/strong-negation', className='sidebar-link')], **{'aria-label': 'Go to Strong Negation'}),
                    html.Div([dcc.Link('Related Works', href='/related-works', className='sidebar-link')], **{'aria-label': 'Go to Related Works'}),
                    html.Div([dcc.Link('Concluding Remarks', href='/concluding-remarks', className='sidebar-link')], **{'aria-label': 'Go to Concluding Remarks'}),
                    html.Div([dcc.Link('Appendix', href='/appendix', className='sidebar-link')], **{'aria-label': 'Go to Appendix'}),
                    html.Div([dcc.Link('References', href='/references', className='sidebar-link')], **{'aria-label': 'Go to References'}),
                ],
                **{'aria-labelledby': 'nav-title'}
            )
        ], id='sidebar-content', style=styles['sidebar'])
    ], **{'aria-label': 'Sidebar navigation'})