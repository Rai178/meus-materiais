def make_album(artist, album, songs=None):
    if songs:
        dict = {'artist': artist, 'album': album, 'songs': songs}
    else:
        dict = {'artist': artist, 'album': album}
    return dict

while True:
    print('\nTell me an album name and an artist, if you know how many songs this album have, tell me too')
    print("(enter 'q' at any time to quit)")

    album = input("album name: ")
    if album == 'q':
        break

    artist = input("artist name: ")
    if artist == 'q':
        break

    songs = input("songs: ")
    if songs == 'q':
        break
    elif not songs:
        songs = None
        
    album1 = make_album(album, artist, songs)
    print(album1)
    