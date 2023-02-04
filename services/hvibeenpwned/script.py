from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
import json
from selenium.webdriver.chrome.options import Options


DRIVER_PATH = 'C:/Users/psura/Projects/KSP/chromedriver_win32'


def checkPawned(query):
    options = Options()

    options.add_argument("--window-size=0,0")

    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get('https://haveibeenpwned.com/unifiedsearch/'+query)
    contents = driver.page_source
    soup = BeautifulSoup(contents, 'html5lib')
    if (soup.find('pre') != None):

        results = json.loads(soup.find('pre').contents[0])['Breaches']
    else:
        results = []
    driver.quit()
    return results


print(checkPawned('p.surajkumar907@gmail.com'))

# print(checkPawned('sodvbvb'))
