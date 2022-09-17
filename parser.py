import csv, json, requests

response = requests.get("https://mars.nasa.gov/rss/api/?feed=weather&category=msl&feedtype=json")
mars = json.loads(response.text)

data = []

for sol in mars['soles']:
    row = {
        'date': sol['terrestrial_date'],
        'min_temp': sol['min_temp'],
        'max_temp': sol['max_temp'],
        'pressure': sol['pressure'],
        'uv_irradiance': sol['local_uv_irradiance_index']
    }
    data.append(row)

with open("mars.json", "w") as file:
    json.dump(data, file)

file.close()