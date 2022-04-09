import imp
import os

# all base settings for Django
from .base import *

from .installed import *

ALLOWED_HOSTS = ['*']
HOME_PAGE_MSG = "Hello World, This is local proxy"

print("Using local proxy")
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('LOCAL_PROXY_DATABASE_NAME'),
        'USER': os.environ.get('LOCAL_PROXY_DATABASE_USER'),
        'PASSWORD':os.environ.get('LOCAL_PROXY_DATABASE_PWD'),
        'HOST':os.environ.get('LOCAL_PROXY_DATABASE_HOST'),
        'PORT':5432
    }
}

