import sys
sys.path.append("E:\\Trackify")
from songObject import Song
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime

# Spotify API-Authentifizierung
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='5ea1e5eb32b441489d9b078cb4ed40f4',
                                               client_secret='deb42a044f4741ce96ed56f934994e7a',
                                               redirect_uri='http://localhost:8888/callback',
                                               scope='user-read-playback-state user-read-currently-playing'))

def is_playing():
    current_playback = sp.current_playback()
    is_playing = current_playback['is_playing']
    if is_playing != True and is_playing != False:
        return -1
    return is_playing
    #if sp.current_playback()['is_playing'] == None:
    #   return -1
    #return sp.current_playback()['is_playing']

def get_current_song():
    current_track = sp.current_playback()
    if current_track and current_track.get('item'):
        song_name = current_track['item']['name']
        artists = current_track['item']['artists']
        artist_names = ', '.join([artist['name'] for artist in artists])
        album_name = current_track['item']['album']['name']
        song_length_ms = current_track['item']['duration_ms']
        song_length_seconds = song_length_ms / 1000
        date = datetime.datetime.now().strftime("%d-%m-%Y")
        time = datetime.datetime.now().strftime("%H:%M:%S")
        
        # Überprüfen, ob die Wiedergabe gerade pausiert ist oder spielt
        # is_playing = current_track['is_playing']

        return Song(song_name, artist_names, album_name, date, time, song_length_seconds)
    else:
        return -1



