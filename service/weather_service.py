'''
The module contains methods for generating and sending a request to the server
'''
import requests


def get_service_url(longitude, latitude, api_key) -> str:
    '''
    Forming a request for the weather service
    '''
    return f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'


def weather_service_request(url: str) -> requests.Response:
    '''
    Sending a request to the weather service
    '''
    return requests.get(url)
