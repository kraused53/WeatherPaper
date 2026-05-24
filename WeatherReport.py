import Secrets
import requests
import datetime
import json

class WeatherReport:
    def __init__(self):
        #https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=weather_code,temperature_2m_max,temperature_2m_min,sunrise,sunset,daylight_duration,sunshine_duration,uv_index_max,precipitation_probability_max,wind_speed_10m_max&hourly=temperature_2m,surface_pressure,relative_humidity_2m,dew_point_2m,apparent_temperature,precipitation,precipitation_probability,rain,showers,snowfall,snow_depth,vapour_pressure_deficit,et0_fao_evapotranspiration,evapotranspiration,visibility,cloud_cover_high,cloud_cover_mid,cloud_cover_low,cloud_cover,pressure_msl,weather_code,wind_speed_10m,wind_speed_80m,wind_speed_120m,wind_speed_180m,wind_direction_10m,wind_direction_80m,wind_direction_120m,wind_direction_180m,wind_gusts_10m,temperature_80m,temperature_120m,temperature_180m,soil_moisture_27_to_81cm,soil_moisture_9_to_27cm,soil_moisture_3_to_9cm,soil_moisture_1_to_3cm,soil_moisture_0_to_1cm,soil_temperature_54cm,soil_temperature_18cm,soil_temperature_0cm,soil_temperature_6cm,uv_index_clear_sky,is_day,uv_index&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,weather_code,cloud_cover,surface_pressure,wind_speed_10m,wind_direction_10m&forecast_days=3&timeformat=unixtime&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch
        # API URL
        self.api_url = (
            ### Base URL ###
            "https://api.open-meteo.com/v1/forecast?"
            ### Set Location ###
            f"latitude={Secrets.get_lat()}"     # Latitude
            f"&longitude={Secrets.get_lon()}"   # Longitude
            ### Set Daily Forecast ###
            #"&daily="
            #"temperature_2m_max,"              # Request High temp
            #"temperature_2m_min,"              # Request Low temp
            #"sunrise,"                         # Request Sunrise Time
            #"sunset,"                          # Request Sunset Time
            #"uv_index_max,"                    # Request UV Index
            #"precipitation_hours"              # Request Precipitation Forecast
            ### Set Hourly Forecast ###
            #"&hourly="
            #"temperature_2m,"                  # Request Temperature
            #"relative_humidity_2m,"            # Request Humidity
            #"precipitation_probability,"       # Request Precipitation Chance
            #"precipitation,"                   # Request Precipitation Type
            #"weather_code"                     # Request Weather Code
            ### Set Current Weather ###
            "&current="
            #'visibility,'                      # Request Visibility
            'surface_pressure,'                # Request Surface Pressure
            "temperature_2m,"                  # Request Temperature
            "relative_humidity_2m,"            # Request Humidity
            "weather_code,"                    # Request Weather Code
            "precipitation_probability,"       # Request Precipitation
            "wind_speed_10m,"                  # Request Wind Speed
            "cloud_cover,"                     # Request Cloud Cover %
            'is_day'                           # Request Is Day? Boolean
            ### Settings ###
            "&timezone=America%2FNew_York"     # Set Time Zone
            #"&forecast_days=1"                 # Set Number Of Daily Forecast ( 1 = today only )
            "&timeformat=unixtime"             # Set Time Format
            "&wind_speed_unit=mph"             # Set Wind Speed Units
            "&temperature_unit=fahrenheit"     # Set Temperature Units
            "&precipitation_unit=inch"         # Set Precipitation Units
        )

        # Settings
        self.time_zone = 0
        self.temp_units = ""
        self.humidity_units = ""
        self.precipitation_prob_units = ""
        self.wind_speed_units = ""
        self.cloud_cover_units = ""
        self.wind_direction_units = ""

        # Data
        self.time = 0
        self.temperature = 0
        self.humidity = 0
        self.weather_code = 0
        self.precipitation_prob = 0
        self.wind_speed = 0
        self.cloud_cover = 0
        self.is_day = False
        self.wind_direction = 0

        self.json_data = ""

    def save_report(self):
        with open( 'data.json', 'w' ) as f:
            json.dump( self.json_data, f, indent=4 )

    def get_url(self) -> str:
        return self.api_url

    def generate_report(self) -> None:
        response = requests.get(self.api_url)
        if response.status_code != 200:
            print( "API Request Error!" )
            return

        data = response.json()

        # Current Weather
        if 'utc_offset_seconds' in data:
            self.time_zone = data['utc_offset_seconds']

        # Units
        if 'current_units' in data:
            if 'wind_direction_10m' in data['current_units']:
                self.wind_direction_units = data['current_units']['wind_direction_10m']

            if 'temperature_2m' in data['current_units']:
                self.temp_units = data['current_units']['temperature_2m']

            if 'relative_humidity_2m' in data['current_units']:
                self.humidity_units = data['current_units']['relative_humidity_2m']

            if 'precipitation_probability' in data['current_units']:
                self.precipitation_prob_units = data['current_units']['precipitation_probability']

            if 'wind_speed_10m' in data['current_units']:
                self.wind_speed_units = data['current_units']['wind_speed_10m']

            if 'cloud_cover' in data['current_units']:
                self.cloud_cover_units = data['current_units']['cloud_cover']

        # Data
        if 'current' in data:
            if 'wind_direction_10m' in data['current']:
                self.wind_direction = data['current']['wind_direction_10m']

            if 'time' in data['current']:
                self.time = data['current']['time']

            if 'precipitation_probability' in data['current']:
                self.precipitation_prob = data['current']['precipitation_probability']

            if 'temperature_2m' in data['current']:
                self.temperature = data['current']['temperature_2m']

            if 'relative_humidity_2m' in data['current']:
                self.humidity = data['current']['relative_humidity_2m']

            if 'wind_speed_10m' in data['current']:
                self.wind_speed = data['current']['wind_speed_10m']

            if 'weather_code' in data['current']:
                self.weather_code = data['current']['weather_code']

            if 'cloud_cover' in data['current']:
                self.cloud_cover = data['current']['cloud_cover']

            if 'is_day' in data['current']:
                if data['current']['is_day'] == 1:
                    self.is_day = True
                else:
                    self.is_day = False
        self.json_data = data
        self.save_report()

    def get_icon(self) -> str:
        pass

    def __str__(self) -> str:
        ret  = "#################### Weather Report ####################\n"
        ret += "\tTime\n"
        ret += f"\t\tDate: {datetime.datetime.fromtimestamp( self.time ).strftime( '%h %d, %Y' )}\n"
        ret += f"\t\tCurrent Time: {datetime.datetime.fromtimestamp( self.time ).strftime( '%I:%M %p' )}\n"
        ret += f"\t\tIs Daytime: {self.is_day}\n"
        ret += "\tWeather Condition:\n"
        ret += f"\t\tWeather Code: {self.weather_code}\n"
        ret += "\tTemperature\n"
        ret += f"\t\tCurrent Temperature: {self.temperature}{self.temp_units}\n"
        ret += "\tHumidity\n"
        ret += f"\t\tHumidity: {self.humidity}{self.humidity_units}\n"
        ret += "\tWind\n"
        ret += f"\t\tWind Speed: {self.wind_speed} {self.wind_speed_units}\n"

        return ret

if __name__ == "__main__":
    report = WeatherReport()
    report.generate_report()
    print( report.get_url() )
    print( report )