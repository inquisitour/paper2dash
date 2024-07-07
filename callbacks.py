from dash.dependencies import Input, Output, State
from dash import html, dcc
import plotly.graph_objs as go
from utils.data_processing import get_complexity_data, get_complexity_content, get_content, get_references, search_references, format_reference
from styles import styles, apply_dark_mode

def register_callbacks(app):
    @app.callback(
        Output('sidebar-content', 'style'),
        [Input('sidebar-toggle', 'n_clicks')],
        [State('sidebar-content', 'style')]
    )
    def toggle_sidebar(n_clicks_sidebar, sidebar_style):
        if n_clicks_sidebar is None:
            return sidebar_style
        if sidebar_style is None:
            sidebar_style = styles['sidebar']
        if 'display' in sidebar_style and sidebar_style['display'] == 'none':
            sidebar_style['display'] = 'block'
        else:
            sidebar_style['display'] = 'none'
        return sidebar_style

    @app.callback(
        [
            Output('content-area', 'style'),
            Output('header', 'style'),
            Output('footer', 'style'),
            Output('dark-mode-store', 'data')
        ],
        [Input('dark-mode-toggle', 'n_clicks')],
        [State('content-area', 'style'),
         State('header', 'style'),
         State('footer', 'style'),
         State('dark-mode-store', 'data')]
    )
    def toggle_dark_mode(n_clicks_dark_mode, content_style, header_style, footer_style, dark_mode_data):
        if n_clicks_dark_mode is None:
            return content_style, header_style, footer_style, dark_mode_data
        dark_mode = not dark_mode_data['dark_mode']
        dark_mode_data['dark_mode'] = dark_mode

        if dark_mode:
            return apply_dark_mode(styles['content_area']), apply_dark_mode(styles['header']), apply_dark_mode(styles['footer']), dark_mode_data
        else:
            return styles['content_area'], styles['header'], styles['footer'], dark_mode_data

    @app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname'),
         Input('dark-mode-store', 'data')]
    )
    def display_page(pathname, dark_mode_data):
        is_dark_mode = dark_mode_data['dark_mode']
        style = styles['dark_mode_card'] if is_dark_mode else styles['card']
        
        if pathname.strip('/') == 'complexity':
            return create_complexity_content(style)
        
        content = get_content(pathname)
        if not content:
            return html.Div([
                html.H1("404 - Not Found"),
                html.P("The requested page does not exist.")
            ], style=style)
        
        if pathname.strip('/') == 'references':
            references = get_references()
            return html.Div([
                html.H1(content['title']),
                html.Div([
                    html.P(format_reference(ref)) for ref in references
                ])
            ], style=style)
        elif 'sections' in content:
            return html.Div([
                html.H1(content['title']),
                html.Div([
                    html.Div([
                        html.H2(section['title']),
                        html.Div([html.P(p) for p in section['content']])
                    ]) for section in content['sections']
                ])
            ], style=style)
        else:
            return html.Div([
                html.H1(content['title']),
                html.Div([html.P(p) for p in content['paragraphs']])
            ], style=style)

    @app.callback(
        Output('reference-search-results', 'children'),
        [Input('reference-search-input', 'value')]
    )
    def search_reference_results(search_term):
        if not search_term:
            return []
        results = search_references(search_term)
        return [html.P(format_reference(ref)) for ref in results]

    @app.callback(
        Output('search-results', 'children'),
        [Input('search-button', 'n_clicks')],
        [State('search-input', 'value')]
    )
    def perform_search(n_clicks, search_term):
        if not n_clicks or not search_term:
            return []
        results = search_references(search_term)
        return [html.P(format_reference(ref)) for ref in results]

    def create_complexity_content(style):
        complexity_content = get_complexity_content()
        return html.Div([
            html.H1(complexity_content['title']),
            html.Div([
                html.Div([
                    html.H2(section['title']),
                    html.Div([html.P(p) for p in section['content']])
                ]) for section in complexity_content.get('sections', [])
            ]),
            html.Div([
                dcc.Dropdown(
                    id='chart-type',
                    options=[
                        {'label': 'Bar Chart', 'value': 'bar'},
                        {'label': 'Radar Chart', 'value': 'radar'}
                    ],
                    value='bar',
                    style={'width': '50%', 'margin': '10px 0'}
                ),
                dcc.Graph(id='complexity-chart')
            ], className='chart-container', style={'marginTop': '20px'})
        ], style=style)

    @app.callback(
        Output('complexity-chart', 'figure'),
        [Input('chart-type', 'value'),
        Input('dark-mode-store', 'data')]
    )
    def update_complexity_chart(chart_type, dark_mode_data):
        data = get_complexity_data()
        is_dark_mode = dark_mode_data['dark_mode']
        
        if chart_type == 'bar':
            return create_bar_chart(data, is_dark_mode)
        elif chart_type == 'radar':
            return create_radar_chart(data, is_dark_mode)

    def create_bar_chart(data, is_dark_mode):
        background_color = '#1e1e1e' if is_dark_mode else '#ffffff'
        text_color = '#ffffff' if is_dark_mode else '#000000'
        bar_color = '#007bff'  # A nice blue color that should work well in both light and dark modes

        return {
            'data': [go.Bar(
                x=[d['Task'] for d in data],
                y=[d['ComplexityValue'] for d in data],
                text=[d['Complexity'] for d in data],
                textposition='auto',
                hoverinfo='text',
                marker_color=bar_color
            )],
            'layout': go.Layout(
                title={
                    'text': 'Complexity of Reasoning Tasks',
                    'font': {'color': text_color}
                },
                xaxis={
                    'title': 'Task',
                    'tickangle': -45,
                    'tickfont': {'color': text_color},
                    'title_font': {'color': text_color}
                },
                yaxis={
                    'title': 'Complexity Class',
                    'tickvals': [1, 2, 3, 4],
                    'ticktext': ['NP', 'co-NP', 'ΣP2', 'ΠP2'],
                    'tickfont': {'color': text_color},
                    'title_font': {'color': text_color}
                },
                margin={'l': 50, 'b': 100, 't': 50, 'r': 50},
                hovermode='closest',
                plot_bgcolor=background_color,
                paper_bgcolor=background_color,
                font={'color': text_color}
            )
        }

    def create_radar_chart(data, is_dark_mode):
        background_color = '#1e1e1e' if is_dark_mode else '#ffffff'
        text_color = '#ffffff' if is_dark_mode else '#000000'
        line_color = '#007bff' 

        return {
            'data': [go.Scatterpolar(
                r=[d['ComplexityValue'] for d in data],
                theta=[d['Task'] for d in data],
                fill='toself',
                name='Complexity',
                line_color=line_color
            )],
            'layout': go.Layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 4],
                        tickvals=[1, 2, 3, 4],
                        ticktext=['NP', 'co-NP', 'ΣP2', 'ΠP2'],
                        tickfont={'color': text_color}
                    ),
                    angularaxis=dict(
                        tickfont={'color': text_color}
                    ),
                    bgcolor=background_color
                ),
                showlegend=False,
                title={
                    'text': 'Complexity of Reasoning Tasks',
                    'font': {'color': text_color}
                },
                paper_bgcolor=background_color,
                font={'color': text_color}
            )
        }