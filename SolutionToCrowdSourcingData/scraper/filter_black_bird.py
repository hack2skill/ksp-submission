import json
import csv
import tweepy
from tweepy import OAuthHandler
import json
 


def filter_BB(person):
    with open("results/"+person+".json", "r") as file:
    # Load the JSON data from the file
        data = json.load(file)
    
    # Now data is a dictionary
    data=data["sites"]
    valued=dict()
    for i in data:
        #print(i)
        if i['response-status']=="200 OK" and i['status']=="FOUND":
            valued[i['app']]=i

    with open("results/1"+person+".json", "w") as file:
    # Load the JSON data from the file
        json.dump(valued,file,indent=4)
    # query = 'from:elonmusk has:media_link'
    # tweets = client.search_recent_tweets(query=query,
    #                                     media_fields=['url'],
    #                                     expansions='attachments.media_keys',
    #                                     max_results=10)
    # if 'media' in tweets.includes:

    #     # Get list of media from the includes object
    #     media = {m["media_key"]: m for m in tweets.includes['media']}

    #     for tweet in tweets.data:
    #         try:
    #             attachments = tweet.data['attachments']
    #             print(attachments)
    #             media_keys = attachments['media_keys']
    #             for i in range(len(media_keys)):
    #                 if media[media_keys[i]].url:
    #                     image_url = media[media_keys[i]].url
    #                     print(image_url)
    #         except:
    #             pass
    # else:
    #     print('No images found for this search query')
