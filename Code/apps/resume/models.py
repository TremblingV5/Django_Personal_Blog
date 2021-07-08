import os
import time
from hashlib import md5

from django.core.files.storage import FileSystemStorage
from django.db import models
from utils.CommonModel import CommonModel
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


class BasicInfo(CommonModel):
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


class Resume(CommonModel):
    title = models.TextField()
    introduction = models.TextField()
    start_time = models.DateField()
    end_time = models.DateField()
    # 该经历的结束时间是否为 至今
    is_now = models.BooleanField()
    # 工作经历或教育经历
    type = models.CharField(max_length=3)


class CapabilityStack(CommonModel):
    name = models.CharField(max_length=10)
    rate = models.IntegerField()
