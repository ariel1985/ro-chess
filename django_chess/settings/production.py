"""
PRODUCTION CONFIG
-----------------
Django settings for django_chess project.
"""
import dj_database_url
from decouple import config

from .base import *

# Override base.py settings here


ENV_NAME = "production"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

ALLOWED_HOSTS = ['rotem-chess.herokuapp.com']

MIDDLEWARE_CLASSES += [
    # Simplified static file serving for heroku
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'django_chess.urls'

WSGI_APPLICATION = 'django_chess.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases


# heroku deployment vars
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'chess_engine/static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Heruko set initial data in db.
FIXTURE_DIRS = [
    'fixture_db_init_data'
]