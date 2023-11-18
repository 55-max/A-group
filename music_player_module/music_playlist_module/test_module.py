import pandas as pd
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import ytmusicapi
import subprocess

CLIENT_INFO_JSON_PATH = './spotify_client_info.json'

# client_id = 'XXXXXXXXXXXXXXXX' # App作成時のCliend ID
# client_secret = 'XXXXXXXXXXXXXXXX' # App作成時のCliend Secret

with open(CLIENT_INFO_JSON_PATH) as f:
    data = json.load(f)
    client_id = data['client_id']
    client_secret = data['client_secret']

client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

youtube_headers_file = "your_youtube_headers_file"
youtube = ytmusicapi.YTMusic(youtube_headers_file)

PLAYLIST_URLS_PATH = 'playlist_urls.csv'
class music_player_module:

    def __init__(self) -> None:
        self.playlist1 = None # pd.DataFrame()
        self.playlist2 = None # pd.DataFrame()
        self.playlist3 = None # pd.DataFrame()
        self.list_of_playlists = {'1': self.playlist1, '2': self.playlist2, '3': self.playlist3}
        self.playlist_url = None
        self.playlist_urls = pd.read_csv(PLAYLIST_URLS_PATH)['url'].tolist()
        self.playlist_metadates = None
        self.random_3_songs = None
        pass

    def select_playlist(self):
        playlist_url = self.playlist_urls[random.randint(0, len(self.playlist_urls)-1)]
        self.playlist_url = playlist_url

    def get_songs_metadate_from_playlist(self):
        assert self.playlist_url is not None, 'Playlist URL is not set'

        def get_DataFrame_from_playlist_url(playlist_url) -> pd.DataFrame:
            playlist = spotify.playlist(playlist_url)
            playlist_tracks = playlist['tracks']
            playlist_tracks_items = playlist_tracks['items']
            playlist_tracks_items_df = pd.DataFrame(playlist_tracks_items)
            playlist_tracks_items_df = playlist_tracks_items_df['track']
            playlist_tracks_items_df = pd.DataFrame(playlist_tracks_items_df)
            playlist_tracks_items_df = playlist_tracks_items_df['id']
            return playlist_tracks_items_df
    
        self.playlist_metadates = get_DataFrame_from_playlist_url(self.playlist_url)

    def get_random_3_songs(self):
        assert self.playlist_metadates is not None, 'Playlist metadates is not set'

        def get_random_3_songs_from_playlist_metadates(playlist_metadates) -> list:
            random_3_songs = playlist_metadates.sample(n=3)
            return random_3_songs

        self.random_3_songs = get_random_3_songs_from_playlist_metadates(self.playlist_metadates)

    def make_3playlist(self):
        assert self.random_3_songs is not None, 'Random 3 songs is not set'

        def make_playlist_from_song(song_data: pd.DataFrame) -> pd.DataFrame:
            # playlist_df = pd.DataFrame()
            return playlist_df
        

        for i in range(3):
            song_data = self.random_3_songs.iloc[i]
            playlist_df = make_playlist_from_song(song_data)
            self.list_of_playlists[str(i+1)] = playlist_df

    def download_songs(self):
        assert self.list_of_playlists is not None, 'List of playlists is not set'

        def make_dir_for_playlist(playlist_num: int):
            pass

        def download_song_from_playlist(playlist_df: pd.DataFrame):

            def get_youtube_music_url_list(playlist_df: pd.DataFrame) -> list:
                youtube_music_url_list = []
                for song_id in playlist_df:
                    spotify_track_info = spotify.track(song_id)
                    spotify_track_title = spotify_track_info["name"]
                    spotify_track_artist = spotify_track_info["artists"][0]["name"]
                    youtube_music_url = youtube.search(f'{spotify_track_title} {spotify_track_artist}', filter="songs")[0]['videoId']
                    youtube_music_url_list.append(youtube_music_url)
                return youtube_music_url_list
            
            def download_songs_from_youtube_music_url_list(youtube_music_url_list: list):
                for youtube_music_url in youtube_music_url_list:
                    cmd = f'yt-dlp -x --audio-format mp3 --audio-quality 0 https://www.youtube.com/watch?v={youtube_music_url}'
                    subprocess.call(cmd, shell=True)
                    

            youtube_music_url_list = get_youtube_music_url_list(playlist_df)
            download_songs_from_youtube_music_url_list(youtube_music_url_list)

        for i in range(3):
            make_dir_for_playlist(i+1)
            playlist_df = self.list_of_playlists[str(i+1)]
            download_song_from_playlist(playlist_df)

        

if __name__ == '__main__':
    music_selector = music_player_module.music_selector()
    music_selector.select_playlist()

    quit()
    music_selector.get_songs_metadate_from_playlist()
    music_selector.get_random_3_songs()
    music_selector.make_3playlist()
    music_selector.download_songs()
    # music_selector.play_songs()