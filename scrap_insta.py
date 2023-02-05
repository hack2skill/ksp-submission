import asyncio
from pyppeteer import launch
import time
import json
import os
from captcha import get_captcha

async def get_text(page, selector_path):
    element = await page.querySelector(selector_path)
    query = '(element) => element.innerText.trim()'
    temp = await page.evaluate(query, element)
    return temp


async def main_scrap(email):
    browser = await launch({"headless": False})
    page = await browser.newPage()
    await page.goto(url)
    
    # # take screenshot of captcha
    # time.sleep(2)

    #type captcha
    time.sleep(2)
    # search_box = await page.querySelector('#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv')
    search_box = await page.querySelector('#mount_0_0_gs > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z > section > main > div._ac06.x78zum5.xdt5ytf > div > div > div > div > div:nth-child(4) > form')
    # print(search_box)
    await search_box.type(email)

    # press enter button

    time.sleep(2)
    # await page.click("#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div > div > div > div")
    
    await page.click('#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div:nth-child(6)')
    # page.keypad('Enter')
    # time.sleep(10)
    login_option = await page.querySelector('#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div:nth-child(1)')
    time.sleep(2)
    # print("login option:", login_option)
    
    captcha_element = await page.querySelector(
            '#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div:nth-child(1)'
        )
    await captcha_element.screenshot({'path': 'example.png'})
    
    
    #get captcha from image using pytesseract
    captcha = get_captcha('example.png')

    print("captcha:", captcha)

    if "Sign in to Twitter" in captcha:
        print("we did not found an twitter account with this id")
    else:
        print("we found a twitter account with this id")
        

    await browser.close()
    return captcha


def scrape_data(email):
    data = asyncio.new_event_loop().run_until_complete(main_scrap(email))

    try:
        os.makedirs("output_data")
    except FileExistsError:
        # directory already exists
        pass
    with open('output_data/{}.json'.format(name), 'w') as f:
        json.dump(data, f)

    return data


if __name__ == '__main__':
    url = "https://www.instagram.com/accounts/password/reset/"
    name = "sumit jha"
    id = "gopal@elintdata.com"
    id = "rahulverma.upe@gmail.com"
    id = "gopal.kgpian@gmail.com"
    id = "6206609503"
    
    data = scrape_data(id)