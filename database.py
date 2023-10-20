import sqlite3
from songObject import Song
import datetime

class SongDatabase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                songname TEXT,
                artist TEXT,
                album TEXT, 
                date TEXT,
                time TEXT,
                length_in_seconds INT
            )
        ''')
        self.conn.commit()

    def insert_song(self, song):
        self.cursor.execute('''
            INSERT INTO songs (songname, artist, album, date, time, length_in_seconds)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (song.get_songname(), song.get_artist(), song.get_album(), str(song.get_date()), str(song.get_time()), song.get_song_length_s()))
        self.conn.commit()

    def get_all_songs(self):
        self.cursor.execute('SELECT * FROM songs')
        return self.cursor.fetchall()

    def get_all_songs_as_song_object(self) -> Song:
        self.cursor.execute('SELECT * FROM songs')
        all_songs = self.cursor.fetchall()

        all_songs_as_object = [] 
        for song in all_songs:
            song_object = Song(song[1], song[2], song[3], song[4], song[5], song[6])
            all_songs_as_object.append(song_object)
        return all_songs_as_object

    def close(self):
        self.conn.close()
