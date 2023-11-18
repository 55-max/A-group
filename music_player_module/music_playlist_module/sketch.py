#%%
import pandas as pd

df = pd.read_csv('../../playlist_urls.csv')
df
df['url'].tolist()
pd.read_csv('../../player_data_03_22.csv/player_data_03_22.csv')['Player']

#%%

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

with open('../../spotify_client_info.json') as f:
    data = json.load(f)
    client_id = data['client_id']
    client_secret = data['client_secret']

client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_url = 'https://open.spotify.com/playlist/37i9dQZF1DX9ww9tisjowN'
playlist = spotify.playlist(playlist_url)
playlist_tracks = playlist['tracks']
playlist_tracks_items = playlist_tracks['items']
playlist_tracks_items_df = pd.DataFrame(playlist_tracks_items)
playlist_tracks_items_df = playlist_tracks_items_df['track']
playlist_tracks_items_df = pd.DataFrame(playlist_tracks_items_df)

# %%


pd.DataFrame(playlist_tracks['items'])

# track. artistの名前と、曲のタイトルが欲しい

# playlist_tracks['items'][0]['track']['artists'][0]['name']
# playlist_tracks['items'][0]['track']['name']

# これを、pd.DataFrameにする。

# %%

songs_dict = {}
for i in range(len(playlist_tracks_items)):
    songs_dict[i] = {'artist': playlist_tracks['items'][i]['track']['artists'][0]['name'], 'title': playlist_tracks['items'][i]['track']['name']}

songs_df = pd.DataFrame(songs_dict).T
songs_df