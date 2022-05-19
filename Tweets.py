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

def lista_tweets(candidato):
   
   lista_tt_candidato = []
   
   for i, tweet in enumerate(dados.TwitterSearchScraper(f'{candidato} + since:{data_inicial} until:{data_final}').get_items()):
      if i>500:
         break
      lista_tt_candidato.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
      
   return lista_tt_candidato

data_final = datetime.date.today()
data_inicial = '2022-1-1'

lista_tt_bolsonaro = lista_tweets("Bolsonaro")   
lista_tt_lula = lista_tweets("Lula")

df_bolsonaro = pd.DataFrame(lista_tt_bolsonaro, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
df_lula = pd.DataFrame(lista_tt_lula, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

gui = show(df_bolsonaro)
gui = show(df_lula)
print(data_final)




