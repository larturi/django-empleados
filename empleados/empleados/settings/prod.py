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
        'USER': "gpiifepuznxaos",
        'NAME': "df442nj54pdse2",
        'PASSWORD': "949c745a1b361602f5ddba7319b5e47ee2a93aecb0f5f06d29c3a943fb06c93e",
        'HOST': "ec2-44-198-196-149.compute-1.amazonaws.com",
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "../static",]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.parent/'media/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
