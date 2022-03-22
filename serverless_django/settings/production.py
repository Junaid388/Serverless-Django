import imp
import os

# all base settings for Django
from .base import *

from .installed import *

ALLOWED_HOSTS = ['*']
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", 'django-insecure-i*2yg*in*#v9c=xlpaz+uc45&=^@eu%d=mwku)136#@9kparj7')

print("Using production")

HOME_PAGE_MSG = "Hello World, This is production"
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db_prod.sqlite3',
    }
}

