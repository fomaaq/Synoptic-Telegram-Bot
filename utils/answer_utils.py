'''
The module contains methods for creating and sending responses to the user
'''


def send_start_message(bot, user_id):
    '''
    Sends a welcome message to the user
    '''
    bot.send_message(user_id, 'Hey👋\nI will tell you the weather by geolocation sent via telegram')


def get_weather_answer(country,
                       location,
                       temp_celsius,
                       weather_condition,
                       lon_degree,
                       lon_min,
                       lat_degree,
                       lat_min) -> str:
    '''
    Generates a response for the user in the required format
    '''
    return f"📍{country}, {location}\n" + \
        f"🌡️ Temperature: {temp_celsius} °C\n" + \
        f"🌤 Weather: {weather_condition}\n\n" + \
        f"🌐 Coordinates: {lon_degree}°{lon_min}' {lat_degree}°{lat_min}'"


def send_weather(bot, user_id, weather_answer):
    '''
    Sends the generated response to the user
    '''
    bot.send_message(user_id, weather_answer)


def send_wrong_user_request(bot, user_id):
    '''
    Sends a message to the user about the inability to work with anything other than geolocation
    '''
    bot.send_message(user_id, 'I can only work with geolocation 😒 Don\'t send me something else')
