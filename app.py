import dash
from dash import html, dcc
from layout import create_layout
from callbacks import register_callbacks

# Initialize the Dash app
app = dash.Dash(__name__, 
                suppress_callback_exceptions=True,
                external_stylesheets=[
                    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css'
                ])

# Set the app title
app.title = 'paper2dash'

# Create the app layout
app.layout = create_layout()

# Register callbacks
register_callbacks(app)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)