import requests

##API
api_url = "https://power.larc.nasa.gov/api/temporal/daily/point?start=20220501&end=20220531&latitude=-22.7344&longitude=-47.6480&community=re&parameters=TS_MIN%2CTS%2CTS_MAX%2CPW&format=json&user=victorrocha&header=true&time-standard=utc"
request = requests.get(api_url)

data = request.json()


##Data de inicio/fim
data_header = data['header']
date_begin = data_header['start']
date_end = data_header['end']

formatted_date_begin = f"{date_begin[:4]}/{date_begin[4:6]}/{date_begin[6:]}"
formatted_date_end = f"{date_end[:4]}/{date_end[4:6]}/{date_end[6:]}"

##coordenadas
data_geometry = data['geometry']
coordinates = data_geometry['coordinates']

##Parametros requisitados
data_properties = data['properties']
data_parameters = data_properties['parameter']

##Extraindo os valores de cada parametro para uma lista
values_temp_min =  list(data_parameters['TS_MIN'].values())
values_temp_max = list(data_parameters['TS_MAX'].values())
values_temp_avarage = list(data_parameters['TS'].values())
values_preciptation = list(data_parameters['PW'].values())