import os
from .base import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ["airportsystem-82ef0b028080.herokuapp.com", "localhost"]

DATABASES = {    
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    } 
}

CELERY_BROKER_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
