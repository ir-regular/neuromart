# -*- coding: utf-8 -*-
from base64 import b64decode
from io import StringIO

from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import numpy as np

from neuromart import gene_expression
from neuromart import layout


def register_callbacks(dash_app):
    @dash_app.callback(Output('output-graphs', 'children'),
                       [Input('upload-file', 'contents')],
                       [State('upload-file', 'filename')])
    def update_output(contents, filename):
        if contents is None:
            return []

        data = parse_dash_upload(contents, filename)

        if data is None:
            return [dbc.Alert("Uploaded file is formatted in an unsupported way: please provide a CSV file",
                              color="danger")]

        var_x, var_y, xs, r, p = gene_expression.compare(data)

        return layout.gene_expression_comparison_results(var_x, var_y, xs, r, p)


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
