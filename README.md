# Basic Weather App

A beginner-friendly Python command-line application that fetches real-time weather information using the OpenWeatherMap API.

## Features

* Enter a city name to get weather information
* Displays temperature in °C and °F
* Displays humidity percentage
* Displays weather condition
* Displays wind speed
* Handles invalid city names
* Handles network timeout and connection errors
* Handles invalid API keys
* Rejects empty city input

## Technologies Used

* Python
* Requests
* JSON
* OpenWeatherMap API

## Requirements

Install the required Python packages:

```bash
pip3 install requests python-dotenv
```

## API Key Setup

Create a `.env` file in the project folder and add your OpenWeatherMap API key:

```text
API_KEY=your_api_key_here
```

The `.env` file is excluded from GitHub using `.gitignore` to keep the API key private.

## How to Run

Open the terminal in the project folder and run:

```bash
python3 weatherApp.py
```

Enter a city name when prompted.

## Example

```text
Enter city name: Delhi

--- Weather Information ---
Temperature: 28.96 °C
Temperature: 84.13 °F
Humidity: 84%
Condition: Overcast Clouds
Wind Speed: 3.6 m/s
```

### Note: `.env` contains the private API key and is not uploaded to GitHub.