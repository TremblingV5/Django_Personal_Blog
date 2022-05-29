"""
Django settings for PersonalBlog project.

Generated by 'django-admin startproject' using Django 2.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'in@9_=y-rl3bqcy&$#c#n28!62eir8_gj%6w0f4s7vzyrqb6r+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'demo.local',
    'localhost',
    '127.0.0.1'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'haystack',
    'imagekit',
    'mdeditor',
    'apps.articles',
    'apps.blog',
    'apps.resume',
    'apps.manager'
]

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'apps.blog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_SIGNAL_PROCESSOR = 'apps.blog.HaystackProcessor.Processor'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES':
        ('rest_framework.renderers.JSONRenderer', ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 设置同源的iframe可以被显示
X_FRAME_OPTIONS = 'SAMEORIGIN'

ROOT_URLCONF = 'PersonalBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'PersonalBlog.wsgi.application'

CACHES = {
    'default': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6380/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "tokenPool": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6380/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'personal_blog',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'db',
        'PORT': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, '/static/'),
)
STATIC_ROOT = os.path.join(BASE_DIR, "/static/")

MEDIA_ROOT = os.path.join(BASE_DIR, "resources/")
MEDIA_URL = 'resources/'

# 上传的各类资源的存放地址
class MediaPath:
    ExternalSiteIcons = os.path.join(BASE_DIR, "resources", "icons")
    CoverImages = os.path.join(MEDIA_ROOT, "coverImages")


CoverImages = os.path.join(MEDIA_ROOT, "coverImages")



MDEDITOR_CONFIGS = {
    'default':{
        'width': '100%',  # 自定义编辑框宽度
        'heigth': '100%',   # 自定义编辑框高度
        'toolbar': ["undo", "redo", "|",
                    "bold", "del", "italic", "quote", "|",
                    "list-ul", "list-ol", "hr", "|",
                    "link", "reference-link", "image", "code", "preformatted-text", "table", "datetime",
                    "emoji", "html-entities", "|",
                    "help", "info",
                    "||", "preview", "watch", "fullscreen"],  # 自定义编辑框工具栏
        'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],  # 图片上传格式类型
        'image_folder': 'mdImage',  # 图片保存文件夹名称
        'theme': 'default',  # 编辑框主题 ，dark / default
        'preview_theme': 'default',  # 预览区域主题， dark / default
        'editor_theme': 'default',  # edit区域主题，pastel-on-dark / default
        'toolbar_autofixed': True,  # 工具栏是否吸顶
        'search_replace': True,  # 是否开启查找替换
        'emoji': True,  # 是否开启表情功能
        'tex': True,  # 是否开启 tex 图表功能
        'flow_chart': True,  # 是否开启流程图功能
        'sequence': True,  # 是否开启序列图功能
        'watch': True,  # 实时预览
        'lineWrapping': True,  # 自动换行
        'lineNumbers': True,  # 行号
        'OSS': {
            "usage": False,
            "OSS_ACCESS_KEY_ID": "",
            "OSS_ACCESS_KEY_SECRET": "",
            "OSS_ENDPOINT": "",
            "OSS_BUCKET_NAME": ""
        }
    }
}

SITE_CONFIG = {
    'username': 'zhengfei.xin',
    'title': 'R&D Developer',
    'wish': '想要白嫖'
}

STATUS_INFO = {
    200: "success",
    400: "not found",
    500: "defeat"
}