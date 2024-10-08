from lib.playlist import *


def test_add_artist_and_song_stored_in_dictionary():
    playlist = Playlist()
    assert isinstance(playlist, Playlist)
    
    
def test_add_artist_and_song_stored_in_dictionary():
    playlist = Playlist()
    playlist.add("Pink Floyd","time")
    assert playlist.playlist == {"Pink Floyd":["time"]}



def test_list_all_returns_formatted_string():
    playlist = Playlist()
    playlist.add("Pink Floyd","time")
    playlist.add("Pink Floyd", "comfortably numb")
    playlist.add("Rage", "Killing in the name")
    assert playlist.list_all() == "time by Pink Floyd, comfortably numb by Pink Floyd, Killing in the name by Rage"
