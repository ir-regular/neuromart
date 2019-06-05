# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html


def set_layout(dash_app):
    dash_app.layout = html.Div(children=[
        dcc.Upload(
            id='upload-file',
            children=[html.Button('Upload File')]
        ),
        html.Div(id='output-graphs'),
    ])
