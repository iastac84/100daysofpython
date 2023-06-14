#!/usr/bin/env python3
# Day 24

'''
Python script that fetches and displays the current weather information for a given location using the OpenWeatherMap API
To run we need a free API key at OpenWeatherMap and set it as an environment variable
export OPENWEATHERMAP_API_KEY=your_api_key_here
Also need to install the requests library if not installed already: pip install requests
'''


import os
import requests
import json

def get_weather(city):
    api_key = os.environ.get('OPENWEATHERMAP_API_KEY')
    if not api_key:
        print("Error: API key not found.")
        return

    base_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    url = base_url.format(city, api_key)

    try:
        response = requests.get(url)
        data = json.loads(response.text)

        # Extract relevant weather information
        weather_desc = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        # Convert temperature from Kelvin to Celsius
        temperature = temperature - 273.15

        # Print the weather information
        print(f"Weather in {city}:")
        print(f"Description: {weather_desc}")
        print(f"Temperature: {temperature:.2f}°C")
        print(f"Humidity: {humidity}%")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Provide the city name for which you want to fetch the weather
city_name = input("Enter the city name: ")
get_weather(city_name)

