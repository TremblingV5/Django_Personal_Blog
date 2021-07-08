from django.db import models
from utils.CommonModel import CommonModel

class AdminUser(CommonModel):
    username = models.CharField(max_length=20)
    password = models.TextField()
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=13)
    email = models.TextField()


class ContactInfo(CommonModel):
    name = models.TextField()
    email = models.TextField()
    message = models.TextField()
