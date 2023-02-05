
import os, django
os.environ['DJANGO_SETTINGS_MODULE'] = 'OSINT.settings'
django.setup()

from modules.social.main import main as social
from modules.search import main as search
from modules.news.main import main as news
from modules.tor import search as tor

# social(["aravindha1234u"])
# print(search("aravindha hariharan"))
news()
# search("Drugs LSD")

# import json
# from nltk.corpus import stopwords
# import itertools
# import collections

# data = json.load(open("/tmp/temp.json"))
# stop_words = set(stopwords.words('english'))

# overall = []
# for category,news in data.items():
#     print(category)
#     news_text = [n['title']+" "+(n['description'] or "") for n in news]
#     lower_news = [[w for w in n.lower().split() if w not in stop_words] for n in news_text]
#     overall += lower_news

#     all_words_nsw = list(itertools.chain(*lower_news))
#     counts_nsw = collections.Counter(all_words_nsw)

#     print(counts_nsw.most_common(15))

#     # break

# all_words_nsw = list(itertools.chain(*overall))
# counts_nsw = collections.Counter(all_words_nsw)

# print(counts_nsw.most_common(15))