import sys
import spotipy
import os
import time
import numpy as np
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# open the file and read the contents-List of artists
f = open("List_of_KpopGroups_Wiki_Sept7_2019_v2.csv")
lines = f.readlines()[1:]
results = []
for x in lines:
    results.append(x.split(',')[0])

f.close()
# print(results)

failed_searches = []

for i in results: 
        name = i #chosen artist
        print(name)
        result = sp.search(q='artist:%s genre:k-pop' % name) #search query
        # print(result['tracks']['items'])
        
        # failed searches, stop them
        if not result['tracks']['items']:
                failed_searches.append(name)
                continue


        # extract the Artist's uri
        uri = result['tracks']['items'][0]['artists'][0]['uri']

        # pull all of the artist's albums
        sp_albums = sp.artist_albums(uri)
        # print(sp_albums)

        # #Store artist's albums' names' and uris in separate lists
        album_names = []
        album_uris = []
        
        for i in range(len(sp_albums['items'])):
                album_names.append(sp_albums['items'][i]['name'])
                album_uris.append(sp_albums['items'][i]['uri'])
        
        # print(album_names)
        album_uris
        #Keep names and uris in same order to keep track of duplicate albums

        spotify_albums = {}

        def albumSongs(uri):
                album = uri #assign album uri to a_name
                spotify_albums[album] = {} #Creates dictionary for that specific album
                ## Create keys-values of empty lists inside nested dictionary for album
                spotify_albums[album]['album'] = [] #create empty list
                spotify_albums[album]['track_number'] = []
                spotify_albums[album]['id'] = []
                spotify_albums[album]['name'] = []
                spotify_albums[album]['uri'] = []
                tracks = sp.album_tracks(album) #pull data on album tracks

                for n in range(len(tracks['items'])): #for each song track
                        spotify_albums[album]['album'].append(album_names[album_count]) #append album name tracked via album_count
                        spotify_albums[album]['track_number'].append(tracks['items'][n]['track_number'])
                        spotify_albums[album]['id'].append(tracks['items'][n]['id'])
                        spotify_albums[album]['name'].append(tracks['items'][n]['name'])
                        spotify_albums[album]['uri'].append(tracks['items'][n]['uri'])


        album_count = 0

        for i in album_uris: #each album
                albumSongs(i)
                print("Album " + str(album_names[album_count]) + " songs has been added to spotify_albums dictionary")
                album_count+=1 #Updates album count once all tracks have been added

        def audio_features(album):
        #Add new key-values to store audio features
                spotify_albums[album]['acousticness'] = []
                spotify_albums[album]['danceability'] = []
                spotify_albums[album]['energy'] = []
                spotify_albums[album]['instrumentalness'] = []
                spotify_albums[album]['liveness'] = []
                spotify_albums[album]['loudness'] = []
                spotify_albums[album]['speechiness'] = []
                spotify_albums[album]['tempo'] = []
                spotify_albums[album]['valence'] = []
                spotify_albums[album]['popularity'] = []
                #create a track counter
                track_count = 0
                for track in spotify_albums[album]['uri']:
                        #pull audio features per track
                        features = sp.audio_features(track)
                        
                        #Append to relevant key-value
                        def foo(spotify_albums, album, features, prop):
                                if features is None or features[0] is None:
                                        spotify_albums[album][prop].append("NA")
                                else:
                                        if prop in features[0]:
                                                spotify_albums[album][prop].append(features[0][prop])
                        for prop in [
                                'acousticness',
                                'danceability',
                                'energy',
                                'instrumentalness',
                                'liveness',
                                'loudness',
                                'speechiness',
                                'tempo',
                                'valence',
                        ]:
                                foo(spotify_albums, album, features, prop)
                        # if 'acousticness' if features[0]:
                        #         spotify_albums[album]['acousticness'].append(features[0]['acousticness'])
                        # # spotify_albums[album]['acousticness'].append(features[0]['acousticness']) if features[0]['acousticness'] else next
                        # spotify_albums[album]['danceability'].append(features[0]['danceability'])
                        # spotify_albums[album]['energy'].append(features[0]['energy'])
                        # spotify_albums[album]['instrumentalness'].append(features[0]['instrumentalness'])
                        # spotify_albums[album]['liveness'].append(features[0]['liveness'])
                        # spotify_albums[album]['loudness'].append(features[0]['loudness'])
                        # spotify_albums[album]['speechiness'].append(features[0]['speechiness'])
                        # spotify_albums[album]['tempo'].append(features[0]['tempo'])
                        # spotify_albums[album]['valence'].append(features[0]['valence'])
                        #popularity is stored elsewhere
                        pop = sp.track(track)
                        spotify_albums[album]['popularity'].append(pop['popularity'])
                        track_count+=1


        sleep_min = 2
        sleep_max = 5
        start_time = time.time()
        request_count = 0
        for i in spotify_albums:
                audio_features(i)
                request_count+=1
                if request_count % 5 == 0:
                        print(str(request_count) + " playlists completed")
                        time.sleep(np.random.uniform(sleep_min, sleep_max))
                        print('Loop #: {}'.format(request_count))
                        print('Elapsed Time: {} seconds'.format(time.time() - start_time))

        dic_df = {}
        dic_df['album'] = []
        dic_df['track_number'] = []
        dic_df['id'] = []
        dic_df['name'] = []
        dic_df['uri'] = []
        dic_df['acousticness'] = []
        dic_df['danceability'] = []
        dic_df['energy'] = []
        dic_df['instrumentalness'] = []
        dic_df['liveness'] = []
        dic_df['loudness'] = []
        dic_df['speechiness'] = []
        dic_df['tempo'] = []
        dic_df['valence'] = []
        dic_df['popularity'] = []
        
        for album in spotify_albums: 
                for feature in spotify_albums[album]:
                        dic_df[feature].extend(spotify_albums[album][feature])
                
        len(dic_df['album'])   

        # print(dic_df)
        df = pd.DataFrame.from_dict(dic_df)
        # df

        # print(len(df))
        final_df = df.sort_values('popularity', ascending=False).drop_duplicates('name').sort_index()
        # print(len(final_df))

        final_df.to_csv('%s_SongInfo.csv' % name)

        
print("Failed Searches: " + ' '.join(failed_searches))