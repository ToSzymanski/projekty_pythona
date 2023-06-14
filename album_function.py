#definicja funkcji do tworzenia słownika z danymi albumu
def make_album(band, artist, album_title, track_nb=None):
    """zwraca słownik z informacją o albumie muzycznym"""
    album_dictionary = {'nazwa_albumu': album_title, 'band_name': band, 'artist_name': artist, 'liczba_utworów': track_nb}
    return album_dictionary

#pytanie uzytkownika o dane albumu
while True:
    print("\nProszę podaj dane ulubinego albumu\nJeśli chcesz zakończyć wpisz 'q'")
    n_album = input('Nazwa albumu: ')
    if n_album == "q":
        break
    n_artysty = input('Nazwa artysty: ')
    if n_artysty == "q":
        break
    n_zespol = input('Nazwa zespołu: ')
    if n_zespol == "q":
        break
    n_track = input('Ilość utworów: ')
    if n_track == "q":
        break


#zwrot informacji o zebranych danych
album = make_album(n_zespol, n_artysty, n_album, n_track)
print(album)