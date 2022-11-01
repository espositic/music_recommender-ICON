import pandas as pd
import preprocessing
import graphics
import clustering
import functions


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
            data_frame, songs = preprocessing.preprocessing_for_clustering(data)

            df = clustering.clustering(data_frame, songs)
            functions.playlist_song(track_name, artist_name, songs, n_song + 1)

        elif response == '2':
            print("Ti chiedero' un po' di cose. Inziamo...")

            name = input("Qual è il nome della canzone?\n")

            artist = input("Qual è il nome dell'artista della canzone che hai scelto?\n")

            data = pd.read_csv('../dataset/spotify_features.csv')
            row = data.loc[(data['track_name'] == name) & (data['artist_name'] == artist)]
            if row.empty:
                print("Nessuna canzone trovata nel dataset!")
            else:
                print("Canzone trovata nel dataset!")

            print("\n")
            bol = True
            print("\n\n")

        elif response == '3':
            graphics.print_goodbye()
            break


if __name__ == '__main__':
    main()
