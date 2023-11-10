import subprocess

message = '己がこれからの日本を担う存在であることを誇りに思え'
API_KEY_DIR = './A/chatbot/API_KEY_LINE_NOTIFY.txt'

with open(API_KEY_DIR) as f:
    api_key = f.read().rstrip('\n')

sh_cmd = f'curl https://notify-api.line.me/api/notify -X POST -H "Authorization: Bearer {api_key}" -F "message={message}"'

subprocess.run(sh_cmd, shell=True)  