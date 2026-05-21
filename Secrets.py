import configparser

def get_lat():
    config = configparser.ConfigParser()
    config.read('secrets.ini')
    return config.get('Location', 'lat')

def get_lon():
    config = configparser.ConfigParser()
    config.read('secrets.ini')
    return config.get('Location', 'lon')

def get_key():
    config = configparser.ConfigParser()
    config.read('secrets.ini')
    return config.get( 'Key', 'api_key' )

def get_units():
    config = configparser.ConfigParser()
    config.read('secrets.ini')
    return config.get( 'Settings', 'units' )