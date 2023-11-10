import datetime
#import requests
import subprocess

#LINEメッセージ送信の関数
def send_message(gomi_type):
    #なんかうまくいかないのでコメントアウト
    #url = "https://notify-api.line.me/api/notify" 
    #token = "トークンをここに入力"
    #headers = {"Authorization" : "Bearer "+ token}
    #message =  (gomi_type)
    #payload = {"message" :  message} 
    #r = requests.post(url, headers = headers, params=payload)

    message =  (gomi_type)
    API_KEY_DIR = './A/chatbot/API_KEY_LINE_NOTIFY.txt'

    with open(API_KEY_DIR) as f:
        api_key = f.read().rstrip('\n')

    sh_cmd = f'curl https://notify-api.line.me/api/notify -X POST -H "Authorization: Bearer {api_key}" -F "message={message}"'

    subprocess.run(sh_cmd, shell=True)  


#今日は第何週の何曜日かを調べる関数
def get_WeekNum_and_DayOfWeek(date_):
    # リストを用意（weekday()で取得した数値を曜日に変換)
    lists=["月曜日","火曜日","水曜日","木曜日","金曜日","土曜日","日曜日"]
    divmod_=divmod(date_.day,7) # 日付を７で割って商と余りを取得
    
    # 商が0＝日付が6日以下の場合は第一週
    if divmod_[0]==0:
        week_num=1
    # 余りが0＝7の倍数の日数は商＝第X週
    elif divmod_==0:
        week_num=divmod_[0]
    # それ以外＝商が1以上かつあまりもある⇒商＋1＝第X週
    else:
        week_num=divmod_[0]+1
    # 戻り値は第X週と曜日の二つ
    return (week_num,lists[date_.weekday()])

date_=datetime.date.today()
week_num,DayOfWeek=get_WeekNum_and_DayOfWeek(date_)
print(f"{date_}は第{week_num}週{DayOfWeek}")

#ゴミの種類を入れるための変数を作る。初期値は空白
gomi_type = ""

#ごみの日かどうかを判定する
if DayOfWeek == "水曜日" or DayOfWeek == "土曜日":
    gomi_type = "今日は「燃えるごみ」の日です。"
    
if DayOfWeek == "金曜日":
    
    #第一週、第三週の場合
    if week_num == 1 or week_num == 3:
        gomi_type = "今日は「燃えないごみ、びん・かん」の日です。"
        
    #第二週の場合
    if week_num == 2:
        gomi_type = "今日は「資源古紙、ペットボトル、危険不燃物」の日です。"
        
    #第四週の場合    
    if week_num == 4:
        gomi_type = "今日は「資源古紙、ペットボトル」の日です。"
    
if gomi_type == "":
    print("今日はごみ収集の日ではありません。")

else:
    print(gomi_type)
    #LINEメッセージ送信
    send_message(gomi_type)