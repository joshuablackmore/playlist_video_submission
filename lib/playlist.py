class Playlist:
    # User-facing properties:
    #   name: string

    def __init__(self):

        self.playlist = {}

    def add(self, artist, trackname):
        self.playlist.setdefault(artist,[]).append(trackname)

    def list_all(self):
        output_list = []
        for artist, tracks in self.playlist.items():
            for track in tracks:
                output_list.append(f"{track} by {artist}")

        return ", ".join(output_list)