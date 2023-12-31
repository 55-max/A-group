import RPi.GPIO as GPIO

# このファイルがメインになる予定です。
# カメラデバイス関連のファイルを別のファイルにしよーかなーと思うぜ。

FACE_CASCADE_PATH = './data/haarcascades/haarcascade_frontalface_default.xml'
SMILE_CASCADE_PATH = './data/haarcascades/haarcascade_smile.xml'

import time
# import keyboard
import camera_module.main_camera_ver_0_01 as camera_module
import music_player_module.main_music_player_ver_0_06 as music_player_module
import ultra_sonic_module.Ultra_sonic as Ultra_sonic_module
import motor_related.motor_module as motor_module
import light_module.light as light_module
import chatbot.LINE_NOTIFY as LINE_NOTIFY

camera_module._FACE_CASCADE_PATH = FACE_CASCADE_PATH
camera_module._SMILE_CASCADE_PATH = SMILE_CASCADE_PATH

camera = camera_module.Camera()
player = music_player_module.music_player()
Ultra_sonic = Ultra_sonic_module.Ultra_sonic()
motor = motor_module.motor()
light = light_module.light()
LINE_NOTIFY = LINE_NOTIFY.notify()

def waiting_function(LIGHT_ON_FLAG):
    before_flag = LIGHT_ON_FLAG
    while True:
        Ultra_sonic.get_distance()
        tmp_flag = Ultra_sonic.near_flag
        if tmp_flag and (not before_flag):
            LIGHT_ON_FLAG = True
            print('light onします~~~~~~~~~~~~')
            LINE_NOTIFY.get_check_in_time()
            motor.set_dc(5.3)
            light.on()
            player.start_music()
            return LIGHT_ON_FLAG
        if (not tmp_flag) and before_flag:
            LIGHT_ON_FLAG = False
            before_flag = tmp_flag
            motor.set_dc(3.2)
            light.off()
            print('light offします~~~~~~~~~~~~')
            LINE_NOTIFY.get_check_out_time()
            LINE_NOTIFY.notify()
            player.pause_music()
            continue
        if (not tmp_flag) and (not before_flag):
            print('OFFOFF')
            continue
        if tmp_flag and before_flag:
            print('ONON')
            return LIGHT_ON_FLAG
        print('yes')
        before_flag = tmp_flag
        time.sleep(0.3)
            
def initial():
    light.off()
    motor.set_dc(3.2)

if __name__ == '__main__':

    initial()
    
    print('yes')
    LIGHT_ON_FLAG = False
    
    sleep_time = 0.5

    counter = 0

    player.set_session(session_path = './music_folder/')

    while True:

        LIGHT_ON_FLAG = waiting_function(LIGHT_ON_FLAG)

        print(counter)
        camera.detect_elements()
        if camera.face_detect:
            print('face detect')
            player.concentrate_score_down()
        if not camera.face_detect:
            print('not face detect')
            player.concentrate_score_up()
        if camera.check_stop():
            print('camera stop')
            camera.stop_camera()
            break
        
        if (player.playing_music) and (not player.player.is_playing()):
            counter = 0
            player.next_music()

        counter += 1
            
        time.sleep(sleep_time)

GPIO.cleanup()