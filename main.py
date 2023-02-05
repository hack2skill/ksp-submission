import urllib.request
import shutil
from apiclient.discovery import build
from functions import *
import csv
import re
import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app_name=input("Enter your app name : ")

pure_text(app_name)

desc = open('dataset.txt','r')
description = desc.read()

def get_banned_apps():
    banned_apps = [{"description":description}]
    return banned_apps

def is_app_fraudulent(app_description):
    banned_apps = get_banned_apps()
    descriptions = [app["description"] for app in banned_apps]
    tfidf = TfidfVectorizer().fit_transform(descriptions + [app_description])
    similarities = cosine_similarity(tfidf[-1], tfidf[:-1])
    if max(similarities) > 0.6:
        return True
    return False


sapp = open(str(app_name)+'.txt','r')
sapp_desc = sapp.read()

result = resource.list(q=app_name, cx = "044dd7d0558a14882").execute()

app_description = sapp_desc
if is_app_fraudulent(app_description):  
    for item in result["items"]:
        name=item["title"]
        break; 
    noti(name)
else:
    print("This app does not appear to be fraudulent.")
