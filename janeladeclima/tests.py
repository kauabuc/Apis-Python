import json
from datetime import datetime

import pycountry_convert as pc
import pytz
import requests

chave = 'e9c73dd5461d0905c6604df5b69bd173'
cidade = 'Pelotas'
api_link = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(
    cidade, chave)

r = requests.get(api_link)
dados = r.json()
print(dados)

# dados

pais_codigo = dados['sys']['country']
fusopais = pytz.country_timezones[pais_codigo]
pais = pytz.country_names[pais_codigo]


zona = pytz.timezone(fusopais[0])
zona_horas = datetime.now(zona)
zona_horas = zona_horas.strftime('%d/%m/%Y | %H:%M:%S %p')


tempo = dados['main']['temp']
pressao = dados['main']['pressure']
umidade = dados['main']['humidity']
velocidade = dados['wind']['speed']
descricao = dados['weather'][0]['description']

# mudando informações


def pais_para_continente(i):
    pais_alpha = pc.country_name_to_country_alpha2(i)
    pais_continente_codigo = pc.country_alpha2_to_continent_code(pais_alpha)
    pais_continente_nome = pc.convert_continent_code_to_continent_name(
        pais_continente_codigo)

    return pais_continente_nome


continente = pais_para_continente(pais)
