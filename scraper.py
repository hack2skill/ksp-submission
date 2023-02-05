#instagram scraping
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

#twitter scraping
import tweepy

# Setup Twitter API authentication
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Initialize API client
api = tweepy.API(auth)

# Define the geolocation and time parameters
geocode = "37.781157,-122.398720,1km"  # latitude, longitude, radius (here 1 km radius around San Francisco)
since_id = None  # ID of the tweet after which to start collecting tweets
max_id = -1  # ID of the tweet before which to stop collecting tweets
count = 100  # Number of tweets to retrieve per request

# Collect public tweets based on geolocation and time
tweets = []
while len(tweets) < count:
    try:
        new_tweets = api.search(geocode=geocode, since_id=since_id, max_id=max_id, count=count)
        tweets.extend(new_tweets)
        max_id = new_tweets[-1].id
    except tweepy.errors.TweepException as e:
        print("Error : " + str(e))
        break

# Print the collected tweets
for tweet in tweets:
    print(tweet.text)
