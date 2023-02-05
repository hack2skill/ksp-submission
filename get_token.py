import requests

# Replace APP_ID and APP_SECRET with your Facebook app ID and app secret
APP_ID = '586953412840539'
APP_SECRET = 'ca66efcb3b4f8f22b43803e45a51b86f'

# Define the endpoint for getting an access token
endpoint = f'https://graph.facebook.com/v9.0/oauth/access_token?client_id={APP_ID}&client_secret={APP_SECRET}&grant_type=client_credentials'

# Make a GET request to the endpoint
response = requests.get(endpoint)

# Check if the request was successful
if response.status_code == 200:
    # If successful, extract the access token from the response
    data = response.json()
    access_token = data['access_token']
    print('Access Token:', access_token)
else:
    # If the request failed, print an error message
    print('Request failed with status code:', response.status_code)
