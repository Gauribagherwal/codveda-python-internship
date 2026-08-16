import requests

API_URL = "https://api.open-meteo.com/v1/forecast"


def get_weather(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,weather_code",
        "timezone": "auto"
    }

    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        current = data.get("current")

        if not current:
            print("Error: Invalid response received from the API.")
            return

        print("\n==============================")
        print("      WEATHER INFORMATION")
        print("==============================")
        print(f"Temperature: {current.get('temperature_2m')} °C")
        print(f"Humidity: {current.get('relative_humidity_2m')} %")
        print(f"Weather Code: {current.get('weather_code')}")
        print("==============================")

    except requests.exceptions.RequestException as error:
        print("Error: Unable to connect to the weather API.")
        print("Details:", error)

    except ValueError:
        print("Error: The API returned invalid JSON.")


print("==============================")
print("      WEATHER API APP")
print("==============================")

try:
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))

    get_weather(latitude, longitude)

except ValueError:
    print("Error: Please enter valid numeric coordinates.")