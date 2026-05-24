import configparser

import PIL
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from WeatherReport import WeatherReport

# Image size
IM_W = 400
IM_H = 300

# Icon settings
ICON_SIZE = 200
ICON_DIR = "icons/"

# Locations
TIME_X = 200
TIME_Y = 20
ICON_X = 0
ICON_Y = 40
CUR_TEMP_X = 300
CUR_TEMP_Y = 95
PRECIP_X = 300
PRECIP_Y = 195
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

# Fonts
FONT_DIR = "fonts/"

def generate_png( report: WeatherReport ) -> Image.Image:
    img = Image.new( 'RGBA',  (IM_W, IM_H ), ( 255, 255, 255 ) )
    draw = ImageDraw.Draw(img)

    icon = Image.open( ICON_DIR + get_icon_from_weather_code( report.weather_code, report.is_day ) ).resize((ICON_SIZE, ICON_SIZE))
    convert_icon_background( icon )
    img.paste( icon, ( ICON_X, ICON_Y ) )

    add_middle_anchor_text_to_image( f"{datetime.fromtimestamp( report.time ).strftime( '%I:%M %p' )}", TIME_X, TIME_Y, 40, draw )
    add_middle_anchor_text_to_image( f"{report.temperature}{report.temp_units}", CUR_TEMP_X, CUR_TEMP_Y, 40, draw )
    add_y_centered_text_to_image( f"Temperature", CUR_TEMP_X, 40, 16, draw )
    add_y_centered_text_to_image( f"Precipitation", PRECIP_X, 150, 16, draw )
    add_middle_anchor_text_to_image( f"{report.precipitation_prob}{report.precipitation_prob_units}", PRECIP_X, PRECIP_Y, 30, draw )

    add_middle_anchor_text_to_image( "Humidity", FOOTER_LEFT_X, FOOTER_TITLE_Y, 16, draw )
    add_middle_anchor_text_to_image( f"{report.humidity}{report.humidity_units}", FOOTER_LEFT_X, FOOTER_DATA_Y, 16, draw )

    add_middle_anchor_text_to_image("Wind", FOOTER_RIGHT_X + int( ( FOOTER_CENTER_RIGHT_X - FOOTER_RIGHT_X ) / 2 ), FOOTER_TITLE_Y, 16, draw)
    add_middle_anchor_text_to_image(f"{report.wind_speed} {report.wind_speed_units}", FOOTER_RIGHT_X, FOOTER_DATA_Y, 16, draw)
    add_middle_anchor_text_to_image(f"{report.wind_direction}°", FOOTER_CENTER_RIGHT_X, FOOTER_DATA_Y, 16, draw)

    add_middle_anchor_text_to_image("Clouds", FOOTER_CENTER_LEFT_X, FOOTER_TITLE_Y, 16, draw)
    add_middle_anchor_text_to_image( f"{report.cloud_cover}{report.cloud_cover_units}", FOOTER_CENTER_LEFT_X, FOOTER_DATA_Y, 16, draw )

    # Add Grid Lines
    draw.line([(0,  40), (400,  40)], fill="black", width=1, joint=None)
    draw.line([(0, 240), (400, 240)], fill="black", width=1, joint=None)
    draw.line([(200, 150), (400, 150)], fill="black", width=1, joint=None)
    draw.line([(200, 40), (200, 240)], fill="black", width=1, joint=None)
    draw.line([(100, 240), (100, 300)], fill="black", width=1, joint=None)
    draw.line([(200, 240), (200, 300)], fill="black", width=1, joint=None)

    return img

def add_y_centered_text_to_image( text: str, x: int, y: int, font_size: int, draw ) -> None:
    font = ImageFont.truetype( FONT_DIR + "font.ttf", font_size)
    x = x - int( font.getlength( text ) /2 )
    draw.text( ( x, y ), text, ( 0, 0, 0 ), font )

def add_middle_anchor_text_to_image( text: str, x: int, y: int, font_size: int, draw ) -> None:
    font = ImageFont.truetype( FONT_DIR + "font.ttf", font_size)
    draw.text( ( x, y ), text, ( 0, 0, 0 ), font, anchor="mm" )

def justify_two_strings_to_width( lstr: str, rstr: str, w: int ) -> str:
    padding = max( w - len( lstr ) - len( rstr ), 0 )
    return f"{lstr}{' '*padding}{rstr}"

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

def get_icon_from_weather_code( WeatherCode : int, isDay: bool ) -> str:
    ret = ""

    if WeatherCode in [ 1, 2, 3]:   # Clouds
        ret += "02"
    elif WeatherCode in [ 45, 48 ]:   # Fog
        ret += "50"
    elif WeatherCode in [ 51, 53, 55 ]: # Drizzle
        ret += "10"
    elif WeatherCode in [ 56, 57, 61, 63, 65, 66, 67, 80, 81, 82 ]: # Rain
        ret += "09"
    elif WeatherCode in [ 71, 73, 75, 77, 85, 86 ]: # Snow
        ret += "13"
    elif WeatherCode in [ 95, 96, 99 ]: # Thunderstorm
        ret += "11"
    else:
        ret += "01"

    if isDay:
        ret += "d"
    else:
        ret += "n"
    ret += ".png"
    return ret