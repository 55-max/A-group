import cv2 as cv
import time

# 初期値では、このパスが使われるが、上のファイルで変更可能ということになっている。
_FACE_CASCADE_PATH = './data/haarcascades/haarcascade_frontalface_default.xml'
_SMILE_CASCADE_PATH = './data/haarcascades/haarcascade_smile.xml'


class Camera:

    def __init__(self):
        # カメラインスタンスの生成
        self.camera = cv.VideoCapture(0)
        self.face_detect = False
        self.smile_detect = False
        self.FACE_CASCADE_PATH = _FACE_CASCADE_PATH
        self.SMILE_CASCADE_PATH = _SMILE_CASCADE_PATH

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
        face_cascade = cv.CascadeClassifier(_FACE_CASCADE_PATH)
        smile_cascade = cv.CascadeClassifier(_SMILE_CASCADE_PATH)

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