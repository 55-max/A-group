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
    songs_dict[i] = {'artist': playlist_tracks['items'][i]['track']['artists'][0]['name'], 
                     'title': playlist_tracks['items'][i]['track']['name'], 
                     'artist_id': playlist_tracks['items'][i]['track']['artists'][0]['id'],
                     'track_id': playlist_tracks['items'][i]['track']['id']}

songs_df = pd.DataFrame(songs_dict).T
songs_df
# %%
seed_artists = ['2IUl3m1H1EQ7QfNbNWvgru']
seed_tracks = ['1YXot2MLAG9sttepCtBRM7']
results = spotify.recommendations(seed_artists=seed_artists, seed_tracks=seed_tracks, limit=75)
print(results)
# %%
recommended_songs_dict = {}
for i in range(len(results['tracks'])):
    recommended_songs_dict[i] = {'artist': results['tracks'][i]['artists'][0]['name'], 
                                 'title': results['tracks'][i]['name'], 
                                 'artist_id': results['tracks'][i]['artists'][0]['id'],
                                 'track_id': results['tracks'][i]['id']}
    
recommended_songs_df = pd.DataFrame(recommended_songs_dict).T
recommended_songs_df

# %%

pd.DataFrame(recommended_songs_df.sample(n=3).iloc[0]).T
# %%

import ytmusicapi
youtube = ytmusicapi.YTMusic()
# youtubeのurlに変換する。
youtube_music_url_list = []
for i in range(len(recommended_songs_df)):
    artist, name = recommended_songs_df.iloc[i]['artist'], recommended_songs_df.iloc[i]['title']
    print('now searching:', artist, name)
    search_results = youtube.search(f'{artist} {name}', filter='songs')[0]['videoId']
    video_url = f'https://youtu.be/{search_results}'
    youtube_music_url_list.append(video_url)

#%%

import subprocess

youtube_music_url = youtube_music_url_list[0]
cmd = f'yt-dlp -x --audio-format mp3 --audio-quality 0 {youtube_music_url}'
subprocess.run(cmd, shell=True)


#%%


import pafy
import vlc

playurl = "https://www.youtube.com/watch?v=c7-Dt-BnVVI"
# video = pafy.new(url)
# best = video.getbest()
# playurl = best.url


Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()