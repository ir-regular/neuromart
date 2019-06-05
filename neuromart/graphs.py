# -*- coding: utf-8 -*-
import dash_core_components as dcc
import plotly.graph_objs as go


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
