import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

name = 'Twice'

results = sp.search(q= name)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])
    
features = sp.audio_analysis('5qSoW3ewNlhRN3FNZPmVns')
print(features)