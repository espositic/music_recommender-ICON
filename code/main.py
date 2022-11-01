import pandas as pd
import preprocessing
import graphics
import clustering
import functions
import prediction
import os

def main():
    graphics.print_logo()
    bol = False
    while True:
        if bol:
            graphics.print_menu()

        else:
            graphics.print_welcome_menu()
        response = input()
        # Creazione della playlist in base a nome della canzone e nome dell'artista
        if response == '1':
            # richiesta nome canzone
            graphics.song_request()
            track_name = input()
            # richiesta nome artista
            graphics.artist_request()
            artist_name = input()
            # numero di canzoni da aggiungere alla playlist
            graphics.number_request()
            n_song = int(input())

            data = pd.read_csv('../dataset/spotify_features.csv')
            # Fase di preprocessing
            data_frame, songs = preprocessing.preprocessing_for_clustering(data)
            # Fase di clustering
            df = clustering.clustering(data_frame, songs)
            # Creazione della playlist
            functions.playlist_song(track_name, artist_name, songs, n_song + 1)
            print("\n")
            os.system("pause")
            bol = True
            print("\n")

        # Prediction della popolarità di una canzone
        elif response == '2':
            print("Ti chiedero' un po' di cose. Inziamo...")
            # richiesta nome canzone
            graphics.song_request()
            name = input()
            # richiesta nome artista
            graphics.artist_request()
            artist = input()

            data = pd.read_csv('../dataset/spotify_features.csv')
            # Selezioniamo la riga della canzone selezionata dall'utente
            row = data.loc[(data['track_name'] == name) & (data['artist_name'] == artist)]
            # Controllo dell'esistenza della canzone nel dataset
            if row.empty:
                print("Nessuna canzone trovata nel dataset!")
            else:
                print("Canzone trovata nel dataset!")
                # Scelta del classificatore
                print("Quale classificatore vuoi utilizzare?\n"
                        + "Random Forest - Premi 1\n" \
                        + "KNN - Premi 2\n" \
                        + "Decision Tree - Premi 3\n" \
                        + "Logistic Regression - Premi 4\n")
                scelta = int(input())
                match scelta:
                    case 1:
                        prediction.rfc_prediction(name, artist)
                    case 2:
                        prediction.knn_prediction(name, artist)
                    case 3:
                        prediction.dt_prediction(name, artist)
                    case 4:
                        prediction.lr_prediction(name, artist)

            print("\n")
            os.system("pause")
            bol = True
            print("\n")

        # Uscita dal sistema
        elif response == '3':
            graphics.print_goodbye()
            break


if __name__ == '__main__':
    main()
