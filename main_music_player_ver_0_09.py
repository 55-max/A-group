# このファイルがメインになる予定です。
# カメラデバイス関連のファイルを別のファイルにしよーかなーと思うぜ。

FACE_CASCADE_PATH = './data/haarcascades/haarcascade_frontalface_default.xml'
SMILE_CASCADE_PATH = './data/haarcascades/haarcascade_smile.xml'

import time
import camera_module.main_camera_ver_0_01 as camera_module
import music_player_module.main_music_player_ver_0_05 as music_player_module

camera_module._FACE_CASCADE_PATH = FACE_CASCADE_PATH
camera_module._SMILE_CASCADE_PATH = SMILE_CASCADE_PATH

camera = camera_module.Camera()
player = music_player_module.music_player()

if __name__ == '__main__':
    
    sleep_time = 1

    player.set_session(session_path = './music_folder/')

    # player.start_music()

    while True:
        camera.detect_elements()
        if camera.face_detect:
            print('face detect')
            player.start_music()
        if not camera.face_detect:
            print('not face detect')
            player.pause_music()
        if camera.check_stop():
            print('camera stop')
            camera.stop_camera()
            break
        # player.playing_music
        if (player.playing_music) and (not player.player.is_playing()):
            player.next_music()
            
        time.sleep(sleep_time)

        # if player.player.is_playing():
        #     print('playing')
        # else:
        #     print('not playing')
        #     player.next_music()


    # while True:
    #     time.sleep(sleep_time)
    #     if player.player.is_playing():
    #         print('playing')
    #         camera.detect_elements()
    #         if camera.face_detect:
    #             print('face detect')
    #             player.start_music()
    #         if not camera.face_detect:
    #             print('not face detect')
    #             player.pause_music()
    #         if camera.check_stop():
    #             print('camera stop')
    #             camera.stop_camera()
    #             break
    #     else:
    #         print('not playing')
    #         player.next_music()

    # while True:
    #         camera.detect_elements()
    #         if camera.face_detect:
    #             print('face detect')
    #             player.start_music()
    #         if not camera.face_detect:
    #             print('not face detect')
    #             player.pause_music()
    #         if camera.check_stop():
    #             print('camera stop')
    #             camera.stop_camera()
    #             break
    #         time.sleep(1)