
import os, django
os.environ['DJANGO_SETTINGS_MODULE'] = 'OSINT.settings'
django.setup()

from modules.social.main import main as social
print(social("aravindha1234u"))

from modules.search import main as search
# print(search(**{"keyword":"aravindha"})) 

from modules.phone.main import main as phone
# print(phone(**{"phonenumber":"9486324742"}))

from modules.upi import get_upi
# print(get_upi("aravindha1234u"))