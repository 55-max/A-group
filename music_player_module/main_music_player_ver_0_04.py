#tkinterを導入する→一旦見送る。

import vlc
import time

class music_player:
    def __init__(self):
        self.playing_music = False
        self.volume = 100 # (int: 0~100)
        self.music_list = []
        self.music_title = 'init'
        self.proc = None
        self.player = vlc.MediaPlayer()
        self.pause_flag = False
        pass

    def start_music(self):
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

        tmp_volume = self.volume
        for i in range(20):
            tmp_volume -= int(self.volume / 30)
            self.player.audio_set_volume(tmp_volume)
            time.sleep(0.01)
        self.player.pause()
        time.sleep(0.1)
        self.player.audio_set_volume(self.volume)


    def play_music(self):
        assert self.pause_flag == False, 'pause_flag is True'
        self.playing_music = True
        print(f'now playing... : {self.music_title}')
        self.player.set_mrl('test.mp3')
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
            tmp_volume -= int(self.volume / 30)
            self.player.audio_set_volume(tmp_volume)
            time.sleep(0.01)
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

if __name__ == '__main__':
    sleep_time = 3
    player = music_player()

    player.start_music()
    time.sleep(sleep_time)

    player.pause_music()
    time.sleep(sleep_time)

    player.start_music()
    time.sleep(sleep_time)

    player.stop_music()
    time.sleep(sleep_time)