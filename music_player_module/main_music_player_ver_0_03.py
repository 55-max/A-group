# start_musicと、pause_musicと、stop_musicを作る。resume_musicと、play_musicを統合。
# pause, stopのとき、volume downしていく感じにしたいなぁ。

import vlc

class music_player:
    def __init__(self):
        self.playing_music = False
        self.volume = 10 # (int: 0~100)
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
        self.player.pause()


    def play_music(self):
        assert self.pause_flag == False, 'pause_flag is True'
        self.playing_music = True
        print(f'now playing... : {self.music_title}')
        self.player.set_mrl('test.mp3')
        self.player.play()
    
    def pause_music(self):
        if not self.playing_music:
            return
        self.playing_music = False
        self.pause_flag = True
        print(f'now pausing... : {self.music_title}')
        self.player.pause()
        
    def stop_music(self):
        if not self.playing_music: # 既に止まっているなら、何もしない
            return
        self.playing_music = False # フラグを建てて、音楽を止める。
        print(f'now stopping... byebye : {self.music_title}')
        self.player.stop()

if __name__ == '__main__':
    import time
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