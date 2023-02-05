import os, django
os.environ['DJANGO_SETTINGS_MODULE'] = 'OSINT.settings'
django.setup()

import schedule, time, threading
from logger import log

from dashboard.models import *

from modules.social.main import main as social
from modules.search import main as search
from modules.tor import search as tor
from modules.phone.main import main as phone

def check_scheduler():
    log.debug("Starting Scheduler in background...")
    while True:
        schedule.run_pending()
        time.sleep(1)

def threaded_function(func,job):
    job.stage = 2
    job.save()
    
    job.data = func(**job.parameters)
    job.stage = 3
    job.save()

def check_job():
    jobs = JobQueue.objects.filter(stage=1)

    # Pripority sort
    jobs = sorted(jobs,key=lambda x:x.priority,reverse=True)
    for j in jobs:
        log.info("Invoking the function....")
        func = [c for c in category_type if c[0] == j.category][0]

        t = threading.Thread(target=threaded_function,args=(globals()[func[1].lower()],j))
        t.daemon = True
        t.start()

schedule.every(10).seconds.do(check_job)

# Restart job in pending stage
jobs = JobQueue.objects.filter(stage=2)
for j in jobs:
    j.stage = 1 
    j.save()