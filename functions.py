import random
import string

from slacker import Slacker


def random_number_string():
    string_pool = string.ascii_lowercase + string.digits
    result = ''
    for i in range(8):
        result += random.choice(string_pool)

    return result


def slack_notification(text):
    token = 'xoxb-655104279252-1190224430311-cxgIfApkBXsjdWB4Rl3WtnUb'
    channel = '#anellocoin-noti'
    # log_data(text)
    slack = Slacker(token=token)
    slack.chat.post_message(
        channel=channel,
        text=text
    )