try:
    import argparse
    import json
    import requests
    from fake_headers import Headers
    import docx
except ModuleNotFoundError:
    print("Please download dependencies from requirement.txt")
except Exception as ex:
    print(ex)

class Instagram:
    @staticmethod
    def build_param(username):
        params = {
            'username': username,
        }
        return params

    @staticmethod
    def build_headers(username):
        return {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'referer': f'https://www.instagram.com/{username}/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': Headers().generate()['User-Agent'],
            'x-asbd-id': '198387',
            'x-csrftoken': 'VUm8uVUz0h2Y2CO1SwGgVAG3jQixNBmg',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-requested-with': 'XMLHttpRequest',
        }

    @staticmethod
    def make_request(url, params, headers, proxy=None):
        response = None
        if proxy:
            proxy_dict = {
                'http': f'http://{proxy}',
                'https': f'http://{proxy}'
            }
            response = requests.get(
                url, headers=headers, params=params, proxies=proxy_dict)
        else:
            response = requests.get(
                url, headers=headers, params=params)
        return response

    @staticmethod
    def scrap(username, proxy = None):
        try:
            headers = Instagram.build_headers(username)
            params = Instagram.build_param(username)
            response = Instagram.make_request('https://www.instagram.com/api/v1/users/web_profile_info/',
            headers=headers, params=params, proxy=proxy)
            if response.status_code == 200:
                profile_data = response.json()['data']['user']
                return json.dumps(profile_data)
            else:
                print('Error : ', response.status_code, response.text)
        except Exception as ex:
            print(ex)


def Insta_json(un):
    print(Instagram.scrap(un,"chrome"))
    idict = {}
    data = json.loads(Instagram.scrap(un))
    temp = data
    print(temp)
    idict["username"] = str(temp['username'])
    idict["biography"] =  str(temp['biography'])
    idict["full_name"] = str(temp['full_name'])
    idict["fbid"] = str(temp['fbid'])
    idict["is_erified"] = str(temp['is_verified'])
    idict["profile_pic_url_hd"] = str(temp['profile_pic_url_hd'])
    return idict