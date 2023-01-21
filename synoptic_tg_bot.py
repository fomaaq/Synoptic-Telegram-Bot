import config
import telebot
import error.errors_handler as errors_handler
import service.weather_service as weather_service
import utils.data_utils as data_utils
import utils.answer_utils as answer_utils
import testing

# API key for interacting with the weather service
API_KEY = config.API_KEY

# Chat ID for logs
LOG_CHAT_ID = config.LOG_CHAT_ID

# Bot essence
bot = telebot.TeleBot(config.TOKEN)


# The bot sends a welcome message to the user
@bot.message_handler(commands=['start', 'help'])
def start(message):
    answer_utils.send_start_message(bot=bot,
                                    user_id=message.chat.id)


# The bot receives a geolocation from the user and returns weather data in this location
@bot.message_handler(content_types=['location'])
def location(message):
    if message.location is None:
        # Checking if the bot understood the user's request
        errors_handler.handle_location_is_none_error(bot=bot,
                                                     log_id=LOG_CHAT_ID,
                                                     user_id=message.chat.id,
                                                     message=message)
        return

    # Определяем параметры запроса в API
    longitude = message.location.longitude
    latitude = message.location.latitude

    # Defining request parameters in the API
    request_url = weather_service.get_service_url(longitude=longitude,
                                                  latitude=latitude,
                                                  api_key=API_KEY)

    # Sending a request to the weather service
    response = weather_service.weather_service_request(url=request_url)

    # Checking the response from the weather service
    if response.status_code != 200:
        errors_handler.handle_response_not_ok_error(bot=bot,
                                                    log_id=LOG_CHAT_ID,
                                                    user_id=message.chat.id,
                                                    response_text=response.text)
        return

    # Getting a dictionary of dictionaries from the response from the weather service
    response_dict = response.json()

    # Get data to answer the user from the dictionary
    country = data_utils.get_country(response_dict)
    location = data_utils.get_location(response_dict)
    temp_celsius = data_utils.get_temp_celsius(response_dict)
    weather_condition = data_utils.get_weather_condition(response_dict)

    # Get coordinates in degrees and minutes for a response to the user
    lon_degree, lon_min = data_utils.get_degree_and_min(coordinate=longitude)
    lat_degree, lat_min = data_utils.get_degree_and_min(coordinate=latitude)

    # Forming a response to the user
    weather_answer = answer_utils.get_weather_answer(country=country,
                                                     location=location,
                                                     temp_celsius=temp_celsius,
                                                     weather_condition=weather_condition,
                                                     lon_degree=lon_degree,
                                                     lon_min=lon_min,
                                                     lat_degree=lat_degree,
                                                     lat_min=lat_min)

    # Sending the generated response to the user
    answer_utils.send_weather(bot=bot,
                              user_id=message.chat.id,
                              weather_answer=weather_answer)


# The bot sends a message if the user sent something other than the location
@bot.message_handler(content_types=['text',
                                    'audio',
                                    'document',
                                    'photo',
                                    'sticker',
                                    'video',
                                    'video_note',
                                    'voice',
                                    'contact',
                                    'new_chat_members',
                                    'left_chat_member',
                                    'new_chat_title',
                                    'new_chat_photo',
                                    'delete_chat_photo',
                                    'group_chat_created',
                                    'supergroup_chat_created',
                                    'channel_chat_created',
                                    'migrate_to_chat_id',
                                    'migrate_from_chat_id',
                                    'pinned_message',
                                    'web_app_data'])
def wrong_user_request(message):
    answer_utils.send_wrong_user_request(bot=bot, user_id=message.chat.id)


def run_bot():
    '''
    Running tests and bot
    '''
    print('🤖 Bot is running')
    bot.infinity_polling()


# Bot launch
if __name__ == '__main__':
    testing.run_all_tests()
    run_bot()
