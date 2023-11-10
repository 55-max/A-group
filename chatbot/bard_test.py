from bardapi import Bard
import os

os.environ['_BARD_API_KEY'] = "dAjkNAtONuJCCQnRCLmBYMdyrx0WCFHE2yTXSg0rHstuUocEPFT4iXuAggRGETcptgq31w."

print( Bard().get_answer("日本の人口は何人ですか？")['content'] )