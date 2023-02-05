import requests
from typing import Dict
authkey = creds['auth']

def numsearch(num:str, authkey = authkey) -> Dict:
    """Searches the given number through TrueCaller Directory and returs the details of the given user

    Args:
        num (str): "Number to be searched in the directory format '<COUNTRYCODE>NUMBER'"
        authkey (_type_, optional): Defaults to authkey.

    Returns:
        OUTPUT (Dict): {'name': 'Raghav Maheshwari', 'gender': 'UNKNOWN', 
        'address': [{'address': 'IN', 'city': 'Uttar Pradesh West', 'countryCode': 'IN', 'timeZone': '+05:30', 'type': 'address'}], 
         'email': 'raghav.ddps2@gmail.com'}
    """
    params = {'q':num, 'countryCode':'', 'type':'4', 'locAddr':'', 'placement':'SEARCHRESULTS,HISTORY,DETAILS', 'encoding':'json'}
    resp = requests.get('https://search5-noneu.truecaller.com/v2/search', headers=headers, params=params)
    resp = resp.json()

    out = {"name":"","gender":"","address":[],"image":"","email":""}
    if resp['data'][0].get('name'):
        out["name"] = resp["data"][0]["name"]
    if resp['data'][0].get('gender'):
        out["gender"] = resp["data"][0]["gender"]
    if resp['data'][0].get('addresses'):
        out["address"] = resp["data"][0]["addresses"]
    if resp['data'][0].get('image'):
        out["image"] = resp["data"][0]["image"]
    if resp['data'][0].get('phones'):
        if "carrier" in resp['data'][0]["phones"][0]:
            out["carrier"] = resp["data"][0]["phones"][0]["carrier"]
    if resp['data'][0].get('internetAddresses'):
        if "id" in resp["data"][0]["internetAddresses"][0]:
            out["email"] = resp["data"][0]["internetAddresses"][0]["id"]

    return out

if __name__=='__main__':
    output = numsearch(lnum)
    print(output)
 

