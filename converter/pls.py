import numpy as np
import pandas as pd
from scipy import stats


def remove_nan(parcel_expression, user_input):
    # Indices of rows that do not contain NaN values
    clean_rows = np.all(pd.notna(parcel_expression), axis=1)
    return parcel_expression[clean_rows], user_input[clean_rows]


if __name__ == "__main__":
    import os
    from pathlib import Path
    os.chdir(Path(__file__).parent.parent)

    pe = np.load('resources/parcel_expression.npy')
    scan = np.loadtxt('test/data/expected_upload.csv', delimiter=',')
    pe, scan = remove_nan(pe, scan)

    x = stats.zscore(pe)
    y = stats.zscore(scan)
