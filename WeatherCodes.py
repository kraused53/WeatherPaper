from enum import Enum

class WeatherCodes(Enum):
    # Error
    UNKNOWN_WEATHER_CODE       = (   0,  "Unknown weather condition code", "01" )

    # Thunder Storms
    THUNDERSTORM_LIGHT_RAIN    = ( 200,    "Thunderstorm with light rain", "11" )
    THUNDERSTORM_RAIN          = ( 201,          "Thunderstorm with rain", "11" )
    THUNDERSTORM_HEAVY_RAIN    = ( 202,    "Thunderstorm with heavy rain", "11" )
    LIGHT_THUNDERSTORM         = ( 210,              "Light Thunderstorm", "11" )
    THUNDERSTORM               = ( 211,                    "Thunderstorm", "11" )
    HEAVY_THUNDERSTORM         = ( 212,              "Heavy Thunderstorm", "11" )
    RAGGED_THUNDERSTORM        = ( 221,             "Ragged Thunderstorm", "11" )
    THUNDERSTORM_LIGHT_DRIZZLE = ( 230, "Thunderstorm with light drizzle", "11" )
    THUNDERSTORM_DRIZZLE       = ( 231,       "Thunderstorm with drizzle", "11" )
    THUNDERSTORM_HEAVY_DRIZZLE = ( 232, "Thunderstorm with heavy drizzle", "11" )

    # Drizzle
    LIGHT_DRIZZLE              = ( 300,                   "Light drizzle", "09" )
    DRIZZLE                    = ( 301,                         "Drizzle", "09" )
    HEAVY_DRIZZLE              = ( 302,                   "Heavy drizzle", "09" )
    LIGHT_DRIZZLE_RAIN         = ( 310,              "Light drizzle rain", "09" )
    DRIZZLE_RAIN               = ( 311,                    "Drizzle rain", "09" )
    HEAVY_DRIZZLE_RAIN         = ( 312,              "Heavy drizzle rain", "09" )
    SHOWER_RAIN_DRIZZLE        = ( 313,         "Shower rain and drizzle", "09" )
    HEAVY_SHOWER_RAIN_DRIZZLE  = ( 314,   "Heavy shower rain and drizzle", "09" )
    SHOWER_DRIZZLE             = ( 321,                  "Shower drizzle", "09" )

    # Clear
    CLEAR                      = ( 800,                           "Clear", "01" )

    def __init__(self, code_id: int, text: str, icon: str) -> None:
        self.text = text
        self.code_id = code_id
        self.icon = icon

    @classmethod
    def from_id(cls, wc_id: int) -> "WeatherCodes":
        for code in WeatherCodes:
            if code.code_id == wc_id:
                return code
        return WeatherCodes.UNKNOWN_WEATHER_CODE

    def __str__(self) -> str:
        return str(self.text)

    def get_icon(self, is_day: bool) -> str:
        return f'{self.icon}{"d" if is_day else "n"}.png'

