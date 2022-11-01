import pandas as pd

from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler

pd.options.mode.chained_assignment = None  # default='warn'


def preprocessing_for_classification(dataframe):
    # Per la feature "Key" convertiamo le 12 chiavi in un numeri, utilizzando l'indice.
    list_of_keys = dataframe['key'].unique()
    for i in range(len(list_of_keys)):
        dataframe.loc[dataframe['key'] == list_of_keys[i], 'key'] = i

    # Per la feature "Mode" convertiamo le Major in 1 e Minor in 0.
    dataframe.loc[dataframe["mode"] == 'Major', "mode"] = 1
    dataframe.loc[dataframe["mode"] == 'Minor', "mode"] = 0

    # Per la feature "time_signature" convertiamo i battiti in numeri, utilizzando l'indice.
    list_of_time_signatures = dataframe['time_signature'].unique()
    for i in range(len(list_of_time_signatures)):
        dataframe.loc[dataframe['time_signature'] == list_of_time_signatures[i], 'time_signature'] = i

    # Per la feature "popularity" la rendiamo una binaria, dove una canzone é popolare se ha
    # uno score maggiore o uguale a 75. Non é popolare altrimenti.
    dataframe.loc[dataframe['popularity'] < 75, 'popularity'] = 0
    dataframe.loc[dataframe['popularity'] >= 75, 'popularity'] = 1

    return dataframe
