# このファイルがメインになる予定です。
# カメラデバイス関連のファイルを別のファイルにしよーかなーと思うぜ。

FACE_CASCADE_PATH = './data/haarcascades/haarcascade_frontalface_default.xml'
SMILE_CASCADE_PATH = './data/haarcascades/haarcascade_smile.xml'

import time
import keyboard
import camera_module.main_camera_ver_0_01 as camera_module
import music_player_module.main_music_player_ver_0_06 as music_player_module
import ultra_sonic_module.Ultra_sonic as Ultra_sonic_module
# import motor_related.motor_module as motor_module

camera_module._FACE_CASCADE_PATH = FACE_CASCADE_PATH
camera_module._SMILE_CASCADE_PATH = SMILE_CASCADE_PATH

camera = camera_module.Camera()
player = music_player_module.music_player()
Ultra_sonic = Ultra_sonic_module.Ultra_sonic()
# motor = motor_module.motor()



def waiting_function(LIGHT_ON_FLAG):
    before_flag = LIGHT_ON_FLAG
    while True:
        Ultra_sonic.get_distance()
        tmp_flag = Ultra_sonic.near_flag
        if tmp_flag and (not before_flag):
            LIGHT_ON_FLAG = True
            print('light onします')
            # motor.set_dc(3.2)
            player.start_music()
            # light on / motor きどう。
            return True
        if (not tmp_flag) and before_flag:
            LIGHT_ON_FLAG = False
            # motor.set_dc(5.3)
            print('light offします')
            player.pause_music()
            # light off / motor きどう。
            continue
        if (not tmp_flag) and (not before_flag):
            continue
        if tmp_flag and before_flag:
            return True
        print('yes')
        before_flag = tmp_flag
        time.sleep(0.3)
            
        
        


if __name__ == '__main__':
    print('yes')
    LIGHT_ON_FLAG = False
    
    # light on / motor きどう。

    sleep_time = 0.5

    counter = 0

    player.set_session(session_path = './music_folder/')

    # player.start_music()

    while True:

        waiting_function(LIGHT_ON_FLAG)

        # if counter > 3:
        #     counter = 0
        #     Ultra_sonic.get_distance()
        #     if not Ultra_sonic.near_flag:
        #         print('phone off. pause music...')
        #         player.pause_music()
        #     else:
        #         print('phone on.  playing music...')
        #         player.start_music()

        print(counter)
        camera.detect_elements()
        if camera.face_detect:
            print('face detect')
            player.concentrate_score_down()
            # player.start_music()
        if not camera.face_detect:
            print('not face detect')
            # player.pause_music()
            player.concentrate_score_up()
        if camera.check_stop():
            print('camera stop')
            camera.stop_camera()
            break
        # player.playing_music
        
        if (player.playing_music) and (not player.player.is_playing()):
            counter = 0
            player.next_music()

        counter += 1
            
        time.sleep(sleep_time)