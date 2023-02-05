from twitter_scraper import get_tweets
from flask import Flask, jsonify, request
from facebook_scraper import get_profile
import snscrape.modules.twitter as sntwitter
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# set_cookie(cookies_file)
cookies_file = ("./cookies.txt")

# Facebook Profile Scraper
@app.route("/facebook/profile", methods=['POST'])
def get_facebook_profile():
    username = request.json['username']
    profile_info = get_profile(username, cookies=cookies_file)
    return jsonify(profile_info), 200


# Twitter Profile Scraper
@app.route("/twitter/profile", methods=['POST'])
def get_twitter_profile():
    twitter_username = request.json['twitter_username']
    twitter_scraper = sntwitter.TwitterUserScraper(twitter_username)
    twitter_profile_data = twitter_scraper._get_entity()
    return jsonify(twitter_profile_data), 200


# Twitter Tweets Scraper
@app.route("/twitter/tweets", methods=['POST'])
def get_twitter_tweets():
    tweets = []
    twitter_username = request.json['twitter_username']
    for tweet in sntwitter.TwitterSearchScraper(twitter_username).get_items():
        tweets.append([tweet.date, tweet.username, tweet.content, tweet.links])
    return jsonify(tweets), 200    


if __name__ == '__main__':
    app.run(debug=True)
