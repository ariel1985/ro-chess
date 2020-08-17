"""
LOCAL CONFIG
-----------------
Django settings for django_chess project.
"""
from .base import *

# Override base.py settings here

DEBUG = True


ENV_NAME = "localdev"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm9wyknb(pvgc2#ua#z(9y5(b38+-_ng!q&_8n2z2v@u3i3$(tn'



ALLOWED_HOSTS = ['127.0.0.1']

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# corsheaders config
CORS_ORIGIN_ALLOW_ALL = True

