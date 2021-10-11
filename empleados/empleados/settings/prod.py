import os
from .base import *

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': "qzbumpngayqete",
        'NAME': "dbmieh8c33p32v",
        'PASSWORD': "7924975be16f7aa5f2f90f83fe6b57a5c22a39ed57b7a360d0dba67ab00ee1d7",
        'HOST': "ec2-52-45-238-24.compute-1.amazonaws.com",
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# STATICFILES_DIRS = [BASE_DIR / "../static",]
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.parent/'media/'

