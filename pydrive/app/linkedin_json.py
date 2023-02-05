from linkedin_api import Linkedin
import docx

def LinkedIn_json(un):
    api = Linkedin('policeHackathon23@gmail.com', 'Police@123')
    profile = api.get_profile(un)
    ldict = {}
    ldict["Summary"] = profile['summary']
    ldict["Name of the Industry"] = profile['industryName']
    ldict["Geo Location"] = profile['geoLocationName']
    ldict["Country"] = profile['geoCountryName']
    ldict["Headline"] = profile['headline']
    exps = []
    for exp in profile['experience']:
        dict = {}
        dict['companyName'] = exp['companyName']
        dict['title'] = exp['title']
        exps.append(dict)
    ldict["Experiences"] = exps
    edus = []
    for edu in profile['education']:
        dict = {}
        dict['schoolName'] = edu['schoolName']
        edus.append(dict)
    ldict["Education"] = edus
    return ldict