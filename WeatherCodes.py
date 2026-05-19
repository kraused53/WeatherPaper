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
    SHOWER_RAIN_DRIZZLE        = ( 313,         "Rain shower and drizzle", "09" )
    HEAVY_SHOWER_RAIN_DRIZZLE  = ( 314,   "Heavy rain shower and drizzle", "09" )
    SHOWER_DRIZZLE             = ( 321,                  "Shower drizzle", "09" )

    # Rain
    LIGHT_RAIN                 = ( 500,                      "Light rain", "10" )
    MODERATE_RAIN              = ( 501,                   "Moderate rain", "10" )
    HEAVY_RAIN                 = ( 502,                      "Heavy rain", "10" )
    VERY_HEAVY_RAIN            = ( 503,                 "Very heavy rain", "10" )
    EXTREME_RAIN               = ( 504,                    "Extreme rain", "10" )
    FREEZING_RAIN              = ( 511,                   "Freezing rain", "13" )
    LIGHT_SHOWER_RAIN          = ( 520,              "Light rain showers", "09" )
    SHOWER_RAIN                = ( 521,                    "Rain showers", "09" )
    HEAVY_SHOWER_RAIN          = ( 522,              "Heavy rain showers", "09" )
    RAGGED_SHOWER_RAIN         = ( 531,             "Ragged rain showers", "09" )

    # Snow
    LIGHT_SNOW                 = ( 600,                      "Light snow", "13" )
    SNOW                       = ( 601,                            "Snow", "13" )
    HEAVY_SNOW                 = ( 602,                      "Heavy snow", "13" )
    SLEET                      = ( 611,                           "Sleet", "13" )
    LIGHT_SHOWER_SLEET         = ( 612,              "Light sleet shower", "13" )
    SHOWER_SLEET               = ( 613,                    "Sleet shower", "13" )
    LIGHT_RAIN_AND_SNOW        = ( 615,             "Light rain and snow", "13" )
    RAIN_AND_SNOW              = ( 616,                   "Rain and snow", "13" )
    LIGHT_SHOWER_SNOW          = ( 620,               "Light snow shower", "13" )
    SHOWER_SNOW                = ( 621,                     "Snow shower", "13" )
    HEAVY_SHOWER_SNOW          = ( 622,               "Heavy snow shower", "13" )

    # Atmospheric
    MIST                       = ( 701,                            "Mist", "50" )
    SMOKE                      = ( 711,                           "Smoke", "50" )
    HAZE                       = ( 721,                            "Haze", "50" )
    DUST_WHIRL                 = ( 731,                     "Dust Whirls", "50" )
    FOG                        = ( 741,                             "Fog", "50" )
    SAND                       = ( 751,                            "Sand", "50" )
    DUST                       = ( 761,                            "Dust", "50" )
    ASH                        = ( 762,                             "Ash", "50" )
    SQUALL                     = ( 771,                          "Squall", "50" )
    TORNADO                    = ( 781,                         "Tornado", "50" )

    # Clear
    CLEAR                      = ( 800,                           "Clear", "01" )

    # Clouds
    FEW_CLOUDS                 = ( 801,                      "Few clouds", "02" )
    SCATTERED_CLOUDS           = ( 802,                "Scattered clouds", "03" )
    BROKEN_CLOUDS              = ( 803,                   "Broken clouds", "04" )
    OVERCAST                   = ( 804,                        "Overcast", "04" )

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

