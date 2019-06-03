import numpy as np
import pandas as pd
from scipy import stats


def clean_rows_index(parcel_expression):
    # Indices of rows that do not contain NaN values
    return np.all(pd.notna(parcel_expression), axis=1)


def standardise(data, clean_row_index):
    return stats.zscore(data[clean_row_index])


if __name__ == "__main__":
    import os
    from pathlib import Path
    os.chdir(Path(__file__).parent.parent)

    pe = np.load('resources/parcel_expression.npy')
    scan = np.loadtxt('test/data/expected_upload.csv', delimiter=',')

    index = clean_rows_index(pe)
    pe = standardise(pe, index)
    scan = standardise(scan, index)
