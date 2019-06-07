# -*- coding: utf-8 -*-
from dash import Dash
import dash_bootstrap_components as dbc
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config:
        app.config.from_mapping(test_config)

    configure_dash(app)

    return app


def configure_dash(app):
    from neuromart.callbacks import register_callbacks
    from neuromart.layout import set_layout

    dash_app = Dash(__name__, server=app, external_stylesheets=[dbc.themes.FLATLY])
    set_layout(dash_app)
    register_callbacks(dash_app)
