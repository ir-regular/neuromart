# -*- coding: utf-8 -*-
from dash import Dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from io import StringIO
from numpy import genfromtxt


def plot_pls1_vs_pls2(XS):
    return dcc.Graph(
        id='pls1-vs-pls2-graph',
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


def create_app(test_config=None):
    app = Dash(__name__)
    app.layout = html.Div(children=[
        dcc.Upload(
            id='upload-csv',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select CSV File')
            ]),
            multiple=False
        ),
        html.Div(id='output-graphs'),
    ])

    @app.callback(Output('output-graphs', 'children'),
                  [Input('upload-csv', 'contents')])
    def update_output(list_of_contents):
        if list_of_contents is not None:
            return [html.Div('BLAH BLAH BLAH')]
        #     return [html.Div(len(c)) for c in list_of_contents]
            # XS = genfromtxt(StringIO(list_of_contents[0]), delimiter=',')
            # return [plot_pls1_vs_pls2(genfromtxt(XS))]

    return app.server
