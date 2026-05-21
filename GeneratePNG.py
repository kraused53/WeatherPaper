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
CUR_TEMP_Y = 115
DESC_X = 300
DESC_Y = 165
HUM_X = 300
HUM_Y = 165
WIND_X = 300
WIND_Y = 195
WIND_DIR_X = 300
WIND_DIR_Y = 225
TEMP_MIN_X = 50
FOOTER_TITLE_Y = 255
FOOTER_DATA_Y = 285
FOOTER_CENTER_X = 200
TEMP_MAX_X = 350

# Fonts
FONT_DIR = "fonts/"

def generate_png( report: WeatherReport ) -> Image.Image:
    img = Image.new( 'RGBA',  (IM_W, IM_H ), ( 255, 255, 255 ) )
    draw = ImageDraw.Draw(img)

    icon = Image.open( ICON_DIR + report.get_icon() ).resize((ICON_SIZE, ICON_SIZE))
    convert_icon_background( icon )
    img.paste( icon, ( ICON_X, ICON_Y ) )

    add_middle_anchor_text_to_image( f"{datetime.now().strftime( '%I:%M %p' )}", TIME_X, TIME_Y, 40, draw )
    add_middle_anchor_text_to_image( f"{report.temp_cur}{report.temp_units}", CUR_TEMP_X, CUR_TEMP_Y, 40, draw )
    add_middle_anchor_text_to_image( f"{report.weather_description}", DESC_X, DESC_Y, 20, draw )
    add_middle_anchor_text_to_image( f"Low", TEMP_MIN_X, FOOTER_TITLE_Y, 16, draw )
    add_middle_anchor_text_to_image( f"{report.temp_min}{report.temp_units}", TEMP_MIN_X, FOOTER_DATA_Y, 16, draw )
    add_middle_anchor_text_to_image( f"{report.humidity}{report.humidity_units} Humidity", FOOTER_CENTER_X, FOOTER_TITLE_Y, 16, draw )
    add_middle_anchor_text_to_image( f"{report.wind_speed} {report.wind_speed_units} Winds", FOOTER_CENTER_X, FOOTER_DATA_Y, 16, draw )
    add_middle_anchor_text_to_image( f"High", TEMP_MAX_X, FOOTER_TITLE_Y, 16, draw )
    add_middle_anchor_text_to_image( f"{report.temp_max}{report.temp_units}", TEMP_MAX_X, FOOTER_DATA_Y, 16, draw )

    # Add Grid Lines
    draw.line([(0,  40), (400,  40)], fill="black", width=1, joint=None)
    draw.line([(0, 240), (400, 240)], fill="black", width=1, joint=None)
    draw.line([(200, 40), (200, 240)], fill="black", width=1, joint=None)
    draw.line([(100, 240), (100, 300)], fill="black", width=1, joint=None)
    draw.line([(300, 240), (300, 300)], fill="black", width=1, joint=None)

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