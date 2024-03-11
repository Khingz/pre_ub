#!/usr/bin/env python3
"""
Handles spotify related task
"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyAPI:
    """
    Spotify related function class
    """
    def __init__(self, client_id, client_secret):
        """Initialize spotify client
        """
        client_credentials_manager = SpotifyClientCredentials(client_id=client_id,
                                                              client_secret=client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def fetch_playlist(self, playlist_id):
        """
        Method to fetch playlist
        """
        playlist = self.sp.playlist(playlist_id)
        return playlist