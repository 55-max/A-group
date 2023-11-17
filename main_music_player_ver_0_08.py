# このファイルがメインになる予定です。
# カメラデバイス関連のファイルを別のファイルにしよーかなーと思うぜ。

FACE_CASCADE_PATH = './data/haarcascades/haarcascade_frontalface_default.xml'
SMILE_CASCADE_PATH = './data/haarcascades/haarcascade_smile.xml'

import time
import camera_module.main_camera_ver_0_01 as camera_module
import music_player_module.main_music_player_ver_0_01 as music_player_module

camera_module._FACE_CASCADE_PATH = FACE_CASCADE_PATH
camera_module._SMILE_CASCADE_PATH = SMILE_CASCADE_PATH

camera = camera_module.Camera() # カメラのインスタンスを作成
player = music_player_module.music_player() # 音楽プレイヤーのインスタンスを作成

if __name__ == '__main__':
    
    time.sleep(3)

    while True:
        camera.detect_elements()
        if camera.face_detect:
            print('face detect')
            player.start_music()
        if not camera.face_detect:
            print('not face detect')
            player.stop_music()
        if camera.check_stop():
            print('camera stop')
            camera.stop_camera()
            break
        time.sleep(1)