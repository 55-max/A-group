# 効果音を再生するモジュール

import vlc
p = vlc.MediaPlayer()

class SFX_module:
    def __init__(self):
        self.click_sound_dir = 'SFX/click1.wav'
        self.shut_down_sound_dir = 'SFX/shutdown1.wav'
        self.player = vlc.MediaPlayer()

    def click_sound(self):
        p.set_mrl(self.click_sound_dir)
        p.play()

    def shut_down_sound(self):
        p.set_mrl(self.shut_down_sound_dir)
        p.play()

if __name__ == '__main__':
    SFX = SFX_module()
    SFX.click_sound()
    import time
    time.sleep(1)
    SFX.shut_down_sound()