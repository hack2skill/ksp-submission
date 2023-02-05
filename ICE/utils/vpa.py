import requests
import json

def get_token():
    url = "https://api.sandbox.co.in/authenticate"

    response = requests.post(url, headers=headers)

    return json.loads(response.text)['access_token']

def get_vpa_valid(vpa):
    try:

        url = f"https://api.sandbox.co.in/bank/upi/{vpa}"

        payload = {}

        response = requests.request("GET", url, headers=headers, data = payload)
        print(response.text)
        return json.loads(response.text)['data']['account_exists']
    except Exception as e:
        print(e)
        return False
def get_validity_for_all_vpaIds(phoneNumber: str) -> dict:
    VPAS = {
        'phonepe': ['@ybl','@ibl'],
        'paytm': ['@paytm']
    }

    result = dict()
    for provider in VPAS:
        isValid = False
        for vpa in VPAS[provider]:
            print(phoneNumber + vpa)
            isValid = isValid or get_vpa_valid(phoneNumber + vpa)

        result[provider] = {
            'isAvailable': isValid
        }
    
    return result