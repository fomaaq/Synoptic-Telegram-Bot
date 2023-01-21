'''
The module contains methods for error handling, sending logs, and sending error messages to the user.
'''


def _handle_error(bot, log_id, log_message, user_id, user_message):
    '''
    Handle the error and sends the log and response to the user
    '''
    bot.send_message(log_id, log_message)
    bot.send_message(user_id, user_message)


def handle_location_is_none_error(bot, log_id, user_id, message):
    '''
    Handle the error 'location is None'
    '''
    _handle_error(bot=bot,
                  log_id=log_id,
                  log_message=f'Кто-то решил сломать бота:\n{message}',
                  user_id=user_id,
                  user_message='I didn\'t understand you, please send me the location')


def handle_response_not_ok_error(bot, log_id, user_id, response_text):
    '''
    Handle the error 'response is not ok'
    '''
    _handle_error(bot=bot,
                  log_id=log_id,
                  log_message=f'Бот сломался с ошибкой:\n\n{response_text}',
                  user_id=user_id,
                  user_message='The bot decided to rest, please wait until it wakes up')
