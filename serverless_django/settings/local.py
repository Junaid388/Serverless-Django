import imp
import os

# all base settings for Django
from .base import *

from .installed import *


ALLOWED_HOSTS = ['*']

HOME_PAGE_MSG = "Hello World, This is local"
print("Using local")
# Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('LOCAL_DATABASE_NAME'),
        'USER': os.environ.get('LOCAL_DATABASE_USER'),
        'PASSWORD':os.environ.get('LOCAL_DATABASE_PWD'),
        'HOST':"127.0.0.1",
        'PORT':5432
    }
}
