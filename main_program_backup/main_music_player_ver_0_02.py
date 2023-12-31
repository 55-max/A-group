# このファイルがメインになる予定です。
# 画像で確認する部分を消したぜ。

FACE_CASCADE_PATH = './A-group/data/haarcascades/haarcascade_frontalface_default.xml'
SMILE_CASCADE_PATH = './A-group/data/haarcascades/haarcascade_smile.xml'

import cv2 as cv

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
        
        # cv.imshow('camera', frame) # 画像をウィンドウに表示
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
        pass

    def start_music(self):
        self.playing_music = True
        self.play_music()
        pass

    def play_music(self):
        print(self.music_title)
        pass

    def stop_music(self):
        pass

    def next_music(self):
        pass

    def previous_music(self):
        pass

    def volume_up(self):
        pass

    def volume_down(self):
        pass

    def check_stop(self):
        pass

    def stop_music_player(self):
        pass

if __name__ == '__main__':
    camera = Camera()
    player = music_player()
    while True:
        if camera.detect_elements().face_detect:
            print('face detect')
            player.start_music()
        if camera.detect_elements().smile_detect:
            print('smile detect')
            player.stop_music()
        if camera.check_stop():
            print('camera stop')
            camera.stop_camera()
            break