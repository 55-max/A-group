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
    
    def select_playlist(self):
        playlist_url = self.playlist_urls[random.randint(0, len(self.playlist_urls)-1)]
        self.playlist_url = playlist_url

    def get_songs_metadate_from_playlist(self):
        assert self.playlist_url is not None, 'Playlist URL is not set'

        def get_DataFrame_from_playlist_url(playlist_url) -> pd.DataFrame:
            playlist = spotify.playlist(playlist_url)
            playlist_tracks = playlist['tracks']
            playlist_tracks_items = playlist_tracks['items']
            songs_dict = {}
            for i in range(len(playlist_tracks_items)):
                songs_dict[i] = {'artist': playlist_tracks['items'][i]['track']['artists'][0]['name'], 
                                 'title': playlist_tracks['items'][i]['track']['name'], 
                                 'artist_id': playlist_tracks['items'][i]['track']['artists'][0]['id'],
                                 'track_id': playlist_tracks['items'][i]['track']['id']}
            songs_df = pd.DataFrame(songs_dict).T
            songs_df
            return songs_df
    
        self.playlist_metadates = get_DataFrame_from_playlist_url(self.playlist_url)

    def get_random_3_songs(self):
        assert self.playlist_metadates is not None, 'Playlist metadates is not set'

        def get_random_3_songs_from_playlist_metadates(playlist_metadates) -> list:
            random_3_songs = playlist_metadates.sample(n=3)
            return random_3_songs

        self.random_3_songs = get_random_3_songs_from_playlist_metadates(self.playlist_metadates)

    def user_select_3_songs(self, user_select_3_songs: list):
        # user_select_3_songs = [['Vaundy','踊り子'], ['Vaundy', '東京Flash'], ['Skrillex', 'Recess']]
        # 上のような形式で、ユーザーが選んだ3曲を受け取る。これをdfにする。そして、artist_idとtrack_idを取得する。

        def get_user_select_3_songs_df(user_select_3_songs: list) -> pd.DataFrame:
            user_select_3_songs_dict = {}
            for i in range(len(user_select_3_songs)):
                artist = user_select_3_songs[i][0]
                title = user_select_3_songs[i][1]
                print(f'now searching {artist} {title}')
                result = spotify.search(q=f'artist: {artist} track: {title}', type='track')
                track_id = result['tracks']['items'][0]['id']
                artist_id = result['tracks']['items'][0]['artists'][0]['id']
                user_select_3_songs_dict[i] = {'artist': user_select_3_songs[i][0], 
                                                'title': user_select_3_songs[i][1],
                                                'track_id': track_id,
                                                'artist_id': artist_id}
            user_select_3_songs_df = pd.DataFrame(user_select_3_songs_dict).T
            return user_select_3_songs_df
        
        self.random_3_songs = get_user_select_3_songs_df(user_select_3_songs)

    def make_3playlist(self):
        assert self.random_3_songs is not None, 'Random 3 songs is not set'

        def make_playlist_from_song(song_data: pd.DataFrame) -> pd.DataFrame:
            seed_artist = [song_data['artist_id']]
            seed_track = [song_data['track_id']]
            print(seed_artist, seed_track)
            results = spotify.recommendations(seed_artists=seed_artist, seed_tracks=seed_track, limit=SONGS_NUM)
            recommended_songs_dict = {}
            for i in range(len(results['tracks'])):
                recommended_songs_dict[i] = {'artist': results['tracks'][i]['artists'][0]['name'], 
                                             'title': results['tracks'][i]['name'], 
                                             'artist_id': results['tracks'][i]['artists'][0]['id'],
                                             'track_id': results['tracks'][i]['id']}
            recommended_songs_df = pd.DataFrame(recommended_songs_dict).T
            playlist_df = pd.concat([pd.DataFrame(song_data).T, recommended_songs_df], ignore_index=True)
            return playlist_df
        

        for i in range(3):
            song_data = self.random_3_songs.iloc[i]
            playlist_df = make_playlist_from_song(song_data)
            self.list_of_playlists[str(i+1)] = playlist_df

    def download_songs(self):
        # assert self.list_of_playlists is not None, 'List of playlists is not set'

        def make_dir_for_playlist(playlist_num: int):
            # もし、./music_folderや、./music_folder/1 などが存在しなければ、作成する。
            try:
                os.mkdir('./music_folder')
            except:
                pass
            try:
                os.mkdir(f'./music_folder/{playlist_num}')
            except:
                pass

        def download_song_from_playlist(playlist_df: pd.DataFrame, playlist_num:int):

            def get_youtube_music_url_list(playlist_df: pd.DataFrame) -> list:
                youtube_music_url_list = []
                for i in range(len(playlist_df)):
                    spotify_track_title = playlist_df.iloc[i]['title']
                    spotify_track_artist = playlist_df.iloc[i]['artist']
                    # spotify_track_info = spotify.track(song_id)
                    # spotify_track_title = spotify_track_info["name"]
                    # spotify_track_artist = spotify_track_info["artists"][0]["name"]
                    print(f'now searching {spotify_track_title} {spotify_track_artist}')
                    search_result = youtube.search(f'{spotify_track_title} {spotify_track_artist}', filter="songs")
                    if search_result == []:
                      continue
                    youtube_music_url = search_result[0]['videoId']
                    youtube_music_url_list.append(youtube_music_url)
                return youtube_music_url_list
            
            def download_songs_from_youtube_music_url_list(youtube_music_url_list: list, playlist_num: int):
                for i, youtube_music_url in enumerate(youtube_music_url_list):
                    cmd = f'yt-dlp -x -o "./music_folder/{playlist_num}/music_{i}_%(title)s_%(id)s" https://www.youtube.com/watch?v={youtube_music_url}'
                    subprocess.run(cmd, shell=True)
                    

            youtube_music_url_list = get_youtube_music_url_list(playlist_df)
            download_songs_from_youtube_music_url_list(youtube_music_url_list, playlist_num)

        for i in range(3):
            make_dir_for_playlist(i+1)
            
            playlist_df = self.list_of_playlists[str(i+1)]
            download_song_from_playlist(playlist_df, playlist_num = i+1)

        

if __name__ == '__main__':
    music_selector = music_player_module()

    # music_selector.select_playlist()

    # print(music_selector.playlist_url) # 乱数で選ばれたプレイリストのURLを表示

    # music_selector.get_songs_metadate_from_playlist()

    # print(music_selector.playlist_metadates) # プレイリストのメタデータを表示

    # music_selector.get_random_3_songs()

    # print(music_selector.random_3_songs) # プレイリストからランダムに3曲選んだものを表示

    user_select_3_songs = [['Lil Yachty', 'Poland'], ['King Gnu', '雨燦々'], ['Vaundy','踊り子'] ]
    music_selector.user_select_3_songs(user_select_3_songs)
    print(music_selector.random_3_songs) # プレイリストからランダムに3曲選んだものを表示

    music_selector.make_3playlist()

    print(music_selector.list_of_playlists) # 3つのプレイリストを表示

    print(music_selector.list_of_playlists['1']) # 1つ目のプレイリストを表示

    music_selector.download_songs()

    # music_selector.play_songs()