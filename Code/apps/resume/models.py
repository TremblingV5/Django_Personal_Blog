import os
import time
from hashlib import md5

from django.core.files.storage import FileSystemStorage
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Resize

from PersonalBlog.settings import MEDIA_ROOT
from utils import uploader


class DataStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(MEDIA_ROOT, name))
        return name


def personalImage_uploadTo(instance, filename):
    string = "%s-%s-%s" % (instance.title, str(time.time()), filename)
    return "/".join(
        [
            'personal',
            "%s.png" % md5(string.encode('utf-8')).hexdigest()
        ]
    )

class BasicInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    introduction = models.TextField()
    birthday = models.DateField()
    mobile = models.CharField(max_length=13)
    email = models.TextField()
    website = models.TextField()
    address = models.TextField()

    personalImage = ProcessedImageField(upload_to=personalImage_uploadTo,
                                        storage=DataStorage(),
                                        null=True,
                                        processors=[Resize(200, 250)],
                                        format="PNG")
    personalQRCode = ProcessedImageField(upload_to=personalImage_uploadTo,
                                         storage=DataStorage(),
                                         null=True,
                                         processors=[Resize(200, 250)],
                                         format="PNG")
    vCard = models.FileField(upload_to=personalImage_uploadTo,
                             storage=DataStorage(),
                             null=True)

    is_using = models.BooleanField()
    is_deleted = models.BooleanField()

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class ExternalSites(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.TextField()
    title = models.CharField(max_length=20)
    icon = models.ImageField(upload_to=uploader.externalSitesIcons_uploadTo)
    icon_selected = models.ImageField(upload_to=uploader.externalSitesIcons_uploadTo)

    is_using = models.BooleanField()
    is_deleted = models.BooleanField()

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class Resume(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    introduction = models.TextField()
    start_time = models.DateField()
    end_time = models.DateField()
    # 该经历的结束时间是否为 至今
    is_now = models.BooleanField()
    # 工作经历或教育经历
    type = models.CharField(max_length=3)

    is_using = models.BooleanField()
    is_deleted = models.BooleanField()

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class CapabilityStack(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    rate = models.IntegerField()

    is_using = models.BooleanField()
    is_deleted = models.BooleanField()

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    introductions = models.TextField()
    url = models.TextField()
    online_url = models.TextField()

    is_using = models.BooleanField()
    is_deleted = models.BooleanField()

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
