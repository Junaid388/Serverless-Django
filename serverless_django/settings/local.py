import imp
import os

# all base settings for Django
from .base import *

from .installed import *


ALLOWED_HOSTS = ['*']

HOME_PAGE_MSG = "Hello World, This is local"
print("Using local")
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

