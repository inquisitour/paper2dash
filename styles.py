styles = {
    'main_container': {
        'display': 'flex',
        'flexDirection': 'row',
        'flexGrow': '1',
        'height': '100%',  # Ensure full height
        'overflow': 'hidden'
    },
    'header': {
        'backgroundColor': '#f8f9fa',
        'padding': '10px',
        'borderBottom': '1px solid #dee2e6',
        'display': 'flex',
        'justifyContent': 'space-between',
        'alignItems': 'center',
        'width': '100%'
    },
    'sidebar': {
        'width': '220px',
        'backgroundColor': '#343a40',
        'color': '#fff',
        'padding': '10px',
        'transition': 'transform 0.3s ease-in-out',
        'overflowY': 'auto',
        'height': '100%'  # Ensure sidebar takes full height
    },
    'sidebar_dark_mode': {
        'width': '220px',
        'backgroundColor': '#1e1e1e',
        'color': '#fff',
        'padding': '10px',
        'transition': 'transform 0.3s ease-in-out',
        'overflowY': 'auto',
        'height': '100%'  # Ensure sidebar takes full height
    },
    'content_area': {
        'flexGrow': '1',
        'padding': '20px',
        'overflowY': 'auto',
        'display': 'flex',
        'flexDirection': 'column',
        'transition': 'margin-left 0.3s ease-in-out',
        'width': '100%'  # Ensure content area takes full width
    },
    'search_results': {
        'marginTop': '20px'
    },
    'button': {
        'backgroundColor': '#007bff',
        'color': '#fff',
        'border': 'none',
        'padding': '10px 20px',
        'cursor': 'pointer',
        'margin': '0 5px',  # Adjust margin for proper spacing
        'minWidth': '120px',  # Ensure fixed width for buttons
        'textAlign': 'center'
    },
    'input': {
        'marginRight': '10px'  # Ensure spacing between input and buttons
    },
    'footer': {
        'backgroundColor': '#f8f9fa',
        'padding': '10px',
        'borderTop': '1px solid #dee2e6',
        'textAlign': 'center',
        'width': '100%'
    },
    'card': {
        'backgroundColor': '#ffffff',
        'padding': '20px',
        'margin': '10px 0',
        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
        'borderRadius': '5px',
        'width': '100%'  # Ensure card takes full width of the container
    },
    'dark_mode_card': {
        'backgroundColor': '#424242',
        'color': '#ffffff',
        'padding': '20px',
        'margin': '10px 0',
        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
        'borderRadius': '5px',
        'width': '100%'  # Ensure card takes full width of the container
    }
}

def apply_dark_mode(style):
    dark_style = style.copy()
    dark_style['backgroundColor'] = '#1e1e1e'
    dark_style['color'] = '#ffffff'
    
    if 'borderColor' in dark_style:
        dark_style['borderColor'] = '#495057'
    
    if 'boxShadow' in dark_style:
        dark_style['boxShadow'] = '0 2px 4px rgba(255, 255, 255, 0.1)'
    
    return dark_style
