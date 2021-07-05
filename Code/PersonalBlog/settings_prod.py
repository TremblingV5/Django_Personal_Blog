from PersonalBlog.settings import *

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

def readConf(path, tag):
    with open(path, "r") as f:
        return {
            l.split(tag)[0]: l.split(tag)[1] for l in f.read().split("\n")
        }


info = readConf(os.path.join(BASE_DIR, ".env"), "=")
redis = readConf(os.path.join(BASE_DIR, ".redis"), "=")

DEBUG = False

ALLOWED_HOSTS = [
    'demo.local',
    'localhost',
    '127.0.0.1'
]

CACHES = {
    'default': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:%s@redis:6379/0" % redis['PWD'],
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "tokenPool": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:%s@redis:6379/1" % redis['PWD'],
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': info['MYSQL_DATABASE'],
        'USER': info['MYSQL_USER'],
        'PASSWORD': info['MYSQL_PASSWORD'],
        'HOST': 'db',
        'PORT': '3306'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, '/static/'),
)
STATIC_ROOT = os.path.join(BASE_DIR, "/static/")

MEDIA_ROOT = os.path.join(BASE_DIR, "resources/")
MEDIA_URL = 'resources/'

CoverImages = os.path.join(MEDIA_ROOT, "coverImages")
