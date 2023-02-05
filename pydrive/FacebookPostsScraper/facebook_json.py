from FacebookPostsScraper.FacebookPS import FacebookPostsScraper as Fbps
from pprint import pprint as pp
from facebook_scraper import get_profile
import json
import docx
def Facebook_json(un):
    doc=docx.Document()
    # Enter your Facebook email and password
    email = 'policehackathon23@gmail.com'
    password = 'Police@123'
    print("Helloworld1")
    # Instantiate an object
    fps = Fbps(email, password)
    print("Helloworld2")
    print(get_profile(un,cookies='FacebookPostsScraper/facebook.com_cookies.txt'))
    profile= get_profile(un,cookies='FacebookPostsScraper/facebook.com_cookies.txt')
    # Example with single profile
    single_profile = 'https://www.facebook.com/{}'.format(profile['Contact Info']['Facebook'])
    data = fps.get_posts_from_profile(single_profile)
    #s=pp(data)
    p=profile['top_post']
    fdict={}
    fdict['User ID']= p['user_id']
    fdict['Username']= p['username']
    fdict['User URL']= p['user_url']
    fdict['Cover Photo']= profile['cover_photo']
    fdict['Profile Picture']= profile['profile_picture']
    fdict['Name']= profile['Name']
    fdict['Category']= profile['Category']  
    vals=[]
    for d in data:
        fdict2={}
        fdict2['Date published'] = d['published']
        fdict2['Description'] = d['description']
        fdict2['Images'] = d['images']
        fdict2['Post URL'] = d['post_url']
        vals.append(fdict2)
    fdict['posts']=vals
    return fdict