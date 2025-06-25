import os
import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data.get('main', {})
        weather = data.get('weather', [{}])[0]
        print(f"Weather in {city}:")
        print(f"Temperature: {main.get('temp', 'N/A')}°C")
        print(f"Description: {weather.get('description', 'N/A')}")
    else:
        print("Failed to fetch weather data. Check city name or API key.")

def main():
    city = input("Enter city name: ")
    api_key = "e5dc98f0036a899b908d22f2046a06c1"  # Replace with your actual API key or set as environment variable
    if not api_key:
        print("Error: Please set the OPENWEATHER_API_KEY environment variable.")
        return
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
