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
    return dbc.Container(id="app-content",
                         children=[upload_page(), results_page()])


def upload_page(error=None, display=True):
    upload_hidden = None if display else 'hidden'
    test_upload_url = "https://raw.githubusercontent.com/ir-regular/neuromart/master/test/data/expected_upload.csv"

    return html.Div(
        id="upload-page",
        hidden=upload_hidden,
        children=dbc.Jumbotron(
            children=[
                html.H1("neuromaRt: learn more about the brain"),
                html.P(className="lead",
                       children="Please provide a CSV file in an accepted format (TBC) for analysis."),
                html.P(["For testing purposes, feel free to use ",
                        html.A("this test file", href=test_upload_url)]),
                interactive.upload_csv()
                # TODO: a checkbox for enabling bootstrap
            ],
            className="mt-5"))


def results_page(filename=None, var_x=None, var_y=None, xs=None, r=None, p=None):
    left_col_width = 6

    if all(var is None for var in [filename, var_x, var_y, xs, r, p]):
        results_hidden = 'hidden'
        pls_component_list = var_y_per_pls = pls_r_p = pls1_vs_pls2 = None
    else:
        results_hidden = None
        pls_component_list = tables.pls_component_list(var_x, var_y)
        var_y_per_pls = graphs.var_y_per_pls_components(var_y)
        pls_r_p = tables.pls_r_p(r, p)
        pls1_vs_pls2 = graphs.pls1_vs_pls2(xs)

    return html.Div(
        id="results-page",
        hidden=results_hidden,
        children=[
            dbc.Alert([html.Span(["Source: ", html.Samp(filename)]), interactive.show_upload_screen()],
                      color="light",
                      className="d-flex justify-content-between align-items-center mt-3 mb-3"),
            dbc.Row([
                dbc.Col([
                    html.P("A table listing PLS components and the data from variables VarX, VarY, Pval output",
                           "by the attached code."),
                    html.Div(id="pls-component-list-container", children=pls_component_list),
                    html.Div([interactive.download_var_x(),
                              interactive.download_var_y(),
                              interactive.download_pval()],
                             className="d-flex justify-content-end")],
                    md=left_col_width,
                ),
                dbc.Col([
                    html.P("A plot of VarY vs numbers 1:10"),
                    html.Div(id="var-y-per-pls-container", children=var_y_per_pls)]
                )],
                style={"margin-top": "1em"}),
            dbc.Row([
                dbc.Col([
                    html.P("A table showing the R and p-values from correlating each PLS component",
                           "with the input map."),
                    html.Div(id="pls-r-p-container", children=pls_r_p),
                    html.Div([interactive.download_r(), interactive.download_p()],
                             className="d-flex justify-content-end")],
                    md=left_col_width
                ),
                dbc.Col([
                    html.P("A plot of PLS1 vs PLS2"),
                    html.Div(id="pls1-vs-pls2-container", children=pls1_vs_pls2)
                ])],
                style={"margin-top": "1em"})])
