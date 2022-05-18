
from GoogleNews import GoogleNews 
import pandas as pd
from IPython.display import display
from pandasgui import show

googlenews = GoogleNews()
googlenews.set_lang('pt')
googlenews.set_period('5d')

googlenews.clear()

googlenews.search('Bolsonaro')
googlenews.total_count()

pesquisa_bolsonaro = googlenews.results()
df_bolsonaro = pd.DataFrame(pesquisa_bolsonaro)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

display(df_bolsonaro)
gui = show(df_bolsonaro)
# print(df_bolsonaro.to_string())
