import os
import time
from hashlib import md5

from django.core.files.storage import FileSystemStorage
from django.db import models
from utils.CommonModel import CommonModel
from imagekit.models import ProcessedImageField
from imagekit.processors import Resize
from mdeditor.fields import MDTextField

from PersonalBlog.settings import MEDIA_ROOT


class DataStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(MEDIA_ROOT, name))
        return name

def coverImage_uploadTo(instance, filename):
    string = "%s-%s-%s" % (instance.title, str(time.time()), filename)
    return "/".join(
        [
            'coverImages',
            "%s.png" % md5(string.encode('utf-8')).hexdigest()
        ]
    )

class Articles(CommonModel):
    cate_id = models.ForeignKey('ArticleCategories', on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    introduction = models.CharField(max_length=200)
    content = MDTextField()
    coverImage = ProcessedImageField(
        upload_to=coverImage_uploadTo,
        storage=DataStorage(),
        null=True,
        processors=[Resize(255, 155)],
        format="PNG"
    )


class ArticleCategories(CommonModel):
    name = models.CharField(max_length=10)
