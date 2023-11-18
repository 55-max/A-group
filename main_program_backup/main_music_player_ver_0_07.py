# このファイルがメインになる予定です。
# 音楽を実際に流してみるぜ。omxplayerはやめて、python-vlcを使うのもやめて、cvlcを使ってみる。
# 一旦、場所を変える戦法で行くか。

FACE_CASCADE_PATH = './data/haarcascades/haarcascade_frontalface_default.xml'
SMILE_CASCADE_PATH = './data/haarcascades/haarcascade_smile.xml'

import cv2 as cv
import time
import vlc
import subprocess
import pathlib
import os
import sys
import shutil

class Camera:

    def __init__(self):
        # カメラインスタンスの生成
        self.camera = cv.VideoCapture(0)
        self.face_detect = False
        self.smile_detect = False

    def detect_elements(self):
        self.face_detect = False
        self.smile_detect = False

        # カメラから画像を取得
        ret, frame = self.camera.read()
        if not ret:
            return False
        
        # 画像をグレースケールに変換
        grayimg = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # 顔・笑顔検出の為、特徴量の読み込み
        face_cascade = cv.CascadeClassifier(FACE_CASCADE_PATH)
        smile_cascade = cv.CascadeClassifier(SMILE_CASCADE_PATH)

        # 顔を検出
        faces = face_cascade.detectMultiScale(grayimg, scaleFactor=1.2, minNeighbors=2, minSize=(250, 250))
        smiles = smile_cascade.detectMultiScale(grayimg, scaleFactor=1.2, minNeighbors=5, minSize=(40, 40))

        # 顔を検出した場合
        if len(faces) >= 1:
            self.face_detect = True
            # 笑顔を検出した場合
            if len(smiles) >= 3:
                self.smile_detect = True
        
        cv.imshow('camera', frame) # 画像をウィンドウに表示（デバッグ用）
        return self

    def check_stop(self):
        stop = False
        if cv.waitKey(100) > 0:
            stop = True
        return stop

    def stop_camera(self):
        # カメラを解放し、ウィンドウを閉じる
        self.camera.release()
        cv.destroyAllWindows()

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

if __name__ == '__main__':
    # 今回は、適当に、カメラが顔を検出したら、音楽を流す。カメラが、顔を検出せずに、5秒経ったら、音楽を止めるみたいなのにしたい。
    # time.sleep(3)
    camera = Camera()
    player = music_player()
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
        time.sleep(0.1)