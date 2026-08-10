import requests
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")
API_KEY = "b13989793f184149a91141538230103"

while True:
    COUNTRY = input("\nEnter Country (or type 'exit' to quit): ").strip()

    # Exit condition
    if COUNTRY.lower() in ["exit", "quit", "q"]:
        print("Goodbye!")
        speak.Speak("Goodbye!")
        break

    if not COUNTRY:
        continue

    CITY = input("Enter City: ").strip()

    # Allow exiting at city prompt as well
    if CITY.lower() in ["exit", "quit", "q"]:
        print("Goodbye!")
        speak.Speak("Goodbye!")
        break

    if not CITY:
        continue

    # Speak search target
    speak.Speak(f"{CITY}, {COUNTRY}")

    # Pass both City and Country to the query parameter
    query_location = f"{CITY},{COUNTRY}"
    URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={query_location}"

    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        # Extract location details from API response for accuracy
        actual_city = data["location"]["name"]
        actual_country = data["location"]["country"]

        weather_text = f"Weather in {actual_city}, {actual_country}: {condition}, {temp_c}°C"
        print(weather_text)
        speak.Speak(weather_text)
    else:
        print("Error:", response.json())