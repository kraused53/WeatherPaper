from WeatherReport import WeatherReport
from GeneratePNG import generate_png
from PIL import Image
from inky import InkyWHAT

if __name__ == '__main__':
    display = InkyWHAT("red")
    display.set_border(display.WHITE)

    report = WeatherReport()
    report.generate_report()

    img = generate_png( report )
    
    pal_img = Image.new('P', (1,1))
    pal_img.putpalette((255,255,255,0,0,0,255,0,0)+(0,0,0)*252)
    img = img.convert('RGB').quantize(palette=pal_img)
    display.set_image(img)
    display.show()
