import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "airport_system.settings")

app = Celery("airport_system")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
