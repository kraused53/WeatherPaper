
class WeatherData:
    def __init__(self, data: dict) -> None:
        self.data = data

    def is_day(self) -> bool:
        if 'current' in self.data:
            if 'is_day' in self.data['current']:
                return self.data['current']['is_day'] == 1
        return False

    def current_weather_code(self) -> int:
        if 'current' in self.data:
            if 'weather_code' in self.data['current']:
                return self.data['current']['weather_code']
        return 0

    def today_weather_code(self) -> int:
        if 'daily' in self.data:
            if 'weather_code' in self.data['daily']:
                return self.data['daily']['weather_code'][0]
        return 0

    def tomorrow_weather_code(self) -> int:
        if 'daily' in self.data:
            if 'weather_code' in self.data['daily']:
                return self.data['daily']['weather_code'][1]
        return 0

    def time(self) -> int:
        if 'current' in self.data:
            if 'time' in self.data['current']:
                return self.data['current']['time']
        return 0

    def current_temperature(self) -> float:
        if 'current' in self.data:
            if 'temperature_2m' in self.data['current']:
                return self.data['current']['temperature_2m']
        return 0.0

    def current_temperature_units(self) -> str:
        if 'current_units' in self.data:
            if 'temperature_2m' in self.data['current_units']:
                return self.data['current_units']['temperature_2m']
        return "ERR"

    def tomorrow_high_temperature(self) -> float:
        if 'daily' in self.data:
            if 'temperature_2m_max' in self.data['daily']:
                return self.data['daily']['temperature_2m_max'][1]
        return 0

    def tomorrow_high_temperature_units(self) -> str:
        if 'daily_units' in self.data:
            if 'temperature_2m_max' in self.data['daily_units']:
                return self.data['daily_units']['temperature_2m_max']
        return "ERR"

    def today_high_temperature(self) -> float:
        if 'daily' in self.data:
            if 'temperature_2m_max' in self.data['daily']:
                return self.data['daily']['temperature_2m_max'][0]
        return 0

    def today_high_temperature_units(self) -> str:
        if 'daily_units' in self.data:
            if 'temperature_2m_max' in self.data['daily_units']:
                return self.data['daily_units']['temperature_2m_max']
        return "ERR"

    def today_low_temperature(self) -> float:
        if 'daily' in self.data:
            if 'temperature_2m_min' in self.data['daily']:
                return self.data['daily']['temperature_2m_min'][0]
        return 0

    def today_low_temperature_units(self) -> str:
        if 'daily_units' in self.data:
            if 'temperature_2m_min' in self.data['daily_units']:
                return self.data['daily_units']['temperature_2m_min']
        return "ERR"

    def tomorrow_low_temperature(self) -> float:
        if 'daily' in self.data:
            if 'temperature_2m_min' in self.data['daily']:
                return self.data['daily']['temperature_2m_min'][0]
        return 0

    def tomorrow_low_temperature_units(self) -> str:
        if 'daily_units' in self.data:
            if 'temperature_2m_min' in self.data['daily_units']:
                return self.data['daily_units']['temperature_2m_min']
        return "ERR"

    def tomorrow_sunrise(self) -> int:
        if 'daily' in self.data:
            if 'sunrise' in self.data['daily']:
                return self.data['daily']['sunrise'][1]
        return 0

    def tomorrow_sunset(self) -> int:
        if 'daily' in self.data:
            if 'sunset' in self.data['daily']:
                return self.data['daily']['sunset'][1]
        return 0

    def today_sunrise(self) -> int:
        if 'daily' in self.data:
            if 'sunrise' in self.data['daily']:
                return self.data['daily']['sunrise'][0]
        return 0

    def today_sunset(self) -> int:
        if 'daily' in self.data:
            if 'sunset' in self.data['daily']:
                return self.data['daily']['sunset'][0]
        return 0

    def current_precip_chance(self) -> int:
        if 'current' in self.data:
            if 'precipitation_probability' in self.data['current']:
                return self.data['current']['precipitation_probability']
        return 0

    def current_precip_chance_units(self) -> str:
        if 'current_units' in self.data:
            if 'precipitation_probability' in self.data['current_units']:
                return self.data['current_units']['precipitation_probability']
        return "ERR"

    def tomorrow_precip_chance_units(self) -> str:
        if 'daily_units' in self.data:
            if 'precipitation_probability_max' in self.data['daily_units']:
                return self.data['daily_units']['precipitation_probability_max']
        return "ERR"

    def tomorrow_precip_chance(self) -> int:
        if 'daily' in self.data:
            if 'precipitation_probability_max' in self.data['daily']:
                return self.data['daily']['precipitation_probability_max'][1]
        return 0

    def today_precip_chance_units(self) -> str:
        if 'daily_units' in self.data:
            if 'precipitation_probability_max' in self.data['daily_units']:
                return self.data['daily_units']['precipitation_probability_max']
        return "ERR"

    def today_precip_chance(self) -> int:
        if 'daily' in self.data:
            if 'precipitation_probability_max' in self.data['daily']:
                return self.data['daily']['precipitation_probability_max'][0]
        return 0

    def current_humidity(self) -> float:
        if 'current' in self.data:
            if 'relative_humidity_2m' in self.data['current']:
                return self.data['current']['relative_humidity_2m']
        return 0.0

    def current_humidity_units(self) -> str:
        if 'current_units' in self.data:
            if 'relative_humidity_2m' in self.data['current_units']:
                return self.data['current_units']['relative_humidity_2m']
        return "ERR"

    def current_cloud_cover(self) -> float:
        if 'current' in self.data:
            if 'cloud_cover' in self.data['current']:
                return self.data['current']['cloud_cover']
        return 0.0

    def current_cloud_cover_units(self) -> str:
        if 'current_units' in self.data:
            if 'cloud_cover' in self.data['current_units']:
                return self.data['current_units']['cloud_cover']
        return "ERR"

    def current_wind_speed(self) -> float:
        if 'current' in self.data:
            if 'wind_speed_10m' in self.data['current']:
                return self.data['current']['wind_speed_10m']
        return 0.0

    def current_wind_speed_units(self) -> str:
        if 'current_units' in self.data:
            if 'wind_speed_10m' in self.data['current_units']:
                return self.data['current_units']['wind_speed_10m']
        return "ERR"

    def current_wind_direction(self) -> float:
        if 'current' in self.data:
            if 'wind_direction_10m' in self.data['current']:
                return self.data['current']['wind_direction_10m']
        return 0.0

    def current_wind_direction_units(self) -> str:
        if 'current_units' in self.data:
            if 'wind_direction_10m' in self.data['current_units']:
                return self.data['current_units']['wind_direction_10m']
        return "ERR"