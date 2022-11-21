import string

def make_album(artist, title, total_tracks=None):
    """Return a dictionary containing album information."""
    album = {"artist": string.capwords(artist), 
             "title": string.capwords(title)} 
    if total_tracks:
        album['total_tracks'] = total_tracks
    return album

while True:
    print("\n--- Music Album Database ---")
    print("(enter 'x' at any time to exit)")

    artist = input("Enter the artist name: ")
    if artist == 'x':
        break

    title = input("Enter the album title: ")
    if title == 'x':
        break

    n_tracks = int(input("Enter the the number of track: "))
    if n_tracks == 'x':
        break

    print(make_album(artist, title, n_tracks))

    cont = input("Continue? (yes/no): ")
    if cont == 'yes':
        continue
    if cont == 'no':
        break