import pandas as pd
import preprocessing
import graphics
import clustering
import functions
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler


def main():
    graphics.print_logo()
    bol = False
    while True:
        if bol:
            graphics.print_menu()

        else:
            graphics.print_welcome_menu()
        response = input()

        if response == '1':

            graphics.song_request()
            track_name = input()
            graphics.artist_request()
            artist_name = input()
            graphics.number_request()
            n_song = int(input())

            data = pd.read_csv('../dataset/spotify_features.csv')

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

            df = clustering.clustering(pd.DataFrame, songs)
            functions.playlist_song(track_name, artist_name, songs, n_song + 1)

        elif response == '3':
            graphics.print_goodbye()
            break

        """elif response == '2':

            print("Ti chiedero' un po' di cose. Inziamo...")

            name = input("Qual è il nome dell'anime che vuoi classificare?\n ").lower()

            score = input("Qual è lo score dell'anime che vuoi classificare?\n").lower()

            type_ = input(
                "Qual è il type dell'anime che vuoi classificare?(se non sai cos'è il tipo digita 1)\n").lower()

            while type_ == '1':
                print("Quando parliamo di tipo intendiamo se l'anime appartiene a una di queste categorie:\n" +
                      "- TV      : l'anime viene trasmesso ad episodi\n" +
                      "- Movie   : l'anime è un film\n" +
                      "- ONA/OVA : l'anime è una puntata speciale di un anime o originale\n")

                type_ = input(
                    "Quindi, qual è il type dell'anime che vuoi classificare?(se non sai cos'è il tipo digita 1)\n").lower()

            episodes = input("Quanti episodi ha l'anime che vuoi classificare?\n").lower()

            duration = input("Quanto dura mediamente un episodio dell'anime che vuoi classificare?\n").lower()

            producers = input("Qual è il produttore dell'anime che vuoi classificare?\n").lower()

            studios = input("Qual è lo studio dell'anime che vuoi classificare?\n").lower()

            source = input("Qual è l'origine dell'anime che vuoi classificare?" +
                           " (se non sai cos'è l'origine di un anime tipo digita 1)\n").lower()

            while source == '1':
                print("Quando parliamo di origine intendiamo se l'anime appartiene a una di queste categorie:\n" +
                      "- Manga\n- Novel\n- Book \n- Radio\n- Picture book\n- Web Manga\n- Digital Manga\n- Original\n")

                source = input("Quindi, qual è l'origine dell'anime che vuoi classificare?(se non sai cos'è l'origine "
                               "digita 1)\n").lower()

            prediction_genre.predict_genre(name, score, type_, episodes, duration, producers, studios, source)
            print("\n")
            os.system("pause")
            bol = True
            print("\n\n")
        """



if __name__ == '__main__':
    main()
