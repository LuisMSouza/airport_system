import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airport_sistem.settings')

app = Celery('airport_sistem')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
