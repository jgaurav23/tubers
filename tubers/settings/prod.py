from .base import *

SECRET_KEY = os.environ.get('TUBERS_DJANGO_SECRET_KEY')

DEBUG = os.environ.get('TUBERS_DJANGO_DEBUG')

ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('TUBERS_DB_NAME'),
        'USER' : os.environ.get('TUBERS_DB_USER'),
        'PASSWORD' : os.environ.get('TUBERS_DB_PASSWORD'),
        'HOST' : os.environ.get('TUBERS_DB_HOST'),
        'PORT' : os.environ.get('TUBERS_DB_PORT'),

    }
}

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('TUBERS_SOCIAL_AUTH_FACEBOOK_KEY')  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('TUBERS_SOCIAL_AUTH_FACEBOOK_SECRET')  # App Secret

SOCIAL_AUTH_GITHUB_KEY = os.environ.get('TUBERS_SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = os.environ.get('TUBERS_SOCIAL_AUTH_GITHUB_SECRET')

SESSION_ENGINE = os.environ.get('TUBERS_SESSION_ENGINE')
SESSION_COOKIE_SECURE = os.environ.get('TUBERS_SESSION_COOKIE_SECURE')
SESSION_COOKIE_HTTPONLY = os.environ.get('TUBERS_SESSION_COOKIE_HTTPONLY')