from lib.playlist import *

import pytest

def test_add_artist_and_song_stored_in_dictionary():
    playlist = Playlist()
    assert isinstance(playlist, Playlist)
    
    
def test_add_artist_and_song_stored_in_dictionary():
    playlist = Playlist()
    playlist.add("time", "Pink Floyd")
    assert playlist.playlist == {"Pink Floyd":["time"]}



def test_list_all_returns_formatted_string():
    playlist = Playlist()
    playlist.add("time", "Pink Floyd")
    playlist.add("comfortably numb", "Pink Floyd")
    playlist.add("Killing in the name", "Rage")
    playlist.add("Suck my kiss")
    assert playlist.list_all() == "time by Pink Floyd, comfortably numb by Pink Floyd, Killing in the name by Rage, Suck my kiss by Unknown Artist"

@pytest.mark.parametrize("bad_inputs", [int,float, None, []])
def test_exception_raised_if_trackname_or_artist_is_not_a_string(bad_inputs):
    playlist = Playlist()
    with pytest.raises(Exception) as e:
        playlist.add(bad_inputs,bad_inputs)
    assert str(e.value) == "Trackname and/or Artist must a string."

def test_add_does_not_except_empty_string():
    playlist = Playlist()
    with pytest.raises(Exception) as e:
        playlist.add("","")
    assert str(e.value) == "Please pass a none empty string."
    
def test_add_cleans_up_dodgy_strings():
    playlist = Playlist()
    playlist.add("  time     ", "  Pink Floyd      ")
    playlist.add(" killing in the name   ","     ")
    
    assert playlist.list_all() == "time by Pink Floyd, killing in the name by Unknown Artist"
    
    