import requests

# Replace ACCESS_TOKEN with your Facebook access token
ACCESS_TOKEN = 'EAATQZBQ0Xw2UBADgE1rEbVplG4jhzxqrgGktMnq5PSJSjUicx28h7K1foHcRoqI3H7Wnu7eUg6ZCELPfvZBMbodD5QTXtKKzLUzAe75H9vboyb2jZAv1UUrB1GxqW7UQTsogm31zKWiIEimYOMoXEiyOJgAxupXl8u6PFoXE7kkBRD4Ou7NtGvXBSGcv3ugAuUKvZBW45bghrYd4ZARpYw1pkZC4JWOKZCxdHtuSodWohHKtdsPEIiYFVli5B1fSHgwZD'

# # Define the endpoint you want to access
endpoint = 'https://graph.facebook.com/v9.0/me?fields=id,name&access_token=' + ACCESS_TOKEN

# Make a GET request to the endpoint
response = requests.get(endpoint)

# Check if the request was successful
if response.status_code == 200:
    # If successful, extract the data from the response
    data = response.json()
    print(data)
else:
    # If the request failed, print an error message
    print('Request failed with status code:', response.status_code)



# Replace USER_ID with the Facebook ID of the user you want to retrieve data for
user_id = data["id"]
user_id = '100086603361203'

# Define the endpoint URL
url = f"https://graph.facebook.com/v12.0/{user_id}?fields=name,picture&access_token={ACCESS_TOKEN}"

# Send a GET request to the endpoint
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON
    user_data = response.json()
    
    # Extract the name and picture URL from the response
    name = user_data["name"]
    picture_url = user_data["picture"]["data"]["url"]
    
    # Print the name and picture URL
    print("Name:", name)
    print("Picture URL:", picture_url)
else:
    # If the request was unsuccessful, print the error message
    print("Failed to retrieve data. Response code:", response.status_code)

# import requests

# # Replace ACCESS_TOKEN with your Facebook access token
# ACCESS_TOKEN = 'your-access-token'

# Replace EMAIL with the email address of the Facebook user you want to search for
# EMAIL = 'rahul.v@elintdata.com'

# # Define the endpoint for the Facebook Graph API
# endpoint = f'https://graph.facebook.com/v9.0/search?q={EMAIL}&type=user&fields=id,name&access_token={ACCESS_TOKEN}'

# # Make a GET request to the endpoint
# response = requests.get(endpoint)
# print(response)
# # Check if the request was successful
# if response.status_code == 200:
#     # If successful, extract the data from the response
#     data = response.json()
#     users = data['data']
#     if len(users) > 0:
#         user = users[0]
#         user_id = user['id']
#         user_name = user['name']
#         print('User ID:', user_id)
#         print('User Name:', user_name)
#     else:
#         print('No user found with that email address')
# else:
#     # If the request failed, print an error message
#     print('Request failed with status code:', response.status_code)
#     if response.status_code == 400:
#         # If so, extract the error information from the response
#         error = response.json()
#         error_message = error['error']['message']
#         error_code = error['error']['code']
#         print('Error Message:', error_message)
#         print('Error Code:', error_code)

