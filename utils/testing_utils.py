'''
The module contains methods for testing utils.
'''


def test_log(is_success, test_title):
    '''
    Getting test log
    '''
    if is_success:
        test_status = '🟢'
    else:
        test_status = '🔴'

    print(test_status, test_title)
