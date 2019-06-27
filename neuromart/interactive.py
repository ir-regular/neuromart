# -*- coding: utf-8 -*-
"""Interactive app components

App components that a user can interact with to trigger app state change
(see callbacks.)
"""

import dash_bootstrap_components as dbc
import dash_core_components as dcc


def upload_csv():
    mime_types = [
        "text/plain", "text/csv", "text/x-csv", "application/vnd.ms-excel",
        "application/csv", "application/x-csv", "text/comma-separated-values",
        "text/x-comma-separated-values", "text/tab-separated-values"]

    return dcc.Upload(
        id='upload-file',
        children=[dbc.Button("Select a file", color="danger")],
        accept=", ".join(mime_types))


def download_var_x():
    return dbc.Button("Download VarX.csv", color="warning", className="m-1")


def download_var_y():
    return dbc.Button("Download VarY.csv", color="warning", className="m-1")


def download_pval():
    pass  # return dbc.Button("Download Pval", color="warning", className="m-1")


def download_r():
    return dbc.Button("Download R.csv", color="warning", className="m-1")


def download_p():
    return dbc.Button("Download P.csv", color="warning", className="m-1")
