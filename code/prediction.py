import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split

import classification
import preprocessing
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler

def RFC_Predict(name_song, name_artist):
    dataframe = pd.read_csv('../dataset/spotify_features.csv')
    dataframe = preprocessing.preprocessing_for_classification(dataframe)
    features = ["acousticness", "danceability", "duration_ms", "energy", "instrumentalness", "key", "liveness",
                "mode", "speechiness", "tempo", "time_signature", "valence"]

    row = dataframe.loc[(dataframe['track_name'] == name_song) & (dataframe['artist_name'] == name_artist)]
    print(row)

    # Destiniamo l'80% del dataset per il training set.
    training = dataframe.sample(frac=0.8, random_state=420)
    X_train = training[features]
    y_train = training['popularity']
    X_test = dataframe.drop(training.index)[features]

    # Il restante 20% per il test set.
    X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=0.2, random_state=420)
    RFC_Model = RandomForestClassifier()
    RFC_Model.fit(X_train, y_train)

    row = row.drop(['track_id', 'track_name', 'artist_name', 'loudness', 'genre', 'popularity'], axis=1)
    print(row)
    Popularity_Predict = RFC_Model.predict(row)
    if  Popularity_Predict.all() == 0:
        print("La canzone non e' popolare")
    else:
        print("La canzone e' popolare")

RFC_Predict("C'est beau de faire un Show", 'Henri Salvador')

    #rf = random_forest_classification(training, target)

    #genre_predict = rf.predict([row_user])

    #final_val = [key for key, val in genre_dictionary.items() if val == genre_predict[0]]

    #print(f"Il genere dell'anime {name} e': ", final_val[0])