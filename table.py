import pandas as pd
from app import data_parameters, coordinates, formatted_date_begin, formatted_date_end
from IPython.display import display

df = pd.DataFrame()

##Extraindo os valores de cada parametro para uma lista
values_temp_min =  list(data_parameters['TS_MIN'].values())
values_temp_max = list(data_parameters['TS_MAX'].values())
values_temp_avarage = list(data_parameters['TS'].values())
values_preciptation = list(data_parameters['PW'].values())

##Construindo o data frame
df['temperatura_minima(C°)'] = values_temp_min
df['temperatura_maxima(C°)'] = values_temp_max
df['Temperatura_media(C°)'] = values_temp_avarage
df['precipitacao(cm)'] = values_preciptation

##Retornando valores
print(f"\n\nLatitude: {coordinates[1]}")
print(f"Longitude: {coordinates[0]}")
print(f"Data ínicio: {formatted_date_begin}")
print(f"Data fim: {formatted_date_end}\n\n")
display(df)