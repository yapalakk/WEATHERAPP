import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

while True:
    city = input("Enter city name: ").strip()

    # Empty input validation
    if city == "":
        print("City name cannot be empty.")
        continue

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        # Invalid API key
        if response.status_code == 401:
            print("Invalid API key.")
            break

        # City not found
        if response.status_code == 404:
            print("City not found.")
            continue

        response.raise_for_status()

        # JSON response
        data = response.json()

        # Weather information
        temperature_c = data["main"]["temp"]
        temperature_f = (temperature_c * 9/5) + 32
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print("\n--- Weather Information ---")
        print(f"Temperature: {temperature_c} °C")
        print(f"Temperature: {temperature_f:.2f} °F")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition.title()}")
        print(f"Wind Speed: {wind_speed} m/s")

        break

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Network error. Please check your internet connection.")

    except requests.exceptions.RequestException:
        print("Something went wrong. Please try again.")