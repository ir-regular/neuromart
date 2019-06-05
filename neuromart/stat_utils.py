# -*- coding: utf-8 -*-
import numpy as np
from pandas import notna
from scipy.stats import zscore, pearsonr


def clean_rows_index(parcel_expression):
    # Indices of rows that do not contain NaN values
    return np.all(notna(parcel_expression), axis=1)


def standardise(data, clean_row_index):
    return zscore(data[clean_row_index])


def center(data):
    mean_row = np.mean(a=data, axis=0, dtype=np.float64, keepdims=True)
    return np.subtract(data, mean_row)


def explained_variance_pct(x, x_loadings):
    x0 = center(x)
    return np.divide(
        np.sum(np.square(np.abs(x_loadings)), 0),
        np.sum(np.sum(np.square(np.abs(x0)), 0))
    )


def pearson_corr_coef(x, y):
    shape = x.shape[1], y.shape[1]
    r = np.zeros(shape, dtype=np.float64)
    p = np.zeros(shape, dtype=np.float64)
    for i, c1 in enumerate(x.T):
        for j, c2 in enumerate(y.T):
            r[i, j], p[i, j] = pearsonr(c1, c2)
    return r, p
