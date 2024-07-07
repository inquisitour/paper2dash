import dash
from dash import dcc, html
from layout import app_layout
from callbacks import register_callbacks

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS-MML_HTMLorMML',
        'rel': 'stylesheet',
        'type': 'text/javascript'
    }
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Equilibrium Logic Dashboard'
app.layout = app_layout

register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
