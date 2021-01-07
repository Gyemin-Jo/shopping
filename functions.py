import datetime
import locale
import random
import string

from babel.numbers import format_number
from slacker import Slacker


def random_number_string():
    string_pool = string.ascii_lowercase + string.digits
    result = ''
    for i in range(8):
        result += random.choice(string_pool)

    return result

def number_format(value, locale_=None):
    if value and value != '0' and value > 0:
        if locale_ is None:
            locale_ = locale.getlocale()[0]
        return format_number(value, locale=locale_)
    else:
        return 0.0


def date_format(value, format='-'):
    date = datetime.fromtimestamp(value)
    if format == '-':
        return date
    elif format == 'kr':
        return date.strptime(date, '%Y-%m-%d %H:%M:%S')

    return value


def slack_notification(text):
    token = 'xoxb-655104279252-1190224430311-cxgIfApkBXsjdWB4Rl3WtnUb'
    channel = '#anellocoin-noti'
    # log_data(text)
    slack = Slacker(token=token)
    slack.chat.post_message(
        channel=channel,
        text=text
    )