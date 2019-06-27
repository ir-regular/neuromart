# -*- coding: utf-8 -*-
"""App callbacks

How the app reacts to user interactions (see neuromart.interactive for input
sources and neuromart.layout for output targets.)
"""

from base64 import b64decode
from io import StringIO

from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_html_components as html
import numpy as np

from neuromart import gene_expression
from neuromart import layout


def register_callbacks(dash_app):
    @dash_app.callback(Output('app-content', 'children'),
                       [Input('upload-file', 'contents')],
                       [State('upload-file', 'filename')])
    def update_output(contents, filename):
        if contents is None:
            return layout.upload_box()

        data = parse_dash_upload(contents, filename)

        if data is None:
            return layout.upload_box(error="The file is not in a supported format")

        var_x, var_y, xs, r, p = gene_expression.compare(data)

        return [dbc.Row([html.H2("Source: " + filename)])] \
               + layout.gene_expression_comparison_results(var_x, var_y, xs, r, p)


def parse_dash_upload(contents, filename):
    _, content_string = contents.split(',')
    _, encoding = _.split(';')
    _, content_type = _.split(':')

    if content_type == "text/csv" or filename.lower().endswith(".csv"):
        content_string = b64decode(content_string).decode('utf-8')
        return np.genfromtxt(StringIO(content_string), delimiter=',')

    '''
    TODO: at some point it may be also useful to parse into a pandas dataframe
    '''

    return None
