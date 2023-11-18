#%%
from ytmusicapi import YTMusic

ytmusic = YTMusic()

search_results = ytmusic.search("Oasis Wonderwall")

print(search_results)
#%%

import json
import pandas as pd

# pandasで結果を表示したい。

df = pd.DataFrame(search_results)
df