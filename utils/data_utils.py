'''
The module contains methods for processing data received from the weather service
'''


def get_country(data: dict) -> str:
    '''
    Getting a country from a dictionary
    '''
    return data['sys']['country']


def get_location(data: dict) -> str:
    '''
    Getting a location from a dictionary
    '''
    return data['name']


def get_temp_celsius(data: dict) -> str:
    '''
    Getting temperature in degrees Celsius from a dictionary
    '''
    temp_kelvin = data['main']['temp']
    temp_celsius = temp_kelvin - 273.15
    temp_celsius_rounded = int(temp_celsius)
    return str(temp_celsius_rounded)


def get_weather_condition(data: dict) -> str:
    '''
    Getting the weather status from the dictionary
    '''
    weather_condition = data['weather'][0]['main']
    weather_condition_lower = weather_condition.lower()
    return weather_condition_lower


def get_degree_and_min(coordinate: float) -> tuple:
    '''
    Getting coordinates in degrees and minutes from the dictionary
    '''
    coordinate_degree = int(coordinate)
    coordinate_min = int(round(coordinate % 1, 2) * 100)
    return coordinate_degree, coordinate_min
