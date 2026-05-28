import datetime

import Secrets
import PyLog
import requests
import time
import json
from pathlib import Path

_filepath = "forecast/forecast.json"

def get_new_forecast() -> str:
    # API URL
    api_url = (
        ####################
        #  Base  API  URL  #
        ####################
        "https://api.open-meteo.com/v1/forecast"

        ####################
        #     Location     #
        ####################
        f"?latitude={Secrets.get_lat()}"  # Local Latitude  ( SECRET )
        f"&longitude={Secrets.get_lon()}"  # Local Longitude ( SECRET )

        ####################
        #  Daily Forecast  #
        ####################
        "&daily="
        "weather_code,"  # Weather Code
        "temperature_2m_max,"  # Minimum Temperature At 2m
        "temperature_2m_min,"  # Maximum Temperature At 2m
        "sunrise,"  # Local Sunrise Time
        "sunset,"  # Local Sunset Time
        "precipitation_probability_max" # Chance of precipitation

        ####################
        # Hourly  Forecast #
        ####################
        "&hourly="
        "temperature_2m,"  # Temperature At 2m
        "relative_humidity_2m,"  # Humidity At 2m
        "precipitation_probability,"  # Chance Of Precipitation
        "weather_code,"  # Weather Code
        "surface_pressure,"  # Pressure At Local Ground Level
        "cloud_cover,"  # Percent Cloud Cover
        "visibility,"  # Visibility
        "wind_speed_10m,"  # Speed Of Wind At 10m
        "wind_direction_10m"  # Direction Of Wind At 10m

        ####################
        # Current  Weather #
        ####################
        "&current="
        "precipitation_probability,"  # Chance Of Precipitation
        "temperature_2m,"  # Temperature At 2m
        "relative_humidity_2m,"  # Relative Humidity At 2m
        "is_day,"  # Is It Currently Daytime
        "precipitation,"  # Accumulated Precipitation
        "weather_code,"  # Weather Code
        "cloud_cover,"
        "wind_speed_10m,"  # Speed Of Wind At 10m
        "wind_direction_10m,"  # Direction Of Wind At 10m
        "surface_pressure,"  # Pressure At Local Ground Level

        ####################
        #     Settings     #
        ####################
        "&timezone=America%2FNew_York"  # Timezone
        "&timeformat=unixtime"  # Timestamp Format 
        "&wind_speed_unit=mph"  # Wind Speed Units
        "&temperature_unit=fahrenheit"  # Temperature Units
        "&precipitation_unit=inch"  # Precipitation Units
    )

    PyLog.log( "Making API Call..." )

    cnt = 0
    response = requests.get(api_url)

    while response.status_code != 200:
        if cnt >= 10:
            PyLog.error( "API Failure" )
            return "ERROR"

        PyLog.warn( f"API Call Failed. Code: { response.status_code }. Attempt {cnt+1}/10" )

        cnt += 1

        time.sleep( 0.5 )
        response = requests.get(api_url)

    PyLog.log(f"API call success!")
    return response.text

def save_forecast( json_str: str ) -> None:
    PyLog.log( f"Saving forecast to {_filepath}" )
    with open( _filepath, "w" ) as file:
        json.dump( json.loads( json_str ), file, indent=4)

def load_forecast() -> str:
    json_str = "ERROR"
    with open( _filepath, "r" ) as file:
        json_str = file.read()

    return json_str

def get_forecast() -> str:
    json_str = ""
    if Path( _filepath ).is_file():
        PyLog.log( f"Loading forecast from {_filepath}" )
        json_str = load_forecast()
        json_data = json.loads( json_str )
        if 'current' in json_str:
            if 'time' in json_data['current']:
                report_time = int(datetime.datetime.now().timestamp())
                PyLog.log( f"Forecast is {int((report_time - int(json_data['current']['time'])) / 60)} minutes old" )
                if report_time - int( json_data['current']['time'] ) > 900:
                    PyLog.log( "Generating a new report..." )
                    json_str = get_new_forecast()
                else:
                    PyLog.log( "Report is valid and current" )
                    return json_str
        else:
            PyLog.log( f"Could not verify the age of {_filepath}, generating a new report..." )
            json_str = get_new_forecast()
    else:
        PyLog.log( f"Could not find file '{_filepath}', generating a new report..." )
        json_str = get_new_forecast()

    # If the program is here, a new report was generated. Save it
    save_forecast( json_str )
    return json_str

if __name__ == "__main__":
    forecast = get_forecast()