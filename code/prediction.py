import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

import preprocessing


def rfc_prediction(name_song, name_artist):
    dataframe = pd.read_csv('../dataset/spotify_features.csv')
    dataframe = preprocessing.preprocessing_for_classification(dataframe)
    features = ["acousticness", "danceability", "duration_ms", "energy", "instrumentalness", "key", "liveness",
                "mode", "speechiness", "tempo", "time_signature", "valence"]

    row = dataframe.loc[(dataframe['track_name'] == name_song) & (dataframe['artist_name'] == name_artist)]
    row = row.drop(['track_id', 'track_name', 'artist_name', 'loudness', 'genre', 'popularity'], axis=1)
    print(row)

    # Destiniamo l'80% del dataset per il training set.
    training = dataframe.sample(frac=0.8, random_state=420)
    X_train = training[features]
    y_train = training['popularity']

    # Il restante 20% per il test set.
    X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=0.2, random_state=420)
    rfc_model = RandomForestClassifier()
    rfc_model.fit(X_train, y_train)
    rfc_predict = rfc_model.predict(row)
    if rfc_predict.all() == 0:
        print("La canzone non é popolare.")
    else:
        print("La canzone é popolare.")


def lr_prediction(name_song, name_artist):
    dataframe = pd.read_csv('../dataset/spotify_features.csv')
    dataframe = preprocessing.preprocessing_for_classification(dataframe)
    features = ["acousticness", "danceability", "duration_ms", "energy", "instrumentalness", "key", "liveness",
                "mode", "speechiness", "tempo", "time_signature", "valence"]

    row = dataframe.loc[(dataframe['track_name'] == name_song) & (dataframe['artist_name'] == name_artist)]
    row = row.drop(['track_id', 'track_name', 'artist_name', 'loudness', 'genre', 'popularity'], axis=1)

    # Destiniamo l'80% del dataset per il training set.
    training = dataframe.sample(frac=0.8, random_state=420)
    X_train = training[features]
    y_train = training['popularity']

    # Il restante 20% per il test set.
    X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=0.2, random_state=420)
    lr_model = LogisticRegression()
    lr_model.fit(X_train, y_train)
    lr_predict = lr_model.predict(row)
    if lr_predict.all() == 0:
        print("La canzone non é popolare.")
    else:
        print("La canzone é popolare.")


def knn_prediction(name_song, name_artist):
    dataframe = pd.read_csv('../dataset/spotify_features.csv')
    dataframe = preprocessing.preprocessing_for_classification(dataframe)
    features = ["acousticness", "danceability", "duration_ms", "energy", "instrumentalness", "key", "liveness",
                "mode", "speechiness", "tempo", "time_signature", "valence"]

    row = dataframe.loc[(dataframe['track_name'] == name_song) & (dataframe['artist_name'] == name_artist)]
    row = row.drop(['track_id', 'track_name', 'artist_name', 'loudness', 'genre', 'popularity'], axis=1)

    # Destiniamo l'80% del dataset per il training set.
    training = dataframe.sample(frac=0.8, random_state=420)
    X_train = training[features]
    y_train = training['popularity']

    # Il restante 20% per il test set.
    X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=0.2, random_state=420)

    knn_model = KNeighborsClassifier()
    knn_model.fit(X_train, y_train)
    knn_predict = knn_model.predict(row)
    if knn_predict.all() == 0:
        print("La canzone non é popolare.")
    else:
        print("La canzone é popolare.")


def dt_prediction(name_song, name_artist):
    dataframe = pd.read_csv('../dataset/spotify_features.csv')
    dataframe = preprocessing.preprocessing_for_classification(dataframe)
    features = ["acousticness", "danceability", "duration_ms", "energy", "instrumentalness", "key", "liveness",
                "mode", "speechiness", "tempo", "time_signature", "valence"]

    row = dataframe.loc[(dataframe['track_name'] == name_song) & (dataframe['artist_name'] == name_artist)]
    row = row.drop(['track_id', 'track_name', 'artist_name', 'loudness', 'genre', 'popularity'], axis=1)

    # Destiniamo l'80% del dataset per il training set.
    training = dataframe.sample(frac=0.8, random_state=420)
    X_train = training[features]
    y_train = training['popularity']

    # Il restante 20% per il test set.
    X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=0.2, random_state=420)

    dt_model = DecisionTreeClassifier()
    dt_model.fit(X_train, y_train)
    dt_predict = dt_model.predict(row)
    if dt_predict.all() == 0:
        print("La canzone non é popolare.")
    else:
        print("La canzone é popolare.")


rfc_prediction("C'est beau de faire un Show", 'Henri Salvador')
lr_prediction("C'est beau de faire un Show", 'Henri Salvador')
knn_prediction("C'est beau de faire un Show", 'Henri Salvador')
dt_prediction("C'est beau de faire un Show", 'Henri Salvador')
