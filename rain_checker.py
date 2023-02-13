import requests
import json

api_key = "Insert Api key hear"

url = "http://api.openweathermap.org/data/2.5/weather?"

city = "Kochi"

complete_url = url + "appid=" + api_key + "&q=" + city

response = requests.get(complete_url)

response_json = response.json()

if response_json["cod"] != "404":
    val1 = response_json["main"]
    val2 = response_json["weather"]
    humid = val1["humidity"]
    state = val2[0]["main"]
    if state == "Rain" or state == "Drizzle" or state == "Thunderstorm":
        print('Oops its raining, take an umbrella')
        print("Current condition:", state)
    else:
        print("Its not raining")
        print("Current condition:", state)
    if humid > 90:
        print("Humidity is high, So it might rain though watch out")
        print("Humidity:", humid)