import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(data):
    if data.get('cod') != 200:
        print("Error:", data.get('message'))
        return

    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    weather = data['weather'][0]['description']

    print(f"City: {city}, {country}")
    print(f"Temperature: {temp}°C")
    print(f"Weather: {weather}")

def main():
    api_key = "6d308d30d9095304ad7a1593a36a5c9f"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    weather_data = get_weather(city, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    main()