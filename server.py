import requests
import json


def telegram_send_message(msg):
    try:
        bot_token = '' # Your bot token
        api = 'https://api.telegram.org/bot'
        channel = '' # Your channel id
        send_mes_api = api + bot_token + '/SendMessage?chat_id=' + channel + '&text=' + msg + '&parse_mode=HTML'
        # get target ip
        resp = requests.get(send_mes_api)
        resp_json = json.loads(resp.content.decode("utf-8"))
        if (str(resp.status_code) == '200'):
            if (str(resp_json['ok']) == 'True'):
                return True, 'successful'
            else:
                return False, 'error: failed'
        else:
            error_des = 'error code:' + str(resp_json['error_code']) + '=>description:' + str(resp_json['description'])
            return False, error_des
    except:
        return False, 'tlgm script error'
        
def telegram_get_update():
    try:
        bot_token = ''  # Your bot token
        api = 'https://api.telegram.org/'
        channel = '' # Your channel id
        get_update_api = api + bot_token + '/getupdates'
        # get update
        resp = requests.get(get_update_api)
        resp_json = json.loads(resp.content.decode("utf-8"))
        if (str(resp.status_code) == '200'):
            if (str(resp_json['ok']) == 'True'):
                return True, 'successful'
            else:
                return False, 'error: failed'
        else:
            error_des = 'error code:' + str(resp_json['error_code']) + '=>description:' + str(resp_json['description'])
            return False, error_des
    except:
        return False, 'tlgm script error'

telegram_get_update()

#script_message = '101:active'
#res_status, res_message = telegram_send_message(script_message)
#if (res_status):
#    print('successfully: message sent')
#else:
#    print('failed: send message failed =>' + res_message)
