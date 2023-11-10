import subprocess
import datetime

#定数
TASK_TIME = 10 #25*60 #25分
REST_TIME = 5 # 5*60 #5分
JTALK_PATH = './A/chatbot/jtalk.sh'

#変数の初期化
time_setting = TASK_TIME #設定時間
isTask= True #現在の状態がTaskであるかどうか
speech_time = '' #読み上げ時刻用の文字列
speech_message = '' #読み上げメッセージ用の文字列
        
#開始時間の取得
start_time = datetime.datetime.now()

#開始時刻を表示
print(start_time)
print('開始')

#読み上げ
subprocess.run([JTALK_PATH, 'ポモドーロ、スタートです'])

#ループ
while True:
    #現在時刻の取得
    current_time = datetime.datetime.now()

    #経過時間を計算
    elapsed_time = current_time - start_time
    
    #設定時間を経過したら実行
    if elapsed_time.seconds >= time_setting:
        #現在時刻を表示    
        print(current_time)
        
        #スタート時間の更新
        start_time = start_time + datetime.timedelta(seconds=time_setting)
        
        #時間取得し文字列化
        speech_time = datetime.datetime.now().strftime('%-H時 %-M分 %-S秒です')

        #現在の状態に応じて、状態・メッセージ・設定時間を更新
        if isTask== True:
            isTask= False #状態
            speech_message = '休憩しましょう' #メッセージ
            time_setting = REST_TIME #設定時間
        else:
            isTask= True #状態
            speech_message = '再開です' #メッセージ
            time_setting = TASK_TIME #設定時間

        #メッセージを表示
        print(speech_message)
        
        #時刻とメッセージを読み上げ
        subprocess.Popen([JTALK_PATH, speech_time + speech_message])