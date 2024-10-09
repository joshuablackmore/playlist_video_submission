class Playlist:
    # User-facing properties:
    #   name: string

    def __init__(self):

        self.playlist = {}

    def add(self, trackname, artist="Unknown Artist"):
        if not isinstance(trackname, str) or not isinstance(artist, str):
            raise Exception("Trackname and/or Artist must a string.")
        
        trackname = trackname.strip()
        artist = artist.strip()
        
        if trackname == "":
            raise Exception("Please pass a none empty string.")
        elif artist == "":
            artist = "Unknown Artist"
        
        self.playlist.setdefault(artist,[]).append(trackname)

    def list_all(self):
        output_list = []
        for artist, tracks in self.playlist.items():
            for track in tracks:
                output_list.append(f"{track} by {artist}")

        return ", ".join(output_list)