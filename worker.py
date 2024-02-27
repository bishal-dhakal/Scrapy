from celery import Celery
from celery.schedules import crontab
from multiprocessing import Process
from trending.Scrapper import run_scrapy
import logging

app = Celery('celery_proj', 
            broker='redis://localhost:6379/0', 
            backend='redis://localhost:6379/0')

app.conf.beat_schedule = {
    "task-newtasks": {
        "task": "taskadd",  
        "schedule": crontab(minute="*"),
    },
}

logger = logging.getLogger(__name__)

@app.task(name="taskadd")
def run_scraper_task():
    logger.info('run scrapper task')
    p = Process(target=run_scrapy)
    p.start()
    p.join()

