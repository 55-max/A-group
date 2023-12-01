#tkinterを導入する→一旦見送る。

import vlc
import time
import glob
import random

class music_player:
    def __init__(self):
        self.playing_music = False
        self.volume = 100 # (int: 0~100)
        self.music_list = []
        self.music_title = 'init'
        self.proc = None
        self.player = vlc.MediaPlayer()
        self.pause_flag = False
        self.session_path = None
        self.music_playlist = {1: None, 2: None, 3: None}
        self.concentrate_score_list = [0,0]
        pass
    
    def set_session(self, session_path: str):
        self.session_path = session_path

        class music_playlist:
            def __init__(self, playlist_path: str):
                self.counter = 0
                self.playlist_path = playlist_path
                self.playlist = glob.glob(f'{playlist_path}/*')
                self.playlist_shuffled = random.sample(self.playlist, len(self.playlist))

        self.music_playlist = {1: music_playlist(f'{self.session_path}/1'), 
                               2: music_playlist(f'{self.session_path}/2'), 
                               3: music_playlist(f'{self.session_path}/3')}
        
        self.now_playing_playlist = 2


    def start_music(self):
        assert self.session_path is not None, 'session_path is not set. 恐らく、set_session()を実行していません。'
        if self.playing_music: # 既に流れているなら、何もしない
            return
        if self.pause_flag:
            self.resume_music()
        else:
            self.play_music()
        
    def resume_music(self):
        assert self.pause_flag, 'pause_flag is False'
        self.playing_music = True
        self.pause_flag = False
        print(f'now resuming... : {self.music_title}')
    
        tmp_volume = 0
        self.player.audio_set_volume(tmp_volume)
        self.player.pause()
        for i in range(20):
            tmp_volume += int(self.volume / 20)
            self.player.audio_set_volume(tmp_volume)
            time.sleep(0.02)
        time.sleep(0.1)
        self.player.audio_set_volume(self.volume)



    def play_music(self):
        assert self.pause_flag == False, 'pause_flag is True'
        self.playing_music = True
        print(f'now playing... : {self.music_title}')
        self.player.set_mrl(self.music_playlist[ self.now_playing_playlist ].playlist[self.music_playlist[ self.now_playing_playlist ].counter])
        self.player.audio_set_volume(self.volume)
        self.player.play()
    
    def pause_music(self):
        if not self.playing_music:
            return
        self.playing_music = False
        self.pause_flag = True
        print(f'now pausing... : {self.music_title}')
        
        tmp_volume = self.volume
        for i in range(20):
            tmp_volume -= int(self.volume / 20)
            self.player.audio_set_volume(tmp_volume)
            time.sleep(0.02)
        self.player.pause()
        time.sleep(0.1)
        self.player.audio_set_volume(self.volume)
        
    def stop_music(self):
        if not self.playing_music: # 既に止まっているなら、何もしない
            return
        self.pause_music()
        self.pause_flag = False
        self.playing_music = False # フラグを建てて、音楽を止める。
        print(f'now stopping... byebye : {self.music_title}')
        self.player.stop()

    def next_music(self):
        self.pause_flag = False
        self.playing_music = False # フラグを建てて、音楽を止める。
        self.music_playlist[ self.now_playing_playlist ].counter += 1
        concentrate_score = self.concentrate_score_list[0] / self.concentrate_score_list[1]
        
        if concentrate_score > 0.8:
            self.now_playing_playlist = 1
            print('concentrate_score > 0.8 : 1')
        elif concentrate_score > 0.6:
            self.now_playing_playlist = 2
            print('concentrate_score > 0.6 : 2')
        else:
            self.now_playing_playlist = 3
            print('concentrate_score < 0.6 : 3')
        if random.random() < 0.1:
            self.now_playing_playlist = random.randint(1,3)
            print('random')
            
        if self.music_playlist[ self.now_playing_playlist ].counter >= len(self.music_playlist[ self.now_playing_playlist ].playlist):
            self.music_playlist[ self.now_playing_playlist ].counter = 0
        self.concentrate_score_list = [0,0]
        
        self.play_music()

    def concentrate_score_up(self):
        self.concentrate_score_list[0] += 1
        self.concentrate_score_list[1] += 1
    
    def concentrate_score_down(self):
        self.concentrate_score_list[0] -= 1
        self.concentrate_score_list[1] += 1

if __name__ == '__main__':
    sleep_time = 3
    player = music_player()

    player.set_session(session_path = './music_folder/')



    player.start_music()

    while True:
        time.sleep(sleep_time)
        if player.player.is_playing():
            print('playing')
        else:
            print('not playing')
            player.next_music()
        

    player.pause_music()
    time.sleep(sleep_time)

    player.start_music()
    time.sleep(sleep_time)

    player.stop_music()
    time.sleep(sleep_time)
