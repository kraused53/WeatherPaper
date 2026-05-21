from WeatherReport import WeatherReport
from GeneratePNG import generate_png
from PIL import Image

if __name__ == '__main__':
    report = WeatherReport()
    report.generate_report()

    img = generate_png( report )
    img.show()