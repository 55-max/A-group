# wave1: 
# 再生フラグが立つ→再生→停止フラグが立つ→停止

import pygame
import time
import sys
import os

# ファイル名を指定して再生

def play_music(music_file):
    #初期設定
    pygame.mixer.init()
    pygame.mixer.music.load(music_file) # 音源を読み込み
    mp3_length = mp3_length = pygame.mixer.music.get_length() # 音源の長さ取得
    pygame.mixer.music.play(1) # 音源再生、ループは1回

    #再生中は1、停止中は0
    playFlag = 1
    stopFlag = 0

    #再生中は1、停止中は0
    while playFlag == 1:
        time.sleep(1)
        playFlag = pygame.mixer.music.get_busy()
        if stopFlag == 1:
            pygame.mixer.music.stop()
            playFlag = 0
        if playFlag == 0:
            pygame.mixer.music.play(1)
            playFlag = 1
            stopFlag = 0

    #終了
    pygame.mixer.music.stop()
    return


if __name__ == "__main__":
    args = sys.argv
    if (len(args) != 2):
        print("Error: 引数にmp3ファイルを指定してください")
        sys.exit()
    music_file = args[1]
    if (not os.path.exists(music_file)):
        print("Error: 指定されたファイルが見つかりません")
        sys.exit()
    play_music(music_file)