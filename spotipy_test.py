import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

name = 'Red Velvet'

results = sp.search(q= name)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])