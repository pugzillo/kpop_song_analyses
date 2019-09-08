import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Print all of the seed genres on spotify
# print(sp.recommendation_genre_seeds())

# print(sp.recommendations(seed_genres='k-pop', limit=20))

results = sp.search(q='k-pop', type='artist', limit=20)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])