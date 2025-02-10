import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from application.layouts import layout
app = dash.Dash(__name__)
app.layout = layout


if __name__ == '__main__':
    app.run_server(debug=True)