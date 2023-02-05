import requests
import re
import urllib
from requests_html import HTML
from requests_html import HTMLSession

def get_source(url):
    """Return the source code for the provided URL. 

    Args: 
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html. 
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

def scrape_google(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)
    # response = get_source()

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.', 
                      'https://google.', 
                      'https://webcache.googleusercontent.', 
                      'http://webcache.googleusercontent.', 
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links

lis = scrape_google('site:play.google.com/store/apps/details after:2023-02-03 "Finance" "India"')
lis = [link for link in lis if re.search("^https://play.google.com/store/apps/details", link)]

for link in lis:
    print(link)




# from google_play_scraper import search
# from googlesearch import search

# class SearchFunc:
#     def __init__(self, keyword):
#         result = search(
#             keyword,
#             lang='en',#parse_qs(parsed_url.query)['hl'][0],
#             country='in'#parse_qs(parsed_url.query)['gl'][0]
#         )

#         print(result)

# # SearchFunc("money")

# print(next(search('site:play.google.com/store/apps/details "Finance" loan "India"')))
# for i in range(0,5):
# 	response=google.search_results()
	
# 	print(response)
# 	print()
	
# 	data=response["body"]
# 	google.click_next() 
