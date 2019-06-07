# -*- coding: utf-8 -*-
import dash_core_components as dcc
import numpy as np
import plotly.graph_objs as go


def var_y_per_pls_components(var_y):
    data = np.cumsum(np.multiply(100, var_y[0:10]))

    return dcc.Graph(
        id='var-y-graph',
        figure={
            'data': [
                go.Scatter(x=list(range(1, 11)), y=data)
            ],
            'layout': go.Layout(
                xaxis={'title': 'Number of PLS components'},
                yaxis={'title': 'Percent Variance Explained in Y'}
            )
        }
    )


def pls1_vs_pls2(xs):
    pls1 = xs[:, 0]
    pls2 = xs[:, 1]

    return dcc.Graph(
        id='pls1-vs-pls2-graph',
        figure={
            'data': [
                go.Scatter(x=pls1, y=pls2, mode='markers')
            ],
            'layout': go.Layout(
                xaxis={'title': 'PLS component 1'},
                yaxis={'title': 'PLS component 2'}
            )
        }
    )
