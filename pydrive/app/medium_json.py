try:
    import argparse
    import requests
    import json
    import pandas as pd
    import docx
    import os
except ModuleNotFoundError:
    print("Please download dependencies from requirement.txt")
except Exception as ex:
    print(ex)


class Medium:

    @staticmethod
    def build_payload(username):
        query = ''
        print("XXX")
        module_dir = os.path.dirname(__file__)  # get current directory
        file_path = os.path.join(module_dir, 'medium_graphql_query.graphql')
        print(file_path)
        with open(file_path, 'r', encoding='utf-8') as file:
            query = file.read()
        json_data = [
            {
                'operationName': 'UserProfileQuery',
                'variables': {
                    'includeDistributedResponses': True,
                    'id': None,
                    'username': '@{}'.format(username),
                    'homepagePostsLimit': 1,
                },
                'query': query
            },
        ]
        return json_data

    @staticmethod
    def make_request(URL, json_data):
        try:
            response = requests.post(URL, json=json_data)
            if response.status_code == 200:
                return response.json()
        except Exception as ex:
            print('Error at Make Request: {}'.format(ex))

    @staticmethod
    def scrap(username):
        """scrap medium's profile"""
        try:
            URL = "https://medium.com/_/graphql"
            payload = Medium.build_payload(username)
            response = Medium.make_request(URL, payload)
            print("Hello World??")
            if response:
                print("Hello World?")
                return json.dumps(response)
            else:
                print("Failed to make response!")
        except Exception as ex:
            return {"error": ex}


def Medium_json(username):
    data = json.loads(Medium.scrap(username))
    temp = data[0]['data']['userResult']
    mdict = {}
    mdict["Username"] = str(temp['username'])
    mdict["Newsletter Name"] = str(temp['newsletterV3']['user']['name'])
    mdict["PromoHeadline"] = str(temp['newsletterV3']['promoHeadline'])
    mdict["PromoBody"] = str(temp['newsletterV3']['promoBody'])
    mdict["About"] = str(temp['about'])
    mdict["Medium Bio"] = str(temp['bio'])
    mdict["Twitter screen name"] = str(temp['twitterScreenName'])
    return mdict