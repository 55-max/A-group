import vlc

class music_player:
    def __init__(self):
        self.playing_music = False
        self.volume = 10 # (int: 0~100)
        self.music_list = []
        self.music_title = 'init'
        self.proc = None
        # self.player = vlc.MediaListPlayer()
        self.player = vlc.MediaPlayer()
        pass

    def start_music(self):
        if self.playing_music: # 既に流れているなら、何もしない
            return
        self.playing_music = True # フラグを建てて、音楽を流す。
        self.play_music()

    def play_music(self):
        print(f'now playing... : {self.music_title}')
        # ここに音楽を流す処理を書く。
        
        # command = 'cvlc test.mp3'
        # self.proc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)

        self.player.set_mrl('test.mp3')
        self.player.play()
    
        

    def stop_music(self):
        if not self.playing_music: # 既に止まっているなら、何もしない
            return
        self.playing_music = False # フラグを建てて、音楽を止める。
        # ここに音楽を止める処理を書く。
        print(f'now stopping... byebye : {self.music_title}')
        # self.player.stop()
        # pauseしたいときは、
        self.player.pause()