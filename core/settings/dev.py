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
        "default": dj_database_url.config(
            default = os.environ.get("DEVELOPMENT_DB_URL"), conn_max_age=600
        )
    }


    # DATABASES = {
    #     "default": {
    #         "ENGINE": "django.db.backends.sqlite3",
    #         "NAME": BASE_DIR / "db.sqlite3",
    #         # "ENGINE": "django.db.backends.mysql",
    #         # "NAME": "storefront3",
    #         # "HOST": "localhost",
    #         # "USER": "root",
    #         # "PASSWORD": "hp15CC154TX",
    #     }
    # }
