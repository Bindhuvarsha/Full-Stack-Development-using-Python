import requests
city = input("enter city:")
url=f"https://wttr.in/{city}?format=j1"
response=requests.get(url)

data=response.json()
temp=data["current_condition"][0]["temp_C"]
print("temperature:",temp,"C")