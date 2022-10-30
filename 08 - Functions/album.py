import string

def make_album(artist, title, total_tracks=None):
    """Return a dictionary containing album information."""
    album = {"artist": string.capwords(artist), 
             "title": string.capwords(title)} 
    if total_tracks:
        album['total_tracks'] = total_tracks
    return album

print(make_album("celine dion", "let's talk about love", total_tracks=16))
print(make_album("celine dion", "d'eux", total_tracks=16))