# -*- coding: utf-8 -*-
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd


def pls_component_list(var_x, var_y):
    rank = list(range(1, 6))
    pls_component = ["PLS" + str(i) for i in rank]

    df = pd.DataFrame({
        "Rank": rank,
        "PLS component": pls_component,
        "% variance expl in X": var_x[:5],
        "% variance expl in Y": var_y[:5],
        # TODO: "P-value for PLS"
    })

    table = dbc.Table.from_dataframe(df, striped=True)
    body = table.children[1]
    body.children.append(html.Tr([
        html.Td(colSpan=2),
        html.Td(dbc.Button("Download VarX.csv", color="secondary")),
        html.Td(dbc.Button("Download VarY.csv", color="secondary")),
        # TODO: html.Td(dbc.Button("Download Pval", color="secondary")),
    ]))
    return table

