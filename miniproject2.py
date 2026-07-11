# import requests
# city = input("enter city:")
# url=f"https://wttr.in/{city}?format=j1"
# response=requests.get(url)

# data=response.json()
# temp=data["current_condition"][0]["temp_C"]
# humidity=data["current_condition"][0]["humidity"]
# condition=data["current_condition"][0]["weatherDesc"][0][Value]
# print("temperature:",temp,"C")
# print("humidity:",humidity,"%")
# print("weather:",condition)

import requests

city = input("Enter city name: ")
url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)
data = response.json()

current = data["current_condition"][0]

print("\n------ Current Weather ------")
print("City:", city)
print("Temperature:", current["temp_C"], "C")
print("Humidity:", current["humidity"], "%")
print("Weather:", current["weatherDesc"][0]["value"])
print("Wind Speed:", current["windspeedKmph"], "km/h")

print("\n------ Hourly Forecast ------")

hourly = data["weather"][0]["hourly"]

for hour in hourly:
    print(
        f"Time: {hour['time']} | "
        f"Temp: {hour['tempC']}C | "
        f"Humidity: {hour['humidity']}% | "
        f"Weather: {hour['weatherDesc'][0]['value']}"
    )