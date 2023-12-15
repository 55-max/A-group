# このプログラムは、LINE Notifyを用いて、LINEに通知を送るプログラムである。
# クラスは、notifyである。
# クラスには、get_check_in_time, get_check_out_time, notifyの3つのメソッドがある。
# また変数は、check_in_time, check_out_timeの2つである。    

import time
import datetime
import subprocess

class notify:
    def __init__(self):
        self.check_in_time = ''
        self.check_out_time = ''

    def get_check_in_time(self):
        self.check_in_time = datetime.datetime.now().strftime('%-H時 %-M分 %-S秒')

    def get_check_out_time(self):
        self.check_out_time = datetime.datetime.now().strftime('%-H時 %-M分 %-S秒')

    def notify(self):
        message = f'{self.check_in_time}から{self.check_out_time}まで勉強しました！お疲れ様でした！'
        API_KEY_DIR = './chatbot/API_KEY_LINE_NOTIFY.txt'

        with open(API_KEY_DIR) as f:
            api_key = f.read().rstrip('\n')

        sh_cmd = f'curl https://notify-api.line.me/api/notify -X POST -H "Authorization: Bearer {api_key}" -F "message={message}"'

        subprocess.run(sh_cmd, shell=True)

if __name__ == '__main__':
    check_in_time = datetime.datetime.now().strftime('%-H時 %-M分 %-S秒')
    time.sleep(5)
    check_out_time = datetime.datetime.now().strftime('%-H時 %-M分 %-S秒')
    message = f'{check_in_time}から{check_out_time}まで勉強しました！お疲れ様でした！'
    API_KEY_DIR = './chatbot/API_KEY_LINE_NOTIFY.txt'

    with open(API_KEY_DIR) as f:
        api_key = f.read().rstrip('\n')

    sh_cmd = f'curl https://notify-api.line.me/api/notify -X POST -H "Authorization: Bearer {api_key}" -F "message={message}"'

    subprocess.run(sh_cmd, shell=True)  