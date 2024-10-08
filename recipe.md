# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Playlist:
    # User-facing properties:
    #   name: string

    def __init__(self):

        self.playlist = {}

    def add(self, artist, trackname):
        self.artist = artist
        self.track = trackname
        self.playlist.setdefault(artist,[]).append(trackname)

    def list_all(self):
        output_list = []
        for artist, tracks in self.playlist.items():
            for track in tracks:
                output_list.append(f"{track} by {artist}")

        return ", ".join(output_list)


```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

```python
# EXAMPLE

"""
given a track and artist, data is stored within the class
"""
playlist = Playlist()
playlist.add("Pink Floyd","time")
assert playlist.playlist == {"Pink Floyd":["time"]}


"""
given a track and artist, list_All returns formatted string
"""
playlist = Playlist()
playlist.add("Pink Floyd","time")
playlist.add("Pink Floyd", "comfortably numb")
playlist.add("Rage", "Killing in the name")
assert playlist.list_all() == "time by Pink FLoyd, comfortably numb by Pink Floyd, Killing in the name by Rage"
"""

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
