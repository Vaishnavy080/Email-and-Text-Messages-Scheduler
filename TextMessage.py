import requests
import json
API_ENDPOINT = "https://api.sms-magic.com/v1/sms/send"
msg_delivery_status_url = 'https://api.sms-magic.com/v1/sms/status'
API_KEY = "54b197ee146649517b9e5b47172cd1ee"

# data to be sent to api

def send_sms_get(number,msg):
    headers = {'apiKey': API_KEY}
    send_sms_data = {'mobile_number': number,
                     'sms_text': msg,
                     'sender_id': 'testSenderIDSMSMagic'}
    response_get = requests.request("GET", API_ENDPOINT, headers=headers, params=send_sms_data)
    return response_get

def send_sms_post(number,body):
    payload = {'mobile_number': number,
                     'sms_text' : body,
                     'sender_id' : 'testSenderIDSMSMagic'}
    headers3 = {'apiKey': API_KEY,
                'content-type': "application/x-www-form-urlencoded",
    }
    response_post = requests.request("POST", API_ENDPOINT, data=payload, headers=headers3)
    res = json.loads(response_post.text)
    get_id = res["id"]
    return get_id


