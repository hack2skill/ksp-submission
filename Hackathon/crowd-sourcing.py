from bs4 import BeautifulSoup
import requests
import json
import re

def check_input_type(input_string):
    # Check if input_string is a text
    if input_string.isalpha():
        return "text"

    # Check if input_string is a number
    if input_string.isdigit():
        return "number"

    # Check if input_string is an email
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_pattern, input_string):
        return "email"

    # Check if input_string is a social media link
    social_media_pattern = r'(?:http(s)?:\/\/)?(?:www\.)?(?:instagram|linkedin|twitter|facebook)\.(?:com|co|in)\S+'
    if re.match(social_media_pattern, input_string, re.IGNORECASE):
        return "social media link"

    # Check if input_string is a web link
    web_link_pattern = r'(http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&\'\(\)\*\+,;=.]+'
    if re.match(web_link_pattern, input_string):
        return "web link"

    # If none of the above match, return None
    return None

def extract_username_from_social_media_url(url):

    # Get username from social media
    data = re.search(r'(?:twitter.com/|facebook.com/|instagram.com/|snapchat.com/add|linkedin.com/(?:[a-z]{2,3}/))([^/?]+)', url)
    if data:
        res = data.group(1)
        check_re = r'^[a-zA-Z0-9_.-]+$'
        if re.match(check_re, res):
            return res

    return 'Invalid Details'

# print(extract_username_from_social_media_url("https://twitter.com/vamsi.kari"))
# input_string = input("Enter input: ")
# print(check_input_type(input_string))

input_string = input("Enter input: ")
# print(extract_username_from_social_media_url(input_string))
extracted_username = extract_username_from_social_media_url(input_string)

# 531873938697-p2on7cff5u79fickgqb7vl672ehvjc7i.apps.googleusercontent.com

# Set up your API key
API_KEY = "AIzaSyAYskwRnqiK-HZwCLjCST6BW740PUOQ0PE"
SEARCH_ENGINE_ID = "f7f32a932f6b34b77"

# Define your search query
query = extracted_username
# using the first page
# page = 1
# # constructing the URL
# # doc: https://developers.google.com/custom-search/v1/using_rest
# # calculating start, (page=2) => (start=11), (page=3) => (start=21)
# start = (page - 1) * 10 + 1
url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&filter=1"

# make the API request
data = requests.get(url).json()

# get the result items
search_items = data.get("items")
# iterate over 10 results found
for i, search_item in enumerate(search_items, start=1):
    try:
        # get the page title
        title = search_item.get("title")
    
        # extract the page url
        link = search_item.get("link")

        data = {"title": title, "link": link}

        print(data)

        TABLE_COL_NAMES = ('Title', 'Link')

        TABLE_DATA = (title, link)

        # pdf = FPDF()
        # pdf.add_page()
        # pdf.set_font("Times", size=16)
        # line_height = pdf.font_size * 2
        # col_width = pdf.epw / 4  # distribute content evenly

        # def render_table_header():
        #     pdf.set_font(style="B")  # enabling bold text
        #     for col_name in TABLE_COL_NAMES:
        #         pdf.cell(col_width, line_height, col_name, border=1)
        #     pdf.ln(line_height)
        #     pdf.set_font(style="")  # disabling bold text

        # render_table_header()
        # for _ in range(10):  # repeat data rows
        #     for row in TABLE_DATA:
        #         if pdf.will_page_break(line_height):
        #             render_table_header()
        #         for datum in row:
        #             pdf.cell(col_width, line_height, datum, border=1)
        #         pdf.ln(line_height)


        # pdf.output("table.pdf")

        # print the results
        # print("="*10, f"Result #{i+start-1}", "="*10)
        # print("Title:", title)
        # print("URL:", link, "\n")
    except KeyError:
        title = ''
        link = ''