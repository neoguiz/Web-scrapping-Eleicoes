
from GoogleNews import GoogleNews 
import pandas as pd

googlenews = GoogleNews()
googlenews.set_lang('pt')
googlenews.set_period('5d')

googlenews.clear()

googlenews.search('Bolsonaro')
googlenews.total_count()

pesquisa_bolsonaro = googlenews.results()
df_bolsonaro = pd.DataFrame(pesquisa_bolsonaro)

display(df_bolsonaro)
