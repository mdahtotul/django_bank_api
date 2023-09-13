import dj_database_url
from dotenv import load_dotenv
from .common import *


SECRET_KEY = 'django-insecure-=cldztbc4jg&xl0!x673!*v2_=p$$eu)=7*f#d0#zs$44xx-h^'

DEBUG = True

ALLOWED_HOSTS = []

load_dotenv(BASE_DIR / 'secrets.env')

if DEBUG:
    INSTALLED_APPS += [
        "debug_toolbar",
    ]

    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

    INTERNAL_IPS = [
        "127.0.0.1",
    ]

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "bank",
            "HOST": "localhost",
            "USER": "root",
            "PASSWORD": "hp15CC154TX",
        }
    }
