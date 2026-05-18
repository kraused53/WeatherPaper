import Secrets

class WeatherReport:
    def __init__(self):
        self.api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={Secrets.get_lat()}&lon={Secrets.get_lon()}&appid={Secrets.get_key()}"

    def get_url(self) -> str:
        return self.api_url