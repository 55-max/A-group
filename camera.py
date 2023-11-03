import cv2 as cv

class Camera:

    def __init__(self):
        # カメラインスタンスの生成
        self.camera = cv.VideoCapture(0)

    def detect_smile(self):
        detect = False

        # カメラからフレームをキャプチャ
        ret, frame = self.camera.read()
        if not ret:
            return False

        # 画像をグレースケールに変換
        grayimg = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # 顔・笑顔検出の為、特徴量の読み込み
        face_cascade = cv.CascadeClassifier('./A/data/haarcascades/haarcascade_frontalface_default.xml')
        smile_cascade = cv.CascadeClassifier('./A/data/haarcascades/haarcascade_smile.xml')

        import os
        assert os.path.isfile(face_cascade), 'haarcascade_frontalface_default.xml がない'
        assert os.path.isfile(smile_cascade), 'eye_cascade_path.xml がない'

        # 顔を検出
        faces = face_cascade.detectMultiScale(grayimg, scaleFactor=1.2, minNeighbors=2, minSize=(250, 250))
        smiles = smile_cascade.detectMultiScale(grayimg, scaleFactor=1.2, minNeighbors=5, minSize=(40, 40))

        # 顔を検出した場合
        if len(faces) >= 1:
            # 検出した箇所に赤色枠を描画する
            for rect in faces:
                cv.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0, 255), thickness=3)
            # 笑顔を検出した場合
            if len(smiles) >= 3:
                # 検出した箇所に緑色枠を描画する
                for rect in smiles:
                    cv.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 255, 0), thickness=3)
                detect = True

        # 画像をウィンドウに表示
        cv.imshow('camera', frame)

        return detect    

    def check_stop(self):
        stop = False
        if cv.waitKey(100) > 0:
            stop = True
        return stop

    def stop_camera(self):
        # カメラを解放し、ウィンドウを閉じる
        self.camera.release()
        cv.destroyAllWindows()

if __name__ == '__main__':
    camera = Camera()
    while True:
        if camera.detect_smile():
            print('smile detect')
        if camera.check_stop():
            print('camera stop')
            camera.stop_camera()
            break