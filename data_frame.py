import pandas as pd
from app import *
from IPython.display import display

df = pd.DataFrame()

##Construindo o data frame

## 'dia_da_observacao' == 1° coluna
df['temperatura_minima(C°)'] = values_temp_min #2° coluna
df['temperatura_maxima(C°)'] = values_temp_max#3° coluna
df['Temperatura_media(C°)'] = values_temp_avarage#4° coluna
df['precipitacao(cm)'] = values_preciptation#5° coluna

##Retornando valores
print(f"\n\nLatitude: {coordinates[1]}")
print(f"Longitude: {coordinates[0]}")
print(f"Data ínicio: {formatted_date_begin}")
print(f"Data fim: {formatted_date_end}\n\n")
display(df)