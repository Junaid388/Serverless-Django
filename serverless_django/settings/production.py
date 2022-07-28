import imp
import os

# all base settings for Django
from .base import *

from .installed import *

ALLOWED_HOSTS = ['*']
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

print("Using production")

HOME_PAGE_MSG = "Hello World, This is production"
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PRODUCTION_DATABASE_NAME'),
        'USER': os.environ.get('PRODUCTION_DATABASE_USER'),
        'PASSWORD':os.environ.get('PRODUCTION_DATABASE_PWD'),
        'HOST':os.environ.get('PRODUCTION_DATABASE_HOST'),
        'PORT':5432
    }
}

