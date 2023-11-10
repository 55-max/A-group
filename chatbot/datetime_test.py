import datetime

#設定時間
TIME_SETTING = 10

#開始時間の取得
start_time = datetime.datetime.now()

#開始時刻を表示
print(start_time)
print('開始')

#ループ
while True:
    #現在時刻の取得
    current_time = datetime.datetime.now()

    #経過時間を計算
    elapsed_time = current_time - start_time
    
    #設定時間を経過したら実行
    if elapsed_time.seconds >= TIME_SETTING:
        #現在時刻を表示    
        print(current_time)
        
        #スタート時間の更新
        start_time = start_time + datetime.timedelta(seconds=TIME_SETTING)
        
        #時間取得し文字列化
        message = datetime.datetime.now().strftime('%H時 %M分 %S秒です')
        
        #表示
        print(message)