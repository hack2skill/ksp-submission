import tweepy
import json
import time
import datetime

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def filter_tweets(tweets):
    filteredTweets = list()
    for tweet in tweets:
        filteredTweets.append({'tweet': tweet.text, 'tweet_date': tweet.created_at.now().strftime("%Y-%m-%d %H:%M:%S")})
    return filteredTweets

def get_user_information(username):
    user = api.get_user(screen_name=username)
    tweets = api.user_timeline(screen_name=username, count=200)
    sorted_tweets = sorted(tweets, key=lambda x: x.favorite_count, reverse=True)[:10]
    
    replies = list()
    top_commentors = dict()

    # Fetching list of people who interacted in last 20 tweets
    # Not the people most interacted with.
    for tweet in tweepy.Cursor(api.search_tweets,q='to:'+username, result_type='recent').items(10):
        replies.append(tweet)
    for reply in replies:
        commentor = api.get_user(screen_name=reply.user.screen_name)
        top_commentors[reply.user.screen_name] = {
            'twitter_url':'https://twitter.com/' + reply.user.screen_name,
            'twitter_profile_url': commentor.profile_image_url
        }
    data = {
        "user_id": user.id,
        "user_name": user.name,
        "user_screen_name": user.screen_name,
        "user_entities": json.dumps(user.entities),
        "user_location": json.dumps(user.location),
        "user_description": user.description,
        "user_followers_count": user.followers_count,
        "user_friends_count": user.friends_count,
        "user_created_at": user.created_at,
        "user_profile_banner": user.profile_image_url_https,
        "user_profile_image": user.profile_image_url_https,
        "user_top_tweets": json.dumps(filter_tweets(sorted_tweets)),
        "top_commentors": top_commentors
    }
    return data