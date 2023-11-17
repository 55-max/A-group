#%%
# pip install spotdl==0.9.1
import subprocess
import sys

#%%

# spotdlで曲をYouTubeのURLに変える関数
def spotify_playlist_url_to_youtube_url_list(spotify_playlist_url):
    cmd = f'spotdl {spotify_playlist_url} -d'
    res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(res.stdout)
    print(res.stderr)

spotify_playlist_url_to_youtube_url_list('https://open.spotify.com/playlist/5P45F9TMBgQ03TGvXBpwUQ')

#%%