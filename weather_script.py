import requests

def fetch_weather(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data.get('main', {})
        weather = data.get('weather', [{}])[0]
        print(f"Weather in {city_name}:")
        print(f"Temperature: {main.get('temp', 'N/A')}°C")
        print(f"Humidity: {main.get('humidity', 'N/A')}%")
        print(f"Condition: {weather.get('main', 'N/A')} - {weather.get('description', 'N/A')}")
    else:
        print(f"Failed to get weather data: {response.status_code}")

if __name__ == "__main__":
    # Replace with your actual API key
    API_KEY = "e4641bab2541a403a31b09382d629284"
    CITY = "London"
    fetch_weather(CITY, API_KEY)
