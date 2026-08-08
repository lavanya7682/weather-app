import requests

API_KEY = "b13989793f184149a91141538230103"
CITY = "mohali"

# Correct URL for WeatherAPI.com
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    print(f"Weather in {CITY}: {condition}, {temp_c}°C")
else:
    print("Error:", response.json())