import subprocess

text_message1 = 'おはようございます。'
text_message2 = '今日も頑張っていきましょう'
subprocess.run(['./A/chatbot/jtalk.sh', text_message1 + text_message2])