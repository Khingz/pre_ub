from flask import Blueprint
from v1.spotify import SpotifyAPI
import os


spotify = Blueprint('spotifyAPI', __name__)

client_id = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_CLIENT_ID']
spotify_api = SpotifyAPI(client_id=client_id, client_secret=client_secret)


@spotify.route('/playlist/<playlist_id>')