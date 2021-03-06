"""
Django settings for dark_maps project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

from .settings import *

DEBUG = True

ALLOWED_HOSTS = "*"

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] = {
    'anon': '10000/second',
    'user': '10000/second',
    'pre_keyBundle': '10000/second'
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

SECURE_SSL_REDIRECT = False
