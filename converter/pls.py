import numpy as np
from pandas import notna
from scipy.stats import zscore, pearsonr
from sklearn.cross_decomposition import PLSRegression


def clean_rows_index(parcel_expression):
    # Indices of rows that do not contain NaN values
    return np.all(notna(parcel_expression), axis=1)


def standardise(data, clean_row_index):
    return zscore(data[clean_row_index])


def center(data):
    mean_row = np.mean(a=data, axis=0, dtype=np.float64, keepdims=True)
    return np.subtract(data, mean_row)


def explained_variance_pct(X, Xloadings):
    X0 = center(X)
    # sum(abs(Xloadings).^2,1) ./ sum(sum(abs(X0).^2,1))
    return np.divide(
        np.sum(np.square(np.abs(Xloadings)), 0),
        np.sum(np.sum(np.square(np.abs(X0)), 0))
    )


def pearson_corr_coef(x, y):
    shape = x.shape[1], y.shape[1]
    R = np.zeros(shape, dtype=np.float64)
    p = np.zeros(shape, dtype=np.float64)
    for i,c1 in enumerate(x.T):
        for j,c2 in enumerate(y.T):
            R[i, j], p[i, j] = pearsonr(c1, c2)
    return R, p


if __name__ == "__main__":
    import os
    from pathlib import Path
    os.chdir(Path(__file__).parent.parent)

    pe = np.load('resources/parcel_expression.npy')
    scan = np.loadtxt('test/data/expected_upload.csv', delimiter=',')

    index = clean_rows_index(pe)
    X = standardise(pe, index)
    Y = standardise(scan, index)

    n_components = min(X.shape[0] - 1, X.shape[1])

    # ...but note that the result is going to be slightly different from Matlab b/c different algorithm used:
    # https://stackoverflow.com/questions/48070346/why-the-result-is-different-between-matlab-and-scikit-learn-when-using-pls-regre?noredirect=1&lq=1
    pls = PLSRegression(n_components=n_components)

    # [XL,YL,XS,YS,BETA,PCTVAR,MSE,stats]
    # ignore: BETA, MSE, XL, YL, YS
    # stats: for bootstrap
    # XS, PCTVAR: used for normal output (and bootstrap)
    pls.fit(X, Y)

    XVar = explained_variance_pct(X, pls.x_loadings_)  # PCTVAR(1)
    YVar = explained_variance_pct(Y, pls.y_loadings_)  # PCTVAR(2)

    # np.savetxt(fname='test/output/VarX.csv', X=XVar, delimiter=',')
    # np.savetxt(fname='test/output/VarY.csv', X=YVar, delimiter=',')

    XS = pls.x_scores_

    R, p = pearson_corr_coef(XS[:, 0:5], Y)

    # np.savetxt(fname='test/output/R.csv', X=R, delimiter=',')
    # np.savetxt(fname='test/output/P.csv', X=p, delimiter=',')
