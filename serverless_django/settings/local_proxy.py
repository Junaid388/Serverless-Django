import imp
import os

# all base settings for Django
from .base import *

from .installed import *


HOME_PAGE_MSG = "Hello World this is local proxy"

print("Using local proxy")
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db_proxy.sqlite3',
    }
}

