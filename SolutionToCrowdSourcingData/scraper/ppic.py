import requests
from bs4 import BeautifulSoup
import json
from math import sqrt
def similarppl(full_name):
    name = full_name# replace with the name you want to search

    # Make a GET request to the search page
    response = requests.get(f"https://www.instagram.com/web/search/topsearch/?context=blended&query={name}")

    # Extract the HTML content from the response
    html_content = response.text

    # Encode the HTML content as UTF-8
    html_content = html_content.encode("utf-8")

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    k=json.loads(str(soup))
    list_of_users=[]
    for i in k['users']:
        list_of_users.append(i['user']['username'])
  
    similarity=[]
    import difflib
    for i in list_of_users:
        seq=difflib.SequenceMatcher(None, i,name)
        d=seq.ratio()*100
        similarity.append([i,d])
    flag=5
    similarity.sort(key=lambda x: x[1],reverse=True)
    while flag!=0:
        ki=5
        try:
            similarity=similarity[:flag]
            break
            
        except:
            flag-=1
            pass
    sum1=0
    # for i in similarity:
    #     sum1+=i[1]
    
    # for i in range(len(similarity)):
    #     similarity[i][1]= similarity[i][1]/sum1
    # print(similarity)
    return similarity

