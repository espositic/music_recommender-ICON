import pandas as pd
import clustering
import functions

from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler

pd.options.mode.chained_assignment = None  # default='warn'


def preprocessing(data):
    """Rimuoviamo le feature "key" e "time_signature",
       e trasferiamo track_name e artist_name in un'altra tabella."""
    indx = data[['track_name', 'artist_name']]
    attributes = data.drop(['track_id', 'time_signature', 'track_name', 'artist_name', 'key'], axis=1)

    """Trasformiamo i valori genre e mode in valori binari,
       aggiungendo ogni tipologia di genere alle feature, in modo
       che ogni canzone abbia 1 al proprio genere."""
    ordinal_encoder = OrdinalEncoder()
    object_cols = ['mode']
    attributes[object_cols] = ordinal_encoder.fit_transform(attributes[object_cols])

    attributes = pd.get_dummies(attributes)
    attributes.insert(loc=0, column='track_name', value=indx.track_name)
    attributes.insert(loc=1, column='artist_name', value=indx.artist_name)

    genres_names = ['genre_A Capella', 'genre_Alternative', 'genre_Anime', 'genre_Blues',
                    "genre_Children's Music", "genre_Children’s Music", 'genre_Classical',
                    'genre_Comedy', 'genre_Country', 'genre_Dance', 'genre_Electronic',
                    'genre_Folk', 'genre_Hip-Hop', 'genre_Indie', 'genre_Jazz',
                    'genre_Movie', 'genre_Opera', 'genre_Pop', 'genre_R&B', 'genre_Rap',
                    'genre_Reggae', 'genre_Reggaeton', 'genre_Rock', 'genre_Ska',
                    'genre_Soul', 'genre_Soundtrack', 'genre_World']

    genres = attributes.groupby(['track_name', 'artist_name'])[genres_names].sum()

    column_names = ['track_name', 'artist_name']
    for i in genres_names:
        column_names.append(i)

    genres.reset_index(inplace=True)
    genres.columns = column_names

    attributes = attributes.drop(genres_names, axis=1)

    atts_cols = attributes.drop(['track_name', 'artist_name'], axis=1).columns
    scaler = StandardScaler()
    attributes[atts_cols] = scaler.fit_transform(attributes[atts_cols])

    songs = pd.merge(genres, attributes, how='inner', on=['track_name', "artist_name"])
    songs = songs.drop_duplicates(['track_name', 'artist_name']).reset_index(drop=True)

    DF = clustering.clustering(pd.DataFrame, songs)


# print(functions.playlist_song('Without Me', 'Eminem', songs, 10))
