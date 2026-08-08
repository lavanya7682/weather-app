import requests
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")

text = "Python text-to-speech test. using win32com.client"
speak.Speak(text)


API_KEY = "b13989793f184149a91141538230103"
CITY = "dharmshala himachal"

# Correct URL for WeatherAPI.com
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    weather_text=f"Weather in {CITY}: {condition}, {temp_c}°C"
    print(weather_text)
    speak.Speak(weather_text)
else:
    print("Error:", response.json())