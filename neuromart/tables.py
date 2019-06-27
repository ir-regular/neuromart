# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc
import pandas as pd


def pls_component_list(var_x, var_y):
    rank = list(range(1, 6))
    pls_component = ["PLS" + str(i) for i in rank]
    var_x_formatted = ['{:.2f}'.format(var_x[i]) for i in range(5)]
    var_y_formatted = ['{:.2f}'.format(var_y[i]) for i in range(5)]

    df = pd.DataFrame({
        "Rank": rank,
        "PLS component": pls_component,
        "% variance expl in X": var_x_formatted,
        "% variance expl in Y": var_y_formatted,
        # TODO: "P-value for PLS"
    })

    return dbc.Table.from_dataframe(df, striped=True)


def pls_r_p(r, p):
    # TODO: both r and p have two columns, is it correct that I'm selecting the second column?
    r_column = ['{:.2f}'.format(r[i, 1]) for i in range(0, 5)]
    p_column = ['{:.2f}'.format(p[i, 1]) for i in range(0, 5)]
    df = pd.DataFrame({
        "PLS component": ["PLS" + str(i) for i in range(1, 6)],
        "R": r_column,
        "P": p_column
    })
    return dbc.Table.from_dataframe(df, striped=True)
