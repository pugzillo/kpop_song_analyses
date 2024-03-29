import sys
import spotipy
import os
import time
import numpy as np
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

# spotify credentials
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# open the file and read the contents-List of artists to find discography
f = open("Data/pudding_boybands_since2000.csv")
lines = f.readlines()[1:] # don't read in header
results = []
for x in lines:
    results.append(x.split(',')[0])

f.close()

failed_searches = [] 

## Get discography for each artists
for name in results: 
        print("Attempting search for " + str(name))
        # result = sp.search(q='artist:%s genre:k-pop' % name) #search query for kpop
        result = sp.search(q='artist:%s' % name)

        # failed searches, stop them if query is not found on spotify
        if not result['tracks']['items']:
                failed_searches.append(name)
                continue

        # extract the Artist's uri (spotify artist ID)
        uri = result['tracks']['items'][0]['artists'][0]['uri']

        # pull all of the artist's albums
        sp_albums = sp.artist_albums(uri)

        # #Store artist's albums' names' and uris 
        album_names = []
        album_uris = []
        
        for i in range(len(sp_albums['items'])):
                album_names.append(sp_albums['items'][i]['name'])
                album_uris.append(sp_albums['items'][i]['uri'])

        spotify_albums = {}

        # function to get song from album
        def albumSongs(uri):
                album = uri #assign album uri to an artist
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

        for i in album_uris: #pulls all songs from each album
                albumSongs(i)
                print("Album " + str(album_names[album_count]) + " songs has been added to spotify_albums.")
                album_count+=1 #Updates album count once every track on the album has been added

        # function to get audio features per song
        def audio_features(album):
        #Add new key-values to store audio features
                def add_key_vals(prop):
                        spotify_albums[album][prop] = []
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
                        'popularity'  
                ]:
                        add_key_vals(prop)

                #track counter
                track_count = 0
                for track in spotify_albums[album]['uri']:
                        #audio features per track
                        features = sp.audio_features(track)
                        
                        #Append to relevant key-value
                        def append_song_features(spotify_albums, album, features, prop):
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
                                append_song_features(spotify_albums, album, features, prop)

                        pop = sp.track(track)
                        spotify_albums[album]['popularity'].append(pop['popularity']) # popularity is not stored in prop
                        track_count+=1

        # time the api requests
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
        def make_dictionary(prop):
                dic_df[prop] = []
        
        for prop in [
                'album',
                'track_number',
                'id',
                'name',
                'uri',
                'acousticness',
                'danceability',
                'energy',
                'instrumentalness',
                'liveness',
                'loudness',
                'speechiness',
                'tempo',
                'valence',
                'popularity'
        ]:
                make_dictionary(prop)
        
        for album in spotify_albums: 
                for feature in spotify_albums[album]:
                        dic_df[feature].extend(spotify_albums[album][feature])
                
        df = pd.DataFrame.from_dict(dic_df)

        final_df = df.sort_values('popularity', ascending=False).drop_duplicates('name').sort_index()

        # print out file with song information for the artist
        final_df.to_csv('%s_SongInfo.csv' % name)


failed_search_df = pd.DataFrame(failed_searches) 
failed_search_df.to_csv('Failed_Searches_westernboybands.csv') #file with the failed queries