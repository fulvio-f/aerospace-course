import requests # Importando a biblioteca utilizada para extrair informações de API
import json     # Importando a biblioteca para manipular JSON

response = requests.get("https://mars.nasa.gov/rss/api/?feed=weather&category=msl&feedtype=json") # "Baixando" dados climáticos do site da NASA
mars = json.loads(response.text) # Carregando o JSON dos dados de Marte em um dicionário (dict)

data = [] # Inicializando lista para dados de Marte

# FOR LOOP para salvar as temperaturas de Marte dos últimos 7 dias, por isso range(0,7)
for i in range(0,7):
    sol = mars['soles'][i]
    row = {
        'date': sol['terrestrial_date'],
        'min_temp': sol['min_temp'],
        'max_temp': sol['max_temp']
    }
    data.append(row)

# Salvando JSON das temperaturas de Marte em um arquivo mars.json
with open("mars.json", "w") as file:
    final = json.dumps(data, indent=2)
    file.write(final)
