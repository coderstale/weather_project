import requests

API_KEY = ""
burl = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

rurl = f"{burl}?appid={API_KEY}&q={city}"
response = requests.get(rurl)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Weather:", weather)
    print("Temperature:", temperature, "Celsius")

else:
    print("ERROR: BAD REQ")
