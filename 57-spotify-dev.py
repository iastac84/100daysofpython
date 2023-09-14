#!/usr/bin/env python3
# Day 57

'''
Python script to interact with Spotify's API, allowing you to perform various actions like retrieving user data, searching for tracks, creating playlists, and more. To do this, you will need to use the Spotify API, which requires authentication through OAuth 2.0.

To run
export SPOTIFY_CLIENT_ID='your_client_id_here'
export SPOTIFY_CLIENT_SECRET='your_client_secret_here'
Generate these credentials from developer.spotify.com

Unfortunately, you cannot use the spotipy library to directly play a song on the user's Spotify account. The spotipy library primarily provides access to Spotify's Web API for retrieving information about tracks, albums, artists, and playlists, as well as managing user playlists and library.

Playing songs on a user's Spotify account typically requires the Spotify mobile or desktop application, and it cannot be controlled programmatically using the Spotify API. The Spotify API does not offer direct control over playback on a user's device.
'''

import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Read client_id and client_secret from environment variables
client_id = os.environ.get('SPOTIFY_CLIENT_ID')
client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')

if not client_id or not client_secret:
    raise ValueError("SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET environment variables are not set.")

# Create a Spotify client with authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri='http://localhost:3000',
                                               scope = 'user-read-playback-state user-library-read playlist-read-private'))


# Example: Search for tracks
#results = sp.search(q='track:Weapon artist:Fatboy Slim', type='track')
results = sp.search(q='track:Got artist:chemical brothers', type='track')
#results = sp.search(q='track:yellow artist:*', type='track')
for track in results['tracks']['items']:
    print(f"{track['name']} by {track['artists'][0]['name']}")

