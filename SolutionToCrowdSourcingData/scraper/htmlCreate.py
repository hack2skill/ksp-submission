
import os
from soc_scrape import instascraper,twitterscraper,fbscraper,truecaller
import urllib.request

def downloader(username):

    path = './data'
    users = os.listdir(path)

    os.mkdir('./data/'+username)
    os.mkdir(f'./data/{username}/'+'image')
    os.mkdir(f'./data/{username}/'+'image/'+'twitter')
    os.mkdir(f'./data/{username}/'+'image/'+'insta')
    os.mkdir(f'./data/{username}/'+'image/'+'fb')
    os.mkdir(f'./data/{username}/'+'video')
    os.mkdir(f'./data/{username}/'+'video/'+'insta')
    os.mkdir(f'./data/{username}/'+'video/'+'fb')

    tImg = twitterscraper(username)
    if tImg!=-1:
        for i in tImg:
            os.system(f"wget '{i}' -P './data/{username}/image/twitter'")
    iImg,iVid =instascraper(username)
    fImg,fVid  = ([],[])#fbscraper(username)

    
    for i in iImg:
        os.system(f"wget '{i}' -P './data/{username}/image/insta'")
    for i in fImg:
        os.system(f"wget '{i}' -P './data/{username}/image/fb'")

    count = 0
    for i in iVid:
        # os.system(f"wget '{i}' -P './data/{username}/video'")
        count += 1
        urllib.request.urlretrieve(i, f'./data/{username}/video/insta/video_insta{count}.mp4') 

    count = 0
    for i in fVid: 
        os.system(f"wget '{i}' -P './data/{username}/video'")
        count += 1
        urllib.request.urlretrieve(i, f'./data/{username}/video/fb/video_fb{count}.mp4') 

def createHtml(username,phone):
    path = f'./data/{username}/image/insta/'
    i = 0
    for filename in os.listdir(path):
        my_dest ="insta_img" + str(i) + ".jpeg"
        my_source =path + filename
        my_dest =path + my_dest
        # rename() function will
        # rename all the files
        os.rename(my_source, my_dest)
        i += 1
    path = f'./data/{username}/image/fb/'
    i = 0
    for filename in os.listdir(path):
        my_dest ="fb_img" + str(i) + ".jpeg"
        my_source =path + filename
        my_dest =path + my_dest
        # rename() function will
        # rename all the files
        os.rename(my_source, my_dest)
        i += 1
    path = f'./data/{username}/image/twitter/'
    i = 0
    for filename in os.listdir(path):
        my_dest ="fb_img" + str(i) + ".jpeg"
        my_source =path + filename
        my_dest =path + my_dest
        # rename() function will
        # rename all the files
        os.rename(my_source, my_dest)
        i += 1
    path = f'./data'


    file_html = open(f"{path}/{username}/{username}.html", "w")

    insta_imagesString = ''
    insta_videoString = ''
    insta_imageList = os.listdir(f'{path}/{username}/image/insta')
    insta_videoList = os.listdir(f'{path}/{username}/video/insta')
    for i in insta_imageList:
        insta_imagesString += f'<img src="image/insta/{i}" alt="image" height="400px" width="400px">'
    for i in insta_videoList:
        insta_videoString += f'<video controls height="400px" width="400px"><source src="video/insta/{i}" type="video/mp4"></video>'

    fb_imagesString = ''
    fb_videoString = ''
    fb_imageList = os.listdir(f'{path}/{username}/image/fb')
    fb_videoList = os.listdir(f'{path}/{username}/video/fb')
    for i in fb_imageList:
        fb_imagesString += f'<img src="image/fb/{i}" alt="image" height="400px" width="400px">'
    for i in fb_videoList:
        fb_videoString += f'<video controls height="400px" width="400px"><source src="video/fb/{i}" type="video/mp4"></video>'

    twe_imagesString = ''

    twe_imageList = os.listdir(f'{path}/{username}/image/twitter')
    for i in twe_imageList:
        twe_imagesString += f'<img src="image/twitter/{i}" alt="image" height="400px" width="400px">'

    callerId = truecaller(phone)
    phoneInfo = ""
    import json
    if callerId!= -1:
        phoneInfo = callerId
        # phoneInfo=json.loads(phoneInfo)
        # phoneInfo=json.dumps(phoneInfo,indent=4)
    # phoneInfo = json.stringify(phoneInfo)
    # print(phoneInfo)

    data ="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>
    """+username+"""</title>
    </head>
    <body>
    """+'<h2>True Caller Data</h2><h4>'+phoneInfo[1]+'<h4/><br/><br/>'+phoneInfo[0]+"<h2>Twitter Images</h2>"+twe_imagesString+"<h2>Instagram Images</h2>"+insta_imagesString+"<h2>Instagram Videos</h2>"+insta_videoString+"<h2>Facebook Images</h2>"+fb_imagesString+"<h2>Facebook Videos</h2>"+fb_videoString+"""
    </body>
    </html> 
    """
    file_html.write(data)
    file_html.close()

username = "elonmusk"
phone = ""
downloader(username)
createHtml(username,phone)
