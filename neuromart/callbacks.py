# -*- coding: utf-8 -*-
"""App callbacks

How the app reacts to user interactions (see neuromart.interactive for input
sources and neuromart.layout for output targets.)
"""

from base64 import b64decode
from io import StringIO

from dash.dependencies import Input, Output, State
import numpy as np

from neuromart import gene_expression
from neuromart import layout


def register_callbacks(dash_app):
    @dash_app.callback(Output('app-content', 'children'),
                       [Input('upload-another', 'n_clicks'),
                        Input('upload-file', 'contents')],
                       [State('upload-file', 'filename')])
    def update_content(uploads_requested, contents, filename):
        display_upload = True
        upload_error = None
        var_x = var_y = xs = r = p = None

        if contents is not None:
            data = parse_dash_upload(contents, filename)

            if data is None:
                upload_error = "The file is not in a supported format"
            else:
                display_upload = False
                var_x, var_y, xs, r, p = gene_expression.compare(data)

        return [layout.upload_page(error=upload_error, display=display_upload),
                layout.results_page(filename, var_x, var_y, xs, r, p)]


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
