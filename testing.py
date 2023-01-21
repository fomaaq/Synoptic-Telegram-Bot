'''
The module contains methods for unit tests.
'''
import utils.testing_utils as testing_utils
import service.weather_service as weather_service
import utils.data_utils as data_utils


def run_all_tests():
    '''
    Running all testing methods
    '''
    test_get_service_url_default_values()
    test_get_service_url_empty_values()
    test_get_temp_celsius_default_values()
    test_get_temp_celsius_minimal_values()
    test_get_weather_condition_clear()
    test_get_weather_condition_rain()
    test_get_degree_and_min_default_values()
    test_get_degree_and_min_empty_values()


def test_get_service_url_default_values():
    '''
    Running get_service_url test with default values
    '''
    longitude = 44.22
    latitude = 55.33
    api_key = 'testing_api_key'

    expected_result = 'https://api.openweathermap.org/data/2.5/weather?lat=55.33&lon=44.22&appid=testing_api_key'

    actual_result = weather_service.get_service_url(longitude=longitude,
                                                    latitude=latitude,
                                                    api_key=api_key)

    test_result = expected_result == actual_result

    testing_utils.test_log(is_success=test_result,
                           test_title='test_get_service_url_default_values')


def test_get_service_url_empty_values():
    '''
    Running get_service_url test with empty values
    '''
    longitude = 0.00
    latitude = -0.01
    api_key = ''

    expected_result = 'https://api.openweathermap.org/data/2.5/weather?lat=-0.01&lon=0.0&appid='

    actual_result = weather_service.get_service_url(longitude=longitude,
                                                    latitude=latitude,
                                                    api_key=api_key)

    test_result = expected_result == actual_result

    testing_utils.test_log(is_success=test_result,
                           test_title='test_get_service_url_empty_values')


def test_get_temp_celsius_default_values():
    '''
    Running get_temp_celsius test with default values
    '''
    test_data = {'main': {'temp': 300.12}}

    expected_result = '26'

    actual_result = data_utils.get_temp_celsius(data=test_data)

    test_result = expected_result == actual_result

    testing_utils.test_log(is_success=test_result,
                           test_title='test_get_temp_celsius_default_values')


def test_get_temp_celsius_minimal_values():
    '''
    Running get_temp_celsius test with minimal values
    '''
    test_data = {'main': {'temp': 0}}

    expected_result = '-273'

    actual_result = data_utils.get_temp_celsius(data=test_data)

    test_result = expected_result == actual_result

    testing_utils.test_log(is_success=test_result,
                           test_title='test_get_temp_celsius_minimal_values')


def test_get_weather_condition_clear():
    '''
    Running get_weather_condition test with 'clear'
    '''
    test_data = {'weather': [{'main': 'Clear'}]}

    expected_result = 'clear'

    actual_result = data_utils.get_weather_condition(data=test_data)

    test_result = expected_result == actual_result

    testing_utils.test_log(is_success=test_result,
                           test_title='test_get_weather_condition_clear')


def test_get_weather_condition_rain():
    '''
    Running get_weather_condition test with 'rain'
    '''
    test_data = {'weather': [{'main': 'Rain'}]}

    expected_result = 'rain'

    actual_result = data_utils.get_weather_condition(data=test_data)

    test_result = expected_result == actual_result

    testing_utils.test_log(is_success=test_result,
                           test_title='test_get_weather_condition_rain')


def test_get_degree_and_min_default_values():
    '''
    Running get_degree_and_min test with default values
    '''
    test_coordinate = 12.3456789

    expected_result_degree = 12
    expected_result_min = 35

    actual_result_degree, actual_result_min = data_utils.get_degree_and_min(coordinate=test_coordinate)

    test_result = expected_result_degree == actual_result_degree and expected_result_min == actual_result_min

    testing_utils.test_log(is_success=test_result,
                           test_title='test_get_degree_and_min_default_values')


def test_get_degree_and_min_empty_values():
    '''
    Running get_degree_and_min test with empty values
    '''
    test_coordinate = 0.0

    expected_result_degree = 0
    expected_result_min = 0

    actual_result_degree, actual_result_min = data_utils.get_degree_and_min(coordinate=test_coordinate)

    test_result = expected_result_degree == actual_result_degree and expected_result_min == actual_result_min

    testing_utils.test_log(is_success=test_result,
                           test_title='test_get_degree_and_min_empty_values')
