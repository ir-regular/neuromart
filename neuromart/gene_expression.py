# -*- coding: utf-8 -*-
import numpy as np
import stat_utils as utils
from sklearn.cross_decomposition import PLSRegression


expression = np.load('resources/parcel_expression.npy')
index = utils.clean_rows_index(expression)
expression = utils.standardise(expression, index)
n_components = min(expression.shape[0] - 1, expression.shape[1])


def compare(converted_brain_map):
    x = expression
    y = utils.standardise(converted_brain_map, index)

    # ...but note that the result is going to be slightly different from Matlab b/c different algorithm used:
    # https://stackoverflow.com/questions/48070346/why-the-result-is-different-between-matlab-and-scikit-learn-when-using-pls-regre?noredirect=1&lq=1
    pls = PLSRegression(n_components=n_components)
    pls.fit(x, y)

    var_x = utils.explained_variance_pct(x, pls.x_loadings_)
    var_y = utils.explained_variance_pct(y, pls.y_loadings_)

    xs = pls.x_scores_

    r, p = utils.pearson_corr_coef(xs[:, 0:5], y)

    return var_x, var_y, xs, r, p
