import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from application.layouts import layout
from module.callback import register_callbacks
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,prevent_initial_callbacks="initial_duplicate",external_stylesheets=[dbc.themes.CYBORG])
app.layout = layout
register_callbacks(app)


if __name__ == '__main__':
    app.run_server(debug=False)