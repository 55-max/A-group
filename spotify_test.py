CLIENT_INFO_JSON_PATH = 'spotify_client_info.json'
PLAYLIST_URLS_PATH = 'playlist_urls.csv'
SONGS_NUM = 10


import json
import random
import spotipy
import ytmusicapi
import subprocess
import pandas as pd
import shutil
import os
import pprint


with open(CLIENT_INFO_JSON_PATH) as f:
    data = json.load(f)
    client_id = data['client_id']
    client_secret = data['client_secret']

client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
youtube = ytmusicapi.YTMusic()

if __name__ == '__main__':
    # artist, title = 'The Beatles', 'Yesterday'
    artist, title = 'Vaundy', '東京Flash'
    result = spotify.search(q=f'artist: {artist} track: {title}', type='track')
    # pprint.pprint(result)

    pprint.pprint(result['tracks']['items'][0]['artists'][0]['id'])

    pprint.pprint(result['tracks']['items'][0]['id'])