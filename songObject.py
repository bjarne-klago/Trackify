class Song:
    def __init__(self, song_name, artist, album, date, time, song_length_s):
        self._song_name = song_name
        self._artist = artist
        self._album = album
        self._song_length_s = song_length_s
        self._date = date
        self._time = time

    def get_songname(self):
        return self._song_name

    def set_songname(self, song_name):
        self._song_name = song_name

    def get_artist(self):
        return self._artist

    def set_artist(self, artist):
        self._artist = artist

    def get_album(self):
        return self._album

    def set_album(self, album):
        self._album = album

    def get_song_length_s(self):
        return self._song_length_s
    
    def set_song_length_s(self, song_length_s):
        self._song_length_s = song_length_s
    
    def get_date(self):
        return self._date
    
    def set_date(self, date):
        self._date = date
    
    def get_time(self):
        return self._time
    
    def set_time(self, time):
        self._time = time