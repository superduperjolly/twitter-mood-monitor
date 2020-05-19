"""The main dash app with the HTML components"""

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from tw_mood_monitor import viz_tools

# Import an external stylesheet sourced from: http://dash.plotly.com/layout
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Create the app
web_app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Design the app
web_app.layout = html.Div(children=[
    # Website header
    html.H1(children="Hello World!"),

    # Dropdown select
    html.Div([
        dcc.Dropdown(
            id="hashtag-selected",
            options=[
                {"label": hashtag, "value": hashtag}
                for hashtag in viz_tools.get_hashtags()
            ])
        ]),

    # Selection info
    html.Div(id="picker-output")
    ])


@web_app.callback(
    Output("picker-output", "children"),
    [Input("hashtag-selected", "value")]
)
def update_option(value):
    return f"You have chosed {value}"
