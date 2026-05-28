import configparser

_config = configparser.ConfigParser()
_config.read('secrets.ini')

def get_lat():
    return _config.get('Location', 'lat')

def get_lon():
    return _config.get('Location', 'lon')
