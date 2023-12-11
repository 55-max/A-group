# ブラウザを起動した状態で実行する必要がある？

from bardapi import Bard
import os

os.environ['_BARD_API_KEY'] = ""

print( Bard().get_answer("日本の人口は何人ですか？")['content'] )