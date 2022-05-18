import subprocess
import sys


def install(package):
     subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("GoogleNews")
install("pandas")
install("IPython")
install("pandasgui")

from GoogleNews import GoogleNews 
import pandas as pd
from IPython.display import display
from pandasgui import show

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
lista_candidato = []

googlenews = GoogleNews()
googlenews.set_lang('pt')
googlenews.set_period('5d')

def pesquisa_candidato(candidato):

    googlenews.clear()
    googlenews.search(candidato)
    googlenews.total_count()

    resultados_candidato = googlenews.results()
    for linha in resultados_candidato:
         #Se você quer adicionar um dataframe do pandas use concat() em vez de append()
        lista_candidato.concat(linha)


pesquisa_candidato("Bolsonaro")
pesquisa_candidato("Lula")

df_candidato = pd.DataFrame(lista_candidato)
gui = show(df_candidato)
