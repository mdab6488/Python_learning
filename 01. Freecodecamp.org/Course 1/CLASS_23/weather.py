from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Dhaka"):
    request_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=metric"

    weather_data = requests.get(request_url).json()

    return weather_data

    # return requests.get(request_url).json()


if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***\n")

    city = input("\nPlease enter a city name: ")

    # Check for emptry strings or string with only spaces
    if not bool(city.strip()):
        city = "Dhaka"
        # print("You must enter a city name.")
        # city = input("\nPlease enter a city name: ")

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
