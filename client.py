import requests
import json


def telegram_get_update(license_number):
    try:
        bot_token = '' # Your bot token
        api = 'https://api.telegram.org/bot'
        channel = '' # Your channel id
        get_update_api = api + bot_token + '/getupdates?chat_id='+channel
        # get update
        resp = requests.get(get_update_api)
        result_json = resp.json()
        if (str(resp.status_code) == '200'):
            if (str(result_json["ok"]) == 'True'):
                return True, result_json["result"]
            else:
                return False, 'error: failed'
        else:
            error_des = 'error code:' + str(resp_json['error_code']) + '=>description:' + str(resp_json['description'])
            return False, error_des
    except:
        return False, 'tlgm script error'

def check_license(license_number):
    try:
        res_status, res_message = telegram_get_update(license_number)
        if (res_status):
            last_element = res_message[-1]
            if "message" in last_element.keys():   
                if "text" in last_element["message"].keys():
                    license_list_str=last_element["message"]["text"]
                    if(license_list_str!=''):
                        license_list_array=license_list_str.split(",")
                        if(license_list_array[0]=='license'):
                            if license_number in license_list_array:
                                return True, 'active license'
                            else:
                                return False, 'deactive license'
                        else:
                            return False, 'not found license list'
                    else:
                        return False, 'text is null'
                else:
                    return False, 'not found text'
            else:
                return False, 'not found message'
        else:
            return False, 'failed: ' + res_message
    except:
        return False, 'Eroor 103'
    
    
license_number='340' # change this
res_status, res_message = check_license(license_number)
print(res_status)
print(res_message)