import requests
import json



def get_token():
    url = "https://api.sandbox.co.in/authenticate"

    headers = {
        "accept": "application/json",
        "x-api-version": "1.0",
        "x-api-key": "",
        "x-api-secret": ""
    }

    response = requests.post(url, headers=headers)

    return json.loads(response.text)['access_token']

def get_vpa_valid(vpa):
    url = f"https://api.sandbox.co.in/bank/upi/{vpa}"

    payload = {}
    headers = {
    'Authorization': get_token(),
    'x-api-key': '',
    'x-api-version': '1.0.0'
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    return json.loads(response.text)['data']['account_exists']

if __name__ == "__main__":
    vpa = '9845107111@ybl'
    print("The UPI ID is present: ", get_vpa_valid(vpa))