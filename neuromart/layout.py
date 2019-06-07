# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from neuromart import tables
from neuromart import graphs


def set_layout(dash_app):
    # dash_app.layout = html.Div(children=[
    #     dcc.Upload(
    #         id='upload-file',
    #         children=[html.Button('Upload File')]
    #     ),
    #     html.Div(id='output-graphs'),
    # ])
    dash_app.layout = html.Div([navbar(), body()])


def navbar():
    return dbc.NavbarSimple(
        # TODO: links to downloads etc
        # children=[
        #     dbc.NavItem(dbc.NavLink("Link", href="#")),
        #     dbc.DropdownMenu(
        #         nav=True,
        #         in_navbar=True,
        #         label="Menu",
        #         children=[
        #             dbc.DropdownMenuItem("Entry 1"),
        #             dbc.DropdownMenuItem("Entry 2"),
        #             dbc.DropdownMenuItem(divider=True),
        #             dbc.DropdownMenuItem("Entry 3"),
        #         ],
        #     ),
        # ],
        brand="neuromaRt",
        brand_href="#",
        sticky="top",
    )


def body():
    return dbc.Container([
        dbc.Row([upload_csv()]),
        dbc.Row(id='output-graphs')
    ])


def upload_csv():
    return dcc.Upload(
        id='upload-file',
        children=[dbc.Button("Upload Scan (CSV)", color="secondary")]
    )


def gene_expression_comparison_results(var_x, var_y, xs, r, p):
    return [
        dbc.Col(
            [
                html.H2("Summary"),
                html.P(
                    """\
A table listing PLS components and the data from variables VarX, VarY, Pval output by the attached code.
"""
                ),
                tables.pls_component_list(var_x, var_y),
                html.P(
                    """\
A table showing the R and p-values from correlating each PLS component with the input map.
"""
                ),
                tables.pls_r_p(r, p),
            ],
            md=6,
        ),
        dbc.Col(
            [
                html.H2("Graph"),
                html.P("A plot of VarY vs numbers 1:10"),
                graphs.var_y_per_pls_components(var_y),
                html.P("A plot of PLS1 vs PLS2"),
                graphs.pls1_vs_pls2(xs)
            ]
        ),
    ]
