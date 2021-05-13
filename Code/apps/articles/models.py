from django.db import models
from utils import uploader
from mdeditor.fields import MDTextField
from django.core.files.storage import FileSystemStorage
import os, time
from PersonalBlog.settings import MediaPath, MEDIA_ROOT, CoverImages
from hashlib import md5
from imagekit.models import ProcessedImageField
from imagekit.processors import Resize

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

class Articles(models.Model):
    id = models.AutoField(primary_key=True)
    cate_id = models.ForeignKey('ArticleCategories', on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    introduction = models.CharField(max_length=200)
    content = MDTextField()
    # coverImage = models.FileField(upload_to=coverImage_uploadTo, storage=DataStorage(), null=True)
    coverImage = ProcessedImageField(upload_to=coverImage_uploadTo, storage=DataStorage(), null=True, processors=[Resize(255, 155)],
                                     format="PNG")

    in_turn = models.BooleanField()
    is_using = models.BooleanField()
    is_deleted = models.BooleanField()

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class ArticleCategories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    parent_id = models.IntegerField(null=True)

    is_using = models.BooleanField()
    is_deleted = models.BooleanField()

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
