import pandas as pd


def clean_query(csv):
    df = pd.read_csv(csv, header=None)
    for i in range(len(df)):
        if df[9][i][0] != '#':
            df[9][i] = None
    df[9][0] = 'query'

    return df
