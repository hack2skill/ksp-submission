import requests
import base64
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

from sqlconnector import SqlConnector
obj = SqlConnector()

def doAppBrainRequest():
    print("Performing GET request to appbrain to get the details of new apps...")
    api_key = os.getenv("APP_BRAIN_API").strip()
    request_headers = {'content-type': 'application/json'}
    res = []
    url = 'https://api.appbrain.com/v2/info/browse?apikey={}&sort=POPULAR_INDIA&filter=FREE&category=CASINO&offset=500&limit=50'.format(api_key)
    app_brain_res = requests.get(url)
    if app_brain_res.ok:
        res.extend(app_brain_res.json()['apps'])
    url = 'https://api.appbrain.com/v2/info/browse?apikey={}&sort=POPULAR_INDIA&filter=FREE&category=FINANCE&offset=500&limit=50'.format(api_key)
    app_brain_res = requests.get(url)
    if app_brain_res.ok:
        res.extend(app_brain_res.json()['apps'])
    return res


def doVTRequest(url_to_test):
    req_endpoint = "https://www.virustotal.com/api/v3/urls/{}"
    encoded = base64.urlsafe_b64encode(url_to_test.encode()).decode().strip("=")
    req_endpoint = req_endpoint.format(encoded)
    print(req_endpoint)
    print(f"Sending query to VirusTotal API...")
    apikey = os.getenv('VT_API')
    request_headers = {"x-apikey": apikey}
    vt_data = requests.get(req_endpoint, headers=request_headers)
    if vt_data.ok:
        return vt_data.json()
    else:
        return None

inplaystore = []
notinplaystore = []

def checkInPlaystore(num, package):
    url = "https://play.google.com/store/apps/details?id={}".format(package.strip())
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    btns = soup.find_all('span')
    flag = 0
    for btn in btns:
        if btn.text.strip().lower() == "install":
            flag = 1
            break
    if flag:
        inplaystore.append(num)
    else:
        notinplaystore.append(num)


def start():

    result = doAppBrainRequest()

    for num, app in enumerate(result):
        checkInPlaystore(num, app['package'])

    for app in inplaystore:
        name = base64.b64encode(result[app]['name'].encode()).decode()
        website = "NA" if result[app]['website']=="" else result[app]['website']
        devname = "NA" if result[app]['developerName']=="" else result[app]['developerName']
        query = "insert into app_list (app_name, website, developer, package_name, platform) values ('{}','{}','{}','{}','{}')".format(name, website, devname, result[app]['package'], "Android")
        try:
            obj.insert(query)
        except:
            continue
        r = doVTRequest(result[app]['website'])
        app_id = obj.retrieve("select id from app_list where package_name ='{}'".format(result[app]['package']))[0][0]
        if r is None:
            threat="Malicious/Website not there"
            harmless = 0
            malicious = 1

        else:
            threat = r['data']['attributes']['threat_names']
            threat = "" if threat==[] else threat[0]
            harmless = r['data']['attributes']['total_votes']['harmless'] + r['data']['attributes']['last_analysis_stats']['harmless']
            malicious = harmless = r['data']['attributes']['total_votes']['malicious'] + r['data']['attributes']['last_analysis_stats']['malicious']
        query = "insert into virustotal (app_id, type, count_malicious, count_non_malicious) values ('{}','{}','{}','{}')"\
                    .format(app_id, threat, malicious, harmless)

        obj.insert(query)

start()