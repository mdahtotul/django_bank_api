import dj_database_url
from .common import *
from dotenv import load_dotenv

import os

load_dotenv(BASE_DIR / 'secrets.env')

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']


if os.environ.get("VERCEL_ENV") == "production":
  DATABASES = {
    "default": dj_database_url.config(
      default = os.environ.get("PRODUCTION_DB_URL"), conn_max_age=600
    )
  }
