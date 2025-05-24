import requests
from dotenv import load_dotenv
import os

# from pprint import pprint


load_dotenv()


def get_current_weather():
    print("\n*** Get Current Weather Conditions ***\n")

    city = input("\nPlease enter city name:\n")

    requests_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    # print(f"API Key: {os.getenv('API_KEY')}")
    # print(requests_url)

    weather_data = requests.get(requests_url).json()

    # pprint(weather_data)

    print(f"\nCurrent weather for {weather_data["name"]}")
    print(f"\nThem Temp is  {weather_data["main"]["temp"]}°C")
    print(
        f"\nFeels like  {weather_data["main"]["feels_like"]}°C and {weather_data["weather"][0]["description"]}."
    )


if __name__ == "__main__":
    get_current_weather()
