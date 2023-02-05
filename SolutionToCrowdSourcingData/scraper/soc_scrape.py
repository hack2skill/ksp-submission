import json
import csv
import tweepy
from tweepy import OAuthHandler
import json
from datetime import datetime
from itertools import dropwhile, takewhile

import instaloader
def twitterscraper(person):
    # Input: Username
    # Output: array of twitter images url

    query = "from:"+person+" has:media_link"
    tweets = client.search_recent_tweets(query=query,
                                        media_fields=['url'],
                                        expansions='attachments.media_keys',
                                        max_results=10)
    if 'media' in tweets.includes:

        # Get list of media from the includes object
        media = {m["media_key"]: m for m in tweets.includes['media']}
        imglist=[]
        for tweet in tweets.data:
            try:
                attachments = tweet.data['attachments']
                media_keys = attachments['media_keys']
                for i in range(len(media_keys)):
                    if media[media_keys[i]].url:
                        image_url = media[media_keys[i]].url
                        imglist.append(image_url)
            except:
                pass
        return imglist
    else:
        return -1
def instascraper(person):
    # Input: Person
    # Output: tuple 
    # tuple[0]:insta images
    # tuple[1]: insta videos
    
    L = instaloader.Instaloader()

    posts = instaloader.Profile.from_username(L.context, person).get_posts()
    i =0
    videos=[]
    imgs=[]
    try:
        for post in posts:
            try:
                if post.is_video:
                    videos.append(post.video_url)
                else:
                    imgs.append(post.url)
            except:
                return (imgs,videos)
            i+=1
            if i==15:
                break
    except:
        pass
    finally:
        return (imgs,videos)
import facebook_scraper as fb
def fbscraper(person):
    i=0
    imgs=[]
    videos=[]
    for post in fb.get_posts("narendramodi",cookies="scraper/facebook.com_cookies.txt"): 
        if i==5:
            break
        if post['video']:

            
            videos.append(post['video'])
        elif post['image']:
            imgs.append(post['image'])
        i+=1
        print(i)
    
    return (imgs,videos)
        
from truecallerpy import search_phonenumber

# def truecaller(Phone):
    
#     try:
#         # id = "a1i0v--dRz1TIV3VsEutLD9CHF-_zejj5McgSGc_zxDpkW-IRlmLi2OkI6fxTaaQ"
#         import ppic
#         id = "a1i0v--dRz1TIV3VsEutLD9CHF-_zejj5McgSGc_zxDpkW-IRlmLi2OkI6fxTaaQ"
#         dataph=dict(search_phonenumber(Phone,"IN", id))
#         naam=dataph['data'][0]['name']
#         #if username==NULL call main function using truecaller
#         return [dataph,naam]
#         # return(str(search_phonenumber(Phone,"IN", id)))

#     except:
#         return -1

def truecaller(Phone):
    try:
        id = ""
        dataph=dict(search_phonenumber(Phone,"IN", id))
        naam=dataph['data'][0]['name']
        photu=dataph['data'][0]['image']
        retarr=[]
        p=dataph
        p=json.dumps(p,indent=2)
        retarr.append(p)
        retarr.append(naam)
        if photu:
            retarr.append(photu)
        #if username==NULL call main function using truecaller
        return retarr
    except:
        return -1

print(fbscraper('elonmusk'))



    

    

