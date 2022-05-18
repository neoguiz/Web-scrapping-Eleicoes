
from GoogleNews import GoogleNews 
import pandas as pd
from IPython.display import display

googlenews = GoogleNews()
googlenews.set_lang('pt')
googlenews.set_period('5d')

googlenews.clear()

googlenews.search('Bolsonaro')
googlenews.total_count()

pesquisa_bolsonaro = googlenews.results()
df_bolsonaro = pd.DataFrame(pesquisa_bolsonaro)

# display(df_bolsonaro)
# print(df_bolsonaro.to_string())
