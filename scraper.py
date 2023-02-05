import requests
import json
#need to go through instagram api's review process to obtain the access_token
access_token = "access_token_here"
location_id = "location_id_here"
#unix format
max_timestamp = "max_timestamp_here"

url = f"https://api.instagram.com/v1/locations/{location_id}/media/recent?access_token={access_token}&max_timestamp={max_timestamp}"

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    for post in data['data']:
        print(post['link'], post['caption']['text'], post['created_time'])
else:
    print("Request failed with status code: ", response.status_code)
