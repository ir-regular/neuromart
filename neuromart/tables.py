# -*- coding: utf-8 -*-
from dash_table import DataTable


def pls_component_list(var_x, var_y, p):
    data = [{'rank': i + 1,
             'pls-comp': "PLS" + str(i + 1),
             'var-x': var_x[i],
             'var-y': var_y[i],
             'p-val': str(p[i, 0]) + " " + str(p[i, 1])}  # TODO: probably wrong value; confirm
            for i in range(0, 5)]

    columns = {'rank': 'Rank',
               'pls-comp': 'PLS comp',
               'var-x': '% variance expl in X',
               'var-y': '% variance expl in Y',
               'p-val': 'P-value for PLS'}

    columns = [{"id": col_id, "name": name} for col_id, name in columns.items()]

    return DataTable(
        id='table',
        columns=columns,
        data=data,
    )
