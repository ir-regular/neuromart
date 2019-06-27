# -*- coding: utf-8 -*-
"""App layout

Gluing together static components (graphs, tables, interactive) into layouts.
Covers presentation concerns (layout, margins, padding), and explanatory text.
"""

import dash_bootstrap_components as dbc
import dash_html_components as html

from neuromart import tables
from neuromart import graphs
from neuromart import interactive


def set_layout(dash_app):
    dash_app.layout = html.Div([navbar(), body()])


def navbar():
    return dbc.NavbarSimple(
        id="navbar",
        brand="neuromaRt",
        brand_href="#",
        sticky="top",
        color="primary",
        dark=True)


def body():
    return dbc.Container(
        id="app-content",
        children=[upload_box()])


def upload_box(error=None):
    return dbc.Jumbotron([
        html.H1("neuromaRt: learn more about the brain"),
        html.P(className="lead",
               children="Please provide a CSV file in an accepted format (TBC) for analysis."),
        interactive.upload_csv()
        # TODO: a checkbox for enabling bootstrap
    ])


def gene_expression_comparison_results(var_x, var_y, xs, r, p):
    left_col_width = 6
    return [
        dbc.Row([
            dbc.Col([
                html.P(
                    """\
A table listing PLS components and the data from variables VarX, VarY, Pval output by the attached code.
"""
                ),
                tables.pls_component_list(var_x, var_y),
                html.Div([interactive.download_var_x(),
                          interactive.download_var_y(),
                          interactive.download_pval()],
                         className="d-flex justify-content-end")],
                md=left_col_width,
            ),
            dbc.Col([
                html.P("A plot of VarY vs numbers 1:10"),
                graphs.var_y_per_pls_components(var_y)]
            )],
            style={"margin-top": "1em"}),
        dbc.Row([
            dbc.Col([
                html.P(
                    """\
    A table showing the R and p-values from correlating each PLS component with the input map.
    """
                ),
                tables.pls_r_p(r, p),
                html.Div([interactive.download_r(), interactive.download_p()],
                         className="d-flex justify-content-end")],
                md=left_col_width
            ),
            dbc.Col([
                html.P("A plot of PLS1 vs PLS2"),
                graphs.pls1_vs_pls2(xs)
            ])],
            style={"margin-top": "1em"})]
