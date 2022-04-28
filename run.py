import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL],
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
app.config.suppress_callback_exceptions = True
