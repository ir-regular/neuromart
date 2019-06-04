# -*- coding: utf-8 -*-
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


def create_app(test_config=None):
    from numpy import loadtxt
    XS = loadtxt('test/data/expected_upload.csv', delimiter=',')

    app = Dash(__name__)
    app.layout = html.Div(children=[
        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    go.Scatter(x=XS[:, 0], y=XS[:, 1], mode='markers')
                ],
                'layout': go.Layout(
                    xaxis={'title': 'PLS component 1'},
                    yaxis={'title': 'PLS component 2'}
                )
            }
        )
    ])
    return app.server
