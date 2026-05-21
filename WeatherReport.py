import Secrets
import requests

class WeatherReport:
    def __init__(self):
        # API URL
        self.api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={Secrets.get_lat()}&lon={Secrets.get_lon()}&appid={Secrets.get_key()}&units={Secrets.get_units()}"

        # Weather Code
        self.weather_id = 0
        self.weather_group = "UNKNOWN"
        self.weather_icon = "01d"
        self.weather_description = "UNKNOWN"

        # Weather Data
        self.temp_cur = 0
        self.temp_min = 0
        self.temp_max = 0

        # Pressure
        self.pressure = 0

        # Humidity
        self.humidity = 0

        # Visibility
        self.visibility = 0

        # Wind
        self.wind_speed = 0
        self.wind_direction = 0

        # Time
        self.time_cur  = 0
        self.time_sr   = 0
        self.time_ss   = 0
        self.time_zone = 0

        # Units
        self.pressure_units = "hPa"
        self.visibility_units = "m"
        self.humidity_units = "%"
        self.wind_direction_units = "°"

        if Secrets.get_units() == "imperial":
            self.temp_units = "°F"
            self.wind_speed_units = "mph"
        elif Secrets.get_units() == "metric":
            self.temp_units = "°C"
            self.wind_speed_units = "m/s"
        else:
            self.temp_units = "K"
            self.wind_speed_units = "m/s"

    def get_url(self) -> str:
        return self.api_url

    def generate_report(self) -> None:
        response = requests.get(self.api_url)
        if response.status_code != 200:
            print( "API Request Error!" )
            return

        data = response.json()

        # Parse weather code data
        if 'weather' in data:
            self.weather_id = data['weather'][0]['id']
            self.weather_group = data['weather'][0]['main']
            self.weather_icon = data['weather'][0]['icon']
            self.weather_description = data['weather'][0]['description']

        # Parse weather data
        if 'main' in data:
            self.temp_cur = data['main']['temp']
            self.temp_min = data['main']['temp_min']
            self.temp_max = data['main']['temp_max']
            self.pressure = data['main']['pressure']
            self.humidity = data['main']['humidity']

        if 'visibility' in data:
            self.visibility = data['visibility']

        if 'wind' in data:
            self.wind_speed = data['wind']['speed']
            self.wind_direction = data['wind']['deg']

        if 'dt' in data:
            self.time_cur = data['dt']

        if 'sys' in data:
            self.time_sr = data['sys']['sunrise']
            self.time_ss = data['sys']['sunset']

        if 'timezone' in data:
            self.time_zone = data['timezone']

    def get_icon(self) -> str:
        return self.weather_icon + ".png"

    def __str__(self) -> str:
        ret  = "#################### Weather Report ####################\n"
        ret += "\tTime\n"
        ret += f"\t\tCurrent Time: {self.time_cur - self.time_zone}\n"
        ret += f"\t\tSunrise Time: {self.time_sr  - self.time_zone}\n"
        ret += f"\t\tSunset  Time: {self.time_ss  - self.time_zone}\n"
        ret += "\tWeather Condition:\n"
        ret += f"\t\tWeather ID: {self.weather_id}\n"
        ret += f"\t\tWeather Group: {self.weather_group}\n"
        ret += f"\t\tWeather Icon: {self.weather_icon}\n"
        ret += f"\t\tWeather Description: {self.weather_description}\n"
        ret += "\tTemperature\n"
        ret += f"\t\tCurrent Temperature: {self.temp_cur}{self.temp_units}\n"
        ret += f"\t\tMinimum Temperature: {self.temp_min}{self.temp_units}\n"
        ret += f"\t\tMaximum Temperature: {self.temp_max}{self.temp_units}\n"
        ret += "\tPressure\n"
        ret += f"\t\tCurrent Pressure: {self.pressure}{self.pressure_units}\n"
        ret += "\tHumidity\n"
        ret += f"\t\tHumidity: {self.humidity}{self.humidity_units}\n"
        ret += "\tVisibility\n"
        ret += f"\t\tVisibility: {self.visibility}{self.visibility_units}\n"
        ret += "\tWind\n"
        ret += f"\t\tWind Speed: {self.wind_speed}{self.wind_speed_units}\n"
        ret += f"\t\tWind Direction: {self.wind_direction}{self.wind_direction_units}\n"

        return ret