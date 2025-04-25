# features/weather.py
import requests

def get_weather(user_input):
    # Extract city name from input
    city = user_input.replace("weather", "").strip()

    if city:
        # Your WeatherAPI API key here
        api_key = "121a11b4dcb444c7bfa152626252104"
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

        try:
            response = requests.get(url)
            data = response.json()
            
            # Check if the API call was successful
            if "current" in data:
                weather_description = data["current"]["condition"]["text"]
                temperature = data["current"]["temp_c"]
                humidity = data["current"]["humidity"]
                return (f"The weather in {city} is {weather_description} with a temperature of {temperature}°C. "
                        f"Humidity: {humidity}%.")
            else:
                return "Sorry, I couldn't find the weather for that city."
        except requests.exceptions.RequestException as e:
            return f"Error occurred: {e}"
    else:
        return "Please provide a city name."
