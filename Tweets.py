import subprocess
import sys

def install(package):
   subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--user"])

# install("python-twitter-v2")
# install("snscrape")
# install("pandas")
# install("pandasgui")

# INICIO DO CODIGO

import snscrape.modules.twitter as dados
import pandas as pd
import datetime
from pandasgui import show

lista_tt_bolsonaro = []
data_final = datetime.date.today()
data_inicial = '2022-1-1'

for i, tweet in enumerate(dados.TwitterSearchScraper(f'{"Bolsonaro"} + since:{data_inicial} until:{data_final}').get_items()):
   if i>500:
      break
   lista_tt_bolsonaro.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
   
df_bolsonaro = pd.DataFrame(lista_tt_bolsonaro, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
gui = show(df_bolsonaro)
print(data_final)



