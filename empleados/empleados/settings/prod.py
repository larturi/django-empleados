from .base import *

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': "rxdtdntkjfihyg",
        'NAME': "d6n1sr3c2eirkl",
        'PASSWORD': "f5505e0e2d55d18032d9382e29df6f5ac2cdac36c34ecdbfa8fc49b8d863eb29",
        'HOST': "ec2-3-221-100-217.compute-1.amazonaws.com",
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "../static",]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.parent/'media/'

