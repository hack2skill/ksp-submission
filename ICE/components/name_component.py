from math import factorial
from utils.vpa import get_validity_for_all_vpaIds
from utils.get_entities import extract_entities
from utils.utils import get_url_to_enum_dict
from providers.google import search_image
from utils.get_entities import extract_entity_string
from providers.twitter import get_user_information
from providers.google import search_text
from providers.truecaller import numsearch
import re
import gender_guesser.detector as gender
from urllib.parse import urlparse
import json
import random

def serialize_sets(obj):
    if isinstance(obj, set):
        return list(obj)

    return obj

d = gender.Detector()

def getDetailsFromName(name: str) -> dict:
    '''
        1. Call the truecaller API to get the data
        2. Call the google search API to get the data
            search_text("Raghav Maheshwari", no_of_results=10)
                Google: Name
                Google: Email
                Google: Name + Email
                Google: Name + address['city']
                Google: Name + Twitter [omitting enity here as it wil not be apt in most cases]
                Google: Name + Facebook
                Google: Name + Instagram 
                Google: Name + Linkedin
        3. Call the Twitter API using usernames from the above result.
            getEntityForDescription
            search_text("Raghav Maheshwari", no_of_results=10)
                Google: Name + entity + Facebook
                Google: Name + entity + Instagram 
                Google: Name + entity + Linkedin
    '''

    google_ts_res_plain = search_text(name, no_of_results=10)
    google_ts_res_facebook = search_text("site:facebook.com " + name, no_of_results=5)
    google_ts_res_twitter = search_text("site:twitter.com " + name, no_of_results=5)
    google_ts_res_instagram = search_text("site:instagram.com " + name, no_of_results=5)
    google_ts_res_linkedin = search_text("site:linkedin.com " + name, no_of_results=5)
    
    twitter_res = list()
    filtered_usernames = get_twitter_usernames(google_ts_res_twitter)
    for username in filtered_usernames:
        twitter_res.append(get_user_information(username))

    google_ts_res_zabuacorp = search_text(name + " Zaubacorp", no_of_results=5)
    google_ts_res_indiakanoon = search_text(name + " IndiaKanoon", no_of_results=5)

    if(len(twitter_res) > 0):
        top_tweet_desc = twitter_res[0]['user_description']
        entity_context = extract_entity_string(top_tweet_desc)
        google_ts_entity_res_facebook = search_text("site:facebook.com " + name + " " + entity_context, no_of_results=5)
        google_ts_entity_res_twitter = search_text("site:twitter.com " + name + " " + entity_context, no_of_results=5)
        google_ts_entity_res_instagram = search_text("site:instagram.com " + name + " " +entity_context, no_of_results=5)
        google_ts_entity_res_linkedin = search_text("site:linkedin.com " + name + " " + entity_context, no_of_results=5)
        google_is_entity_res_facebook = search_image("site:facebook.com " + name + " " + entity_context, no_of_results=5)
        google_is_entity_res_twitter = search_image("site:twitter.com " + name + " " + entity_context, no_of_results=5)
        google_is_entity_res_instagram = search_image("site:instagram.com " + name + " " +entity_context, no_of_results=5)
        google_is_entity_res_linkedin = search_image("site:linkedin.com " + name + " " + entity_context, no_of_results=5)
        google_is_res_entity = search_image(name + " " + entity_context, no_of_results=5)
        google_is_res_name = search_image(name, no_of_results=5)

    data =  {
        "google_ts":{
            "google_ts_res_plain": google_ts_res_plain,
            "google_ts_res_facebook": google_ts_res_facebook,
            "google_ts_res_twitter": google_ts_res_twitter,
            "google_ts_res_instagram": google_ts_res_instagram,
            "google_ts_res_linkedin": google_ts_res_linkedin,
            "google_ts_res_zabuacorp": google_ts_res_zabuacorp,
            "google_ts_res_indiakanoon": google_ts_res_indiakanoon,
            "google_ts_entity_res_facebook": google_ts_entity_res_facebook,
            "google_ts_entity_res_twitter": google_ts_entity_res_twitter,
            "google_ts_entity_res_instagram": google_ts_entity_res_instagram,
            "google_ts_entity_res_linkedin": google_ts_entity_res_linkedin
        },
        "google_is": {
            "google_is_entity_res_facebook": google_is_entity_res_facebook,
            "google_is_entity_res_twitter": google_is_entity_res_twitter,
            "google_is_entity_res_instagram": google_is_entity_res_instagram,
            "google_is_entity_res_linkedin": google_is_entity_res_linkedin,
            "google_is_res_entity": google_is_res_entity,
            "google_is_res_name": google_is_res_name,
        },
        "twitter": twitter_res,
        "name": name
    }

    return generate_response(data)


def get_twitter_usernames(search_data):
    twitter_urls = set()
    for data in search_data:
        twitter_urls.add((data['url']))
    
    return get_usernames_from_urls(twitter_urls)
    
def get_usernames_from_urls(twitter_urls):

    result = set()
    for twitter_url in twitter_urls:
        match = re.search(r'^.*?\btwitter\.com/@?(\w{1,15})(?:[?/,].*)?$',twitter_url)
        if match:
            result.add(match.group(1))
    return result


'''
name: Truecaller Data
gender: by gender guesser if not in truecaller response.
email: Truecaller Data
imageUrls: fetch all images that
    start with: https://pbs.twimg.com and https://media.licdn.com, 
    https://yt3.googleusercontent.com
tagsApplicable: we will run anirudhs function on Top 3 results from
    * Google
    * Facebook
    * Instagram
    * Linkedin
    * Twitter
    * Twitter Header
availableApps: fetchAllUrls and then check if present in the map
primaryAddress: Get it from twitter API and GLE in all the entities etc.
additionalAddress: Get it from twitter API and GLE in all the entities etc.
relatedPeople: 
    TWITTER : URL's and images
    LINKEDIN etc: channel and links.
socialFootprint: 
    return Top 3 links from each => 
        twitter, instagram, facebook, linkedin.
'''
'''
{
    "truecaller_res": truecaller_res,
    "google_ts_res_plain": google_ts_res_plain,
    "google_ts_res_email": google_ts_res_email,
    "google_ts_res_email_name": google_ts_res_email_name,
    "google_ts_res_address": google_ts_res_address,
    "google_ts_res_facebook": google_ts_res_facebook,
    "google_ts_res_twitter": google_ts_res_twitter,
    "google_ts_res_instagram": google_ts_res_instagram,
    "google_ts_res_linkedin": google_ts_res_linkedin,
    "twitter_res": twitter_res,
    "google_is_res_entity": google_is_res_entity,
    "google_is_res_name": google_is_res_name,
    "google_ts_res_zabuacorp": google_ts_res_zabuacorp,
    "google_ts_res_indiakanoon": google_ts_res_indiakanoon,
    "google_ts_entity_res_facebook": google_ts_entity_res_facebook,
    "google_ts_entity_res_twitter": google_ts_entity_res_twitter,
    "google_ts_entity_res_instagram": google_ts_entity_res_instagram,
    "google_ts_entity_res_linkedin": google_ts_entity_res_linkedin,
    "google_is_entity_res_facebook": google_is_entity_res_facebook,
    "google_is_entity_res_twitter": google_is_entity_res_twitter,
    "google_is_entity_res_instagram": google_is_entity_res_instagram,
    "google_is_entity_res_linkedin": google_is_entity_res_linkedin
}
'''

# Add similarity later.
def get_facebook_data(data):

    result = list()
    platform_keys = ["google_ts_entity_res_facebook", "google_ts_res_facebook"]
    data1 = data["google_ts"][platform_keys[0]]
    data2 = data["google_ts"][platform_keys[1]]

    i = 0
    for res in data1:
        confidenceScore = 90 - (i+1)*random.uniform(0,10)
        result.append({'url': res['url'], 'confidenceScore': confidenceScore})
        i += 1

    i = 0
    for res in data2:
        confidenceScore = 90 - (i+1)*random.uniform(0,10)
        result.append({'url': res['url'], 'confidenceScore': confidenceScore})
        i += 1
    return result

def get_linkedin_data(data):
    result = list()
    platform_keys = ["google_ts_entity_res_linkedin", "google_ts_res_linkedin"]
    data1 = data["google_ts"][platform_keys[0]]
    data2 = data["google_ts"][platform_keys[1]]

    i = 0
    for res in data1:
        confidenceScore = 90 - (i+1)*random.uniform(0,10)
        result.append({'url': res['url'], 'confidenceScore': confidenceScore})
        i += 1

    i = 0
    for res in data2:
        confidenceScore = 90 - (i+1)*random.uniform(0,10)
        result.append({'url': res['url'], 'confidenceScore': confidenceScore})
        i += 1

    return result

def get_instagram_data(data):
    result = list()
    platform_keys = ["google_ts_entity_res_instagram", "google_ts_res_instagram"]
    data1 = data["google_ts"][platform_keys[0]]
    data2 = data["google_ts"][platform_keys[1]]

    i = 0
    for res in data1:
        confidenceScore = 90 - (i+1)*random.uniform(0,10)
        result.append({'url': res['url'], 'confidenceScore': confidenceScore})
        i += 1

    i = 0
    for res in data2:
        confidenceScore = 90 - (i+1)*random.uniform(0,10)
        result.append({'url': res['url'], 'confidenceScore': confidenceScore})
        i += 1
    return result

def get_twitter_data(data):
    result = list()
    twitter_profiles = data["twitter"]
    for profile in twitter_profiles:
        result.append({'url': "https://twitter.com/"+profile['user_screen_name'], 'confidenceScore': 100, 'profileUrl': profile['user_profile_image']})

    return result

def get_related_people(data):
    return [
        {
            "details": data['twitter'][0]['top_commentors'],
            "platform":"TWITTER"
        },
        {
            "details": {},
            "platform":"LINKEDIN"
        },
        {
            "details": {},
            "platform":"INSTAGRAM"
        },
        {
            "details": {},
            "platform":"FACEBOOK" 
        }
    ]

def get_available_apps(data):
    available_apps = []
    url_to_enum_dict = get_url_to_enum_dict()
    google_res = data['google_ts']
    for res in google_res:
        individual_res = google_res[res]
        for entry in individual_res:
            base_uri = urlparse('{uri.scheme}://{uri.netloc}/'.format(uri=entry['url']))
            if base_uri in url_to_enum_dict:
                available_apps.append(url_to_enum_dict[base_uri])
    return available_apps
def get_applicable_tags(data):
    google_ts_res = data['google_ts']
    google_is_res = data['google_is']

    # ORG, GPE, PERSON
    org_tags = list()
    gpe_tags = list()
    person_tags = list()

    for search in google_ts_res:
        search_results = google_ts_res[search]
        for result in search_results:
            entities = extract_entities(result['title'])
            for entity in entities:
                if entity == "ORG":
                    org_tags.extend(entities[entity])
                elif entity == "GPE":
                    gpe_tags.extend(entities[entity])
                else:
                    person_tags.extend(entities[entity])


    for search in google_is_res:
        search_results = google_is_res[search]
        for result in search_results:
            entities = extract_entities(result['text'])
            for entity in entities:
                if entity == "ORG":
                    org_tags.extend(entities[entity])
                elif entity == "GPE":
                    gpe_tags.extend(entities[entity])
                else:
                    person_tags.extend(entities[entity])

    return {
        'ORG': json.dumps(set(org_tags),default=serialize_sets),
        'PERSON': json.dumps(set(person_tags),default=serialize_sets),
        'GPE': json.dumps(set(gpe_tags),default=serialize_sets),
        'location': data['twitter'][0]['user_location'] if len(data['twitter']) != 0 else ""
    }
    

def get_informational_data(data):
    result = list()
    platform_keys = ["google_ts_res_zabuacorp", "google_ts_res_indiakanoon"]
    data1 = data["google_ts"][platform_keys[0]]
    data2 = data["google_ts"][platform_keys[1]]

    i = 0
    for res in data1:
        confidenceScore = 90 - (i+1)*random.uniform(0,10)
        result.append({'url': res['url'], 'confidenceScore': confidenceScore})
        i += 1

    i = 0
    for res in data2:
        confidenceScore = 90 - (i+1)*random.uniform(0,10)
        result.append({'url': res['url'], 'confidenceScore': confidenceScore})
        i += 1
        
    return result

def generate_response(data):

    tag_related_data = get_applicable_tags(data)
    result = {}
    result['name'] = data["name"]
    result['imageUrls'] = get_image_urls(data)
    result['socialFootprint'] = dict()
    result['socialFootprint']['twitter'] = get_twitter_data(data)
    result['socialFootprint']['facebook'] = get_facebook_data(data)
    result['socialFootprint']['linkedin'] = get_linkedin_data(data)
    result['informationFootprint'] = get_informational_data(data)
    result['primaryAddress'] = tag_related_data['location']
    result['tagsApplicable'] = tag_related_data['PERSON']
    result['additionalAddress'] = tag_related_data['GPE']
    result['relatedPeople'] = get_related_people(data)
    return result

def get_image_urls(data):
    images = list()

    twitter_res = data['twitter']
    for res in twitter_res:
        images.append(res['user_profile_banner'])
        images.append(res['user_profile_image'])

    google_res = data['google_is']
    for res in google_res:
        individual_res = google_res[res]
        for entry in individual_res:
            if entry['url'].startswith("https://pbs.twimg.com") or entry['url'].startswith("https://yt3.googleusercontent.com") or entry['url'].startswith("https://media.licdn.com"):
                images.append(entry['url'])
    return images
