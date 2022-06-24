from __future__ import absolute_import , unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
# from django_celery_beat.models import PeriodicTasks

os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'django_celery_project.settings')

app = Celery('django_celery_project')
app.conf.enable_utc = False

app.conf.update(timezone = 'Africa/Lagos')

app.config_from_object(settings, namespace='CELERY')


# #Celery Beat Settings   
app.conf.beat_schedule = {
    'send-mail-every-day-at-8':{
        'task':'send_mail_app.tasks.send_mail_func',
        'schedule':  5.0,
        # 'args': (2,)
    },

    'add-every-30-seconds': {
        'task': 'send_mail_app.tasks.add',
        'schedule': 10.0,  # executes every 10 secs
        'args': (16, 16)
    },
}

app.conf.timezone = 'UTC'


# app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')