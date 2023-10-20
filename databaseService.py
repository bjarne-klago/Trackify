import time
import logging
import spotifyAPI
from database import SongDatabase
from songObject import Song
from datetime import datetime, timedelta
from colorlog import ColoredFormatter

class DatabaseService():
    def __init__(self, db_file_name) -> None:
        self._db_file_name = db_file_name

    def run(self):
        log_format = '%(asctime)s - %(levelname)s - %(message)s'
        date_format = '%d-%m-%Y %H:%M:%S'
        database = SongDatabase(self._db_file_name)

        # Erstellen Sie einen ColoredFormatter, um die Textfarbe für INFO-Nachrichten zu ändern
        formatter = ColoredFormatter(
            "%(log_color)s%(asctime)s - %(levelname)s - %(message)s%(reset)s",
            datefmt=date_format,
            log_colors={
                'DEBUG': 'reset',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            }
        )

        # Erstellen Sie einen StreamHandler und verwenden Sie den erstellten ColoredFormatter
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        handler.setFormatter(formatter)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)

        while True:
            database.create_table
            current_song = spotifyAPI.get_current_song()
            
            if current_song == -1:
                logger.info("Spotify is not open")
                time.sleep(5)
            else:
                if spotifyAPI.is_playing() == -1:
                    logger.info("Spotify is not open")
                else:
                    if spotifyAPI.is_playing() :
                        all_songs_from_database = database.get_all_songs_as_song_object()
                        if len(all_songs_from_database) > 0:
                            last_song = all_songs_from_database[len(all_songs_from_database) - 1]
                            current_song = spotifyAPI.get_current_song()
                            if last_song.get_songname() == current_song.get_songname(): 
                                time_format = "%H:%M:%S"
                                last_song_time = datetime.strptime(last_song.get_time(), time_format)
                                current_song_time = datetime.strptime(current_song.get_time(), time_format)
                                time_difference = abs(last_song_time - current_song_time)
                                if last_song.get_date() == current_song.get_date() and time_difference >= timedelta(seconds=current_song.get_song_length_s()): #implement date request. for this, songobject added that it has attribute date and time
                                    logger.info(f"\nSong: {current_song.get_songname()}\nArtist/s: {current_song.get_artist()}\nAlbum: {current_song.get_album()}\nLänge in Sekunden: {current_song.get_song_length_s()}")
                                    database.insert_song(current_song)
                            else:
                                logger.info(f"\nSong: {current_song.get_songname()}\nArtist/s: {current_song.get_artist()}\nAlbum: {current_song.get_album()}\nLänge in Sekunden: {current_song.get_song_length_s()}")
                                database.insert_song(current_song)
                        else:
                            logger.info(f"\nSong: {current_song.get_songname()}\nArtist/s: {current_song.get_artist()}\nAlbum: {current_song.get_album()}\nLänge in Sekunden: {current_song.get_song_length_s()}")
                            database.insert_song(current_song)
                    else:
                        logger.info("Spotify is open, but not playing")

            time.sleep(10)



