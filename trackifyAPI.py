from flask import Flask, jsonify
from flask_cors import CORS
from database import SongDatabase
from collections import Counter

app = Flask(__name__)
CORS(app) 
db_file_name = "trackify_db.sqlite3"

@app.route('/trackify/get-all-songs', methods=['GET'])
def get_all_songs():
    return jsonify({'songs': SongDatabase(db_file_name).get_all_songs()})


@app.route('/trackify/get-all-songs/as-song-object', methods=['GET'])
def get_all_songs_as_song_object():
    all_songs_as_object = SongDatabase(db_file_name).get_all_songs_as_song_object()
    return jsonify({'songs': songs_to_dict_list(all_songs_as_object)}), 200

# @app.route('/trackify/get_most_played_song', method=['GET'])
# def get

def song_to_dict(song):
    return {
            'song_name': song.get_songname(),
            'artist': song.get_artist(),
            'album': song.get_album(),
            'song_length_s': song.get_song_length_s()
        }

def songs_to_dict_list(songs):
    all_songs_to_dict_as_list = []    
    for song in songs:
        all_songs_to_dict_as_list.append(song_to_dict(song))
    return all_songs_to_dict_as_list

def most_played_song(all_sons_as_object):
    if not all_sons_as_object:
        return None, 0
    
    song_count = Counter([song.get_songname() for song in all_sons_as_object])
    most_common_song = song_count.most_common(1)[0]

    return most_common_song[0], most_played_song[1]