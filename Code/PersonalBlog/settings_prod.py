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
oss = readConf(os.path.join(BASE_DIR, ".oss"), "=")

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
            "usage": True,
            "OSS_ACCESS_KEY_ID": oss["OSS_ACCESS_KEY_ID"],
            "OSS_ACCESS_KEY_SECRET": oss["OSS_ACCESS_KEY_SECRET"],
            "OSS_ENDPOINT": oss["OSS_ENDPOINT"],
            "OSS_BUCKET_NAME": oss["OSS_BUCKET_NAME"]
        }
    }
}
