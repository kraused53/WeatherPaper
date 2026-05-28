import json
from PIL.ImageDraw import ImageDraw
import PyLog
from PIL import Image, ImageDraw, ImageFont
import FileManagement
from WeatherData import WeatherData
from datetime import datetime

# Image Settings
_png_width  = 400
_png_height = 300

# Icon Settings
ICON_SIZE = 200
ICON_DIR = "icons/"
ICON_X = 0
ICON_Y = 40

# Font Settings
FONT_DIR = "fonts/"

# Forecast PNG Settings
_png_dir = "PNGs/"
_current_name = "current.png"
_today_name = "today.png"
_tomorrow_name = "tomorrow.png"

# Text locations
TIME_X = 200
TIME_Y = 20
CENTER_RIGHT_UPPER_X = 300
CENTER_RIGHT_UPPER_Y = 95
CENTER_RIGHT_UPPER_TITLE_Y = 40
CENTER_RIGHT_LOWER_X = 300
CENTER_RIGHT_LOWER_Y = 195
CENTER_RIGHT_LOWER_TITLE_Y = 150
HUM_X = 300
HUM_Y = 165
WIND_X = 300
WIND_Y = 195
WIND_DIR_X = 300
WIND_DIR_Y = 225
FOOTER_TITLE_Y = 255
FOOTER_DATA_Y = 285
FOOTER_LEFT_X = 50
FOOTER_CENTER_LEFT_X = 150
FOOTER_CENTER_RIGHT_X = 250
FOOTER_RIGHT_X = 350

# Fetch an up-to-date weather forecast
def get_forecast() -> dict:
    PyLog.log( "Loading JSON for PNG Generation" )
    json_str = FileManagement.get_forecast()
    return json.loads(json_str)

# Create a PNG for the current weather
def create_current_png( wd: WeatherData ) -> None:
    PyLog.log( f"Generating current weather PNG" )
    img = Image.new( 'RGBA',  ( _png_width, _png_height ), ( 255, 255, 255 ) )
    draw = ImageDraw.Draw( img )

    # Fetch the correct icon from storage
    icon = Image.open( ICON_DIR + get_icon_from_weather_code(
        wd.current_weather_code(),
        wd.is_day()
    ) ).resize( ( ICON_SIZE, ICON_SIZE ) )
    # Remove icon background
    convert_icon_background( icon )
    # Add Icon to image
    img.paste(icon, (ICON_X, ICON_Y))

    # Add time stamp for when forecast was generated
    add_middle_anchor_text_to_image(justify_two_strings_to_width( f"{datetime.fromtimestamp( wd.time() ).strftime('%I:%M %p')}", "Current", 18 ), TIME_X, TIME_Y, 35, draw)

    # Add current temperature
    add_y_centered_text_to_image(f"Temperature", CENTER_RIGHT_UPPER_X, CENTER_RIGHT_UPPER_TITLE_Y, 16, draw)
    add_middle_anchor_text_to_image(f"{wd.current_temperature()}{wd.current_temperature_units()}", CENTER_RIGHT_UPPER_X, CENTER_RIGHT_UPPER_Y, 40, draw)

    # Add current precipitation chance
    add_y_centered_text_to_image(f"Precipitation", CENTER_RIGHT_LOWER_X, CENTER_RIGHT_LOWER_TITLE_Y, 16, draw)
    add_middle_anchor_text_to_image(f"{wd.current_precip_chance()}{wd.current_precip_chance_units()}", CENTER_RIGHT_LOWER_X, CENTER_RIGHT_LOWER_Y, 30, draw)

    # Add current humidity
    add_middle_anchor_text_to_image("Humidity", FOOTER_LEFT_X, FOOTER_TITLE_Y, 16, draw)
    add_middle_anchor_text_to_image(f"{wd.current_humidity()}{wd.current_humidity_units()}", FOOTER_LEFT_X, FOOTER_DATA_Y, 16, draw)

    # Add current cloud cover
    add_middle_anchor_text_to_image("Clouds", FOOTER_CENTER_LEFT_X, FOOTER_TITLE_Y, 16, draw)
    add_middle_anchor_text_to_image(f"{wd.current_cloud_cover()}{wd.current_cloud_cover_units()}", FOOTER_CENTER_LEFT_X, FOOTER_DATA_Y, 16, draw)

    # Add current wind
    add_middle_anchor_text_to_image("Wind", FOOTER_RIGHT_X + int((FOOTER_CENTER_RIGHT_X - FOOTER_RIGHT_X) / 2), FOOTER_TITLE_Y, 16, draw)
    add_middle_anchor_text_to_image(f"{wd.current_wind_speed()} {wd.current_wind_speed_units()}", FOOTER_RIGHT_X, FOOTER_DATA_Y, 16, draw)
    add_middle_anchor_text_to_image(f"{wd.current_wind_direction()}°", FOOTER_CENTER_RIGHT_X, FOOTER_DATA_Y, 16, draw)

    # Add grid lines
    draw.line([(0, 40), (400, 40)], fill="black", width=1, joint=None)
    draw.line([(0, 240), (400, 240)], fill="black", width=1, joint=None)
    draw.line([(200, 150), (400, 150)], fill="black", width=1, joint=None)
    draw.line([(200, 40), (200, 240)], fill="black", width=1, joint=None)
    draw.line([(100, 240), (100, 300)], fill="black", width=1, joint=None)
    draw.line([(200, 240), (200, 300)], fill="black", width=1, joint=None)

    PyLog.log( f"Saving current weather PNG" )
    # Save image to folder
    img.save( _png_dir + _current_name )

# Create a PNG for the two-day forecast
def create_tomorrow_png( wd: WeatherData ) -> None:
    PyLog.log( f"Generating tomorrow forecast PNG" )
    img = Image.new( 'RGBA',  ( _png_width, _png_height ), ( 255, 255, 255 ) )
    draw = ImageDraw.Draw( img )

    # Fetch the correct icon from storage
    icon = Image.open( ICON_DIR + get_icon_from_weather_code(
        wd.tomorrow_weather_code(),
        True
    ) ).resize( ( ICON_SIZE, ICON_SIZE ) )
    # Remove icon background
    convert_icon_background( icon )
    # Add Icon to image
    img.paste(icon, (ICON_X, ICON_Y))

    # Add time stamp for when forecast was generated
    add_middle_anchor_text_to_image(justify_two_strings_to_width( f"{datetime.fromtimestamp( wd.time() + 600 ).strftime('%I:%M %p')}", "Tomorrow", 18 ), TIME_X, TIME_Y, 35, draw)

    # Add high temperature
    add_y_centered_text_to_image(f"High Temperature", CENTER_RIGHT_UPPER_X, CENTER_RIGHT_UPPER_TITLE_Y, 16, draw)
    add_middle_anchor_text_to_image(f"{wd.tomorrow_high_temperature()}{wd.tomorrow_high_temperature_units()}", CENTER_RIGHT_UPPER_X, CENTER_RIGHT_UPPER_Y, 40, draw)

    # Add low temperature
    add_y_centered_text_to_image(f"Low Temperature", CENTER_RIGHT_LOWER_X, CENTER_RIGHT_LOWER_TITLE_Y, 16, draw)
    add_middle_anchor_text_to_image(f"{wd.tomorrow_low_temperature()}{wd.tomorrow_low_temperature_units()}", CENTER_RIGHT_LOWER_X, CENTER_RIGHT_LOWER_Y, 40, draw)

    # Add sunrise time
    add_middle_anchor_text_to_image("Sunrise", FOOTER_LEFT_X, FOOTER_TITLE_Y, 16, draw)
    add_middle_anchor_text_to_image(f"{datetime.fromtimestamp( wd.tomorrow_sunrise() ).strftime('%I:%M %p')}", FOOTER_LEFT_X, FOOTER_DATA_Y, 16, draw)

    # Add sunset time
    add_middle_anchor_text_to_image("Sunrise", FOOTER_CENTER_LEFT_X, FOOTER_TITLE_Y, 16, draw)
    add_middle_anchor_text_to_image(f"{datetime.fromtimestamp( wd.tomorrow_sunset() ).strftime('%I:%M %p')}", FOOTER_CENTER_LEFT_X, FOOTER_DATA_Y, 16, draw)

    # Add date
    add_middle_anchor_text_to_image("Date", FOOTER_CENTER_RIGHT_X, FOOTER_TITLE_Y, 16, draw)
    add_middle_anchor_text_to_image(f"{datetime.fromtimestamp( wd.tomorrow_sunset() ).strftime('%b %d')}", FOOTER_CENTER_RIGHT_X, FOOTER_DATA_Y, 16, draw)

    # Add precipitation chance
    add_middle_anchor_text_to_image("Precip.", FOOTER_RIGHT_X, FOOTER_TITLE_Y, 16, draw)
    add_middle_anchor_text_to_image(f"{wd.tomorrow_precip_chance()}{wd.tomorrow_precip_chance_units()}", FOOTER_RIGHT_X, FOOTER_DATA_Y, 16, draw)

    # Add grid lines
    draw.line([(0, 40), (400, 40)], fill="black", width=1, joint=None)
    draw.line([(0, 240), (400, 240)], fill="black", width=1, joint=None)
    draw.line([(200, 150), (400, 150)], fill="black", width=1, joint=None)
    draw.line([(200, 40), (200, 240)], fill="black", width=1, joint=None)
    draw.line([(100, 240), (100, 300)], fill="black", width=1, joint=None)
    draw.line([(200, 240), (200, 300)], fill="black", width=1, joint=None)
    draw.line([(300, 240), (300, 300)], fill="black", width=1, joint=None)

    PyLog.log( f"Saving tomorrow forecast PNG" )
    # Save image to folder
    img.save( _png_dir + _tomorrow_name )

def create_today_png( wd: WeatherData ) -> None:
    PyLog.log( f"Generating today forecast PNG" )
    img = Image.new( 'RGBA',  ( _png_width, _png_height ), ( 255, 255, 255 ) )
    draw = ImageDraw.Draw( img )

    # Fetch the correct icon from storage
    icon = Image.open( ICON_DIR + get_icon_from_weather_code(
        wd.today_weather_code(),
        True
    ) ).resize( ( ICON_SIZE, ICON_SIZE ) )
    # Remove icon background
    convert_icon_background( icon )
    # Add Icon to image
    img.paste(icon, (ICON_X, ICON_Y))

    # Add time stamp for when forecast was generated
    add_middle_anchor_text_to_image(justify_two_strings_to_width( f"{datetime.fromtimestamp( wd.time() + 300 ).strftime('%I:%M %p')}", "Today", 18 ), TIME_X, TIME_Y, 35, draw)

    # Add high temperature
    add_y_centered_text_to_image(f"High Temperature", CENTER_RIGHT_UPPER_X, CENTER_RIGHT_UPPER_TITLE_Y, 16, draw)
    add_middle_anchor_text_to_image(f"{wd.today_high_temperature()}{wd.today_high_temperature_units()}", CENTER_RIGHT_UPPER_X, CENTER_RIGHT_UPPER_Y, 40, draw)

    # Add low temperature
    add_y_centered_text_to_image(f"Low Temperature", CENTER_RIGHT_LOWER_X, CENTER_RIGHT_LOWER_TITLE_Y, 16, draw)
    add_middle_anchor_text_to_image(f"{wd.today_low_temperature()}{wd.today_low_temperature_units()}", CENTER_RIGHT_LOWER_X, CENTER_RIGHT_LOWER_Y, 40, draw)

    # Add sunrise time
    add_middle_anchor_text_to_image("Sunrise", FOOTER_LEFT_X, FOOTER_TITLE_Y, 16, draw)
    add_middle_anchor_text_to_image(f"{datetime.fromtimestamp( wd.today_sunrise() ).strftime('%I:%M %p')}", FOOTER_LEFT_X, FOOTER_DATA_Y, 16, draw)

    # Add sunset time
    add_middle_anchor_text_to_image("Sunrise", FOOTER_CENTER_LEFT_X, FOOTER_TITLE_Y, 16, draw)
    add_middle_anchor_text_to_image(f"{datetime.fromtimestamp( wd.today_sunset() ).strftime('%I:%M %p')}", FOOTER_CENTER_LEFT_X, FOOTER_DATA_Y, 16, draw)

    # Add date
    add_middle_anchor_text_to_image("Date", FOOTER_CENTER_RIGHT_X, FOOTER_TITLE_Y, 16, draw)
    add_middle_anchor_text_to_image(f"{datetime.fromtimestamp(wd.today_sunset()).strftime('%b %d')}", FOOTER_CENTER_RIGHT_X, FOOTER_DATA_Y, 16, draw)

    # Add precipitation chance
    add_middle_anchor_text_to_image("Precip.", FOOTER_RIGHT_X, FOOTER_TITLE_Y, 16, draw)
    add_middle_anchor_text_to_image(f"{wd.today_precip_chance()}{wd.today_precip_chance_units()}", FOOTER_RIGHT_X, FOOTER_DATA_Y, 16, draw)

    # Add grid lines
    draw.line([(0, 40), (400, 40)], fill="black", width=1, joint=None)
    draw.line([(0, 240), (400, 240)], fill="black", width=1, joint=None)
    draw.line([(200, 150), (400, 150)], fill="black", width=1, joint=None)
    draw.line([(200, 40), (200, 240)], fill="black", width=1, joint=None)
    draw.line([(100, 240), (100, 300)], fill="black", width=1, joint=None)
    draw.line([(200, 240), (200, 300)], fill="black", width=1, joint=None)
    draw.line([(300, 240), (300, 300)], fill="black", width=1, joint=None)

    PyLog.log( f"Saving today forecast PNG" )
    # Save image to folder
    img.save( _png_dir + _today_name )

# Add text to image at given [ x, y ]. The text will be placed such that the y-coordinate
#     will be in the center of the text. X will be the top of the text block.
def add_y_centered_text_to_image( text: str, x: int, y: int, font_size: int, draw ) -> None:
    font = ImageFont.truetype( FONT_DIR + "font.ttf", font_size)
    x = x - int( font.getlength( text ) /2 )
    draw.text( ( x, y ), text, ( 0, 0, 0 ), font )

# Add text to image at given [ x, y ]. The text will be placed such that the x and y
#     coordinates will be in the center of the text. X will be the top of the text block.
def add_middle_anchor_text_to_image( text: str, x: int, y: int, font_size: int, draw ) -> None:
    font = ImageFont.truetype( FONT_DIR + "font.ttf", font_size)
    draw.text( ( x, y ), text, ( 0, 0, 0 ), font, anchor="mm" )

# Given two strings and a width, return a string that combines the two strings with space
#     between to pad to width. If string lengths overflow width, return strings with no
#     space between
def justify_two_strings_to_width( lstr: str, rstr: str, w: int ) -> str:
    padding = max( w - len( lstr ) - len( rstr ), 0 )
    return f"{lstr}{' '*padding}{rstr}"

# Convert image background to white pixels
def convert_icon_background(icon):
    # Break image into individual pixels
    pix = icon.load()

    # If given object is a .PNG file
    if icon.mode == 'RGBA':
        # Check every pixel in the image
        for y in range(icon.size[1]):
            for x in range(icon.size[0]):
                # If pixel has a transparency value that is anything other that solid
                if pix[x, y][3] < 255:
                    # Convert the pixel to a solid white one
                    pix[x, y] = (255, 255, 255, 255)
    # Return the adjusted image pixels
    return pix

# Convert a given weather code into the proper icon file name
def get_icon_from_weather_code( weather_code : int, is_day: bool ) -> str:
    ret = ""

    # Get icon base
    if weather_code in [1, 2, 3]:   # Clouds
        ret += "02"
    elif weather_code in [45, 48]:   # Fog
        ret += "50"
    elif weather_code in [51, 53, 55]: # Drizzle
        ret += "10"
    elif weather_code in [56, 57, 61, 63, 65, 66, 67, 80, 81, 82]: # Rain
        ret += "09"
    elif weather_code in [71, 73, 75, 77, 85, 86]: # Snow
        ret += "13"
    elif weather_code in [95, 96, 99]: # Thunderstorm
        ret += "11"
    else:
        ret += "01"

    # Adjust for day / night
    if is_day:
        ret += "d"
    else:
        ret += "n"

    # Append file type and return
    ret += ".png"
    return ret

if __name__ == '__main__':
    PyLog.log( "Generating Forecast PNGs" )
    json_data = get_forecast()
    data = WeatherData( json_data )
    create_current_png( data )
    create_today_png( data )
    create_tomorrow_png( data )