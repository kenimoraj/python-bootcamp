import os

import requests

MY_LAT = os.environ['MY_LAT']
MY_LONG = os.environ['MY_LONG']
API_KEY = os.environ['API_KEY']

PARAMS = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

def print_hourly_forecast(hourly: dict):

    ix = 0

    for hour in hourly[0:12]:
        weather = hour["weather"]
        weather_list = [weather_dscr["id"] for weather_dscr in weather]
        for w in weather_list:
            if w < 700:
                print(f"In {ix} hour(s) it's gonna rain")
            else:
                print(f"In {ix} hours umbrella not needed")
        ix += 1

data: dict
try:
    response = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=PARAMS)
    response.raise_for_status()
    print(f"Response code: {response.status_code}")
    data = response.json()
    # print(data)
    hourly_forecast = data["hourly"]

    print_hourly_forecast(hourly_forecast)



except requests.exceptions.HTTPError as e:
    print(e)


