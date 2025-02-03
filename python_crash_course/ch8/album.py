def make_album(artist, album_title, num_songs=None):
   album = {
      'artist': artist,
      'album_title': album_title
   }
   if num_songs is not None:
      album['num_songs'] = num_songs
   return album

album1 = make_album('Adele', '30')
album2 = make_album('ed Sheeran', 'Subtract', 14)
album3 = make_album('Taylor Swift', '1989', 13)

print(album1)
print(album2)
print(album3)