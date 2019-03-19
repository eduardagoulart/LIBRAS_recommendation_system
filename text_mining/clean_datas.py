import pandas as pd


def limpa_query(csv):
    df = pd.read_csv(csv, header=None)
    # print (type(df))
    print (len(df))
    for i in range(len(df)):
        if df[9][i][0] != '#':
            df[9][i] = None
    df[9][0] = 'query'

    return df


limpa_query('video.csv')
