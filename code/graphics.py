from termcolor import colored


def print_logo():
    print(colored(" _____  _             _ _     _\n"
                  + "|  __ \| |           | (_)   | |\n"
                  + "| |__) | | __ _ _   _| |_ ___| |_\n"
                  + "|  ___/| |/ _` | | | | | / __| __|     Matteo Esposito\n"
                  + "| |    | | (_| | |_| | | \__ \ |_      Giuseppe Galgano\n"
                  + "|_|___ |_|\__,_|\__, |_|_|___/\__|                       _\n"
                  + "|  __ \          __/ |                                  | |\n"
                  + "| |__) |___  ___|___/ _ __ ___  _ __ ___   ___ _ __   __| | ___ _ __\n"
                  + "|  _  // _ \/ __/ _ \| '_ ` _ \| '_ ` _ \ / _ \ '_ \ / _` |/ _ \ '__|\n"
                  + "| | \ \  __/ (_| (_) | | | | | | | | | | |  __/ | | | (_| |  __/ |\n"
                  + "|_|  \_\___|\___\___/|_| |_| |_|_| |_| |_|\___|_| |_|\__,_|\___|_|\n", "green"))


def print_welcome_menu():
    print(colored("Ciao, benvenuto nel sistema di raccomandazione di Playlist basato sulle canzoni di Spotify!\n"
                  + "Vuoi che ti suggerisca una playlist? - Premi 1\n" \
                  + "Vuoi sapere se una canzone è popolare? - Premi 2\n" \
                  + "Vuoi uscire? - Premi 3", "green"))


def print_menu():
    print(colored("Vuoi che ti suggerisca una playlist? - Premi 1\n" \
                  + "Vuoi sapere se una canzone è popolare? - Premi 2\n" \
                  + "Vuoi uscire? - Premi 3", "green"))


def print_goodbye():
    print(colored("Arrivederci!", "green"))


def song_request():
    print(colored("Adesso dovrai suggerirmi su quale canzone basare la tua playlist!\n" \
                  + "Qual'é il nome di una traccia che hai apprezzato?", "green"))


def song_request_for_prediction():
    print(colored("Adesso dovrai suggerirmi la canzone su cui predire la popolaritá!\n" \
                  + "Qual'é il nome della traccia?", "green"))


def artist_request():
    print(colored("Adesso dimmi il nome dell'artista che ha scritto la traccia.", "green"))


def number_request():
    print(colored("Quante canzoni vuoi inserire nella tua playlist?", "green"))


def no_song_matched():
    print(colored("Nessuna canzone trovata nel dataset!", "green"))


def song_mathced():
    print(colored("Canzone trovata nel dataset!", "green"))


def choose_classifier():
    print(colored("Quale classificatore vuoi utilizzare?\n"
                  + "Random Forest Classifier - Premi 1\n" \
                  + "K-Nearest Neighbors Classifier - Premi 2\n" \
                  + "Decision Tree Classifier - Premi 3\n" \
                  + "Logistic Regression - Premi 4\n", "green"))


def song_is_popular():
    print(colored("La canzone é popolare!", "green"))


def song_not_popular():
    print(colored("La canzone é popolare!", "green"))
