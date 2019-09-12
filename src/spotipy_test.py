import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# name = "LOONA"
# results = sp.search(q='artist:%s genre:k-pop' % name)
# print(results)
# for i, t in enumerate(results['tracks']['items']):
#     print(' ', i, t['name'])


results = sp.search(q='artist:fromis_9 genre:k-pop')
print(results)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])
    
# features = sp.audio_analysis('5qSoW3ewNlhRN3FNZPmVns')
# print(features)


# # open the file and read the contents
# f = open("List_of_KpopGroups_Wiki_Sept7_2019.csv")
# lines = f.readlines()[1:]
# results = []
# for x in lines:
#     results.append(x.split(',')[0])

# f.close()
# print(results)