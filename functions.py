import csv
import shutil
from twilio.rest import Client 
from bs4 import BeautifulSoup
import urllib.request
import shutil
from apiclient.discovery import build
import re

api_key= "AIzaSyAy13eukbnEaDE3YuoIjvRj0z-sgbjLgVg"
resource = build("customsearch", "v1" , developerKey = api_key).cse()


def keytokeyword(key,keyword):
    with open(str(key)) as csv_file:
        list=[]
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            image_source={row[0]}
            list.append(image_source)

    webpage = open(str(keyword), "w")
    webpage.write(str(list))


def noti(app_name):    
    account_sid = 'AC674e7aa11fd575d4ce144e596514b791' 
    auth_token = 'b0168e711bf8663f0c7f9a10506f85c9' 
    client = Client(account_sid, auth_token) 
    
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Greetings, an app named ' + str(app_name) + ' is in our potential fradulant list. Kindly look in to the matter and take suitable actions.\nThank You \nTeam Blaze' ,      
                                to='whatsapp:+916393875244' 
                            ) 
    
    print(message.sid)


def pure_text(app_name):
    result = resource.list(q=str(app_name), cx = "a6eebe5cb5170407f").execute()
    url=result['items'][1]['link']
    with urllib.request.urlopen(url) as response:
        html = response.read()


    def cleanme(html):
        soup = BeautifulSoup(html,features="lxml")
        for script in soup(["script"]): 
            script.extract()
        text = soup.get_text()
        return text
    testhtml = html

    cleaned = cleanme(testhtml)
    webpage = open(str(app_name)+".html", "w", encoding="utf-8")
    webpage.write(cleaned)


    punct = re.compile("[^\w\s]")
    input_file = str(app_name)+".html"
    output_file = str(app_name)+".txt"
    file_content = cleaned
    new_file_content = re.sub(punct,"",file_content)
    with open(output_file, "w") as fw:
        fw.write(new_file_content)

def white_bank():
    with open('whitebank.csv') as csv_file:
        list=[]
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            app_name={row[0]}
            result = resource.list(q=app_name, cx = "a6eebe5cb5170407f").execute()
            url=result['items'][0]['link']
            list.append(url)
        playlink = open("white_loan.txt", "w")
        playlink.write(str(list))


def image_search(image_name):
    result = resource.list(q=str(image_name), cx = "b77bd9bd32b924ef2").execute()
    for i in range (1,10):
        pic_url=result['items'][i]['pagemap']['cse_thumbnail'][0]['src']
        with urllib.request.urlopen(pic_url) as response:
            html = response.read()
        webpage = open("image"+str(i)+".png", "wb")
        webpage.write(html)


