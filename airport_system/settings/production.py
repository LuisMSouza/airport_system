import os
from .base import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ["airportsystem-82ef0b028080.herokuapp.com"]

DATABASES = {"default": dj_database_url.config(conn_max_age=600, ssl_require=True)}

CELERY_BROKER_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")
