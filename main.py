from WeatherCodes import WeatherCodes
from WeatherReport import WeatherReport


def main( r: WeatherReport ):
    print( r.get_url() )

if __name__ == '__main__':
    report = WeatherReport()
    main( report )

    code = WeatherCodes.from_id( 310 )
    print( code )

    code = WeatherCodes.from_id( 800 )
    print( code )

    code = WeatherCodes.from_id( 999 )
    print( code )