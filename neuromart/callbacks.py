# -*- coding: utf-8 -*-
import dash_html_components as html
from dash.dependencies import Input, Output, State
from base64 import b64decode
from io import StringIO
import numpy as np

import tables
import graphs
from gene_expression import compare


def register_callbacks(dash_app):
    @dash_app.callback(Output('output-graphs', 'children'),
                       [Input('upload-file', 'contents')],
                       [State('upload-file', 'filename')])
    def update_output(contents, filename):
        if contents is None:
            return []

        data = parse_dash_upload(contents, filename)

        if data is None:
            return [html.Div("Uploaded file is formatted in an unsupported way: please provide a CSV file")]

        var_x, var_y, xs, r, p = compare(data)

        return [
            tables.pls_component_list(var_x, var_y, p),
            graphs.var_y_per_pls_components(var_y),
            graphs.pls1_vs_pls2(xs)
        ]


def parse_dash_upload(contents, filename):
    _, content_string = contents.split(',')
    _, encoding = _.split(';')
    _, content_type = _.split(':')

    if content_type == "text/csv" or filename.lower().endswith(".csv"):
        content_string = b64decode(content_string).decode('utf-8')
        return np.genfromtxt(StringIO(content_string), delimiter=',')

    '''
    TODO: at some point it may be also useful to parse into a pandas dataframe
    for use in dash_table, like so:

    df = pd.read_csv(StringIO(content_string), header=None)
    data = df.to_dict('records')
    dash_table.DataTable(
        data=data,
        columns=[{'name': i, 'id': i} for i in df.columns]
    )
    '''

    return None
