import requests

# Replace ACCESS_TOKEN with your access token
ACCESS_TOKEN = 'EAATQZBQ0Xw2UBADgE1rEbVplG4jhzxqrgGktMnq5PSJSjUicx28h7K1foHcRoqI3H7Wnu7eUg6ZCELPfvZBMbodD5QTXtKKzLUzAe75H9vboyb2jZAv1UUrB1GxqW7UQTsogm31zKWiIEimYOMoXEiyOJgAxupXl8u6PFoXE7kkBRD4Ou7NtGvXBSGcv3ugAuUKvZBW45bghrYd4ZARpYw1pkZC4JWOKZCxdHtuSodWohHKtdsPEIiYFVli5B1fSHgwZD'

# Replace EMAIL_ADDRESS with the email address of the user you want to retrieve the Facebook ID for
email_address = "rahul.v@elintdata.com"

# Define the endpoint URL
url = f"https://graph.facebook.com/search?q={email_address}&type=user&access_token={ACCESS_TOKEN}"

# Send a GET request to the endpoint
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON
    search_results = response.json()["data"]
    
    # Loop through the search results to find the user with the matching email address
    for user in search_results:
        if user["email"] == email_address:
            # If the email address matches, print the Facebook ID
            print("Facebook ID:", user["id"])
            break
else:
    # If the request was unsuccessful, print the error message
    print("Failed to retrieve data. Response code:", response.status_code)
    error = response.json()
    error_message = error['error']['message']
    error_code = error['error']['code']
    print('Error Message:', error_message)
    print('Error Code:', error_code)