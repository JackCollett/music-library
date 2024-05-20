from lib.albums import Album

"""
When I construct an Album
with the fields title, release_year, artist_id
They are reflected in the instance properties
"""
def test_album_constructs():
    album = Album("Test Title", "1966", 1)
    assert album.title == "Test Title"
    assert album.release_year == "1966"
    assert album.artist_id == 1

'''
When I construct two albums with the same fields
They are equal
'''
def test_equality():
    album_1 = Album("Test Title", "1966", 1)
    album_2 = Album("Test Title", "1966", 1)
    assert album_1 == album_2

'''
When i construct an album
and format it to a string
it come out in a friendly format
'''
def test_formatting():
    album_1 = Album("Test Title", "1966", 1)
    assert str(album_1) == "Album(Test Title, 1966, 1)" 

