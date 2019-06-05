# -*- coding: utf-8 -*-
from flask import Flask
from dash import Dash


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config:
        app.config.from_mapping(test_config)

    configure_dash(app)

    return app


def configure_dash(app):
    from layout import set_layout
    from callbacks import register_callbacks

    dash_app = Dash(__name__, server=app)
    set_layout(dash_app)
    register_callbacks(dash_app)
