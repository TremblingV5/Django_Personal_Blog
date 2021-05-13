from django.db import models


class AdminUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.TextField()
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=13)
    email = models.TextField()


class ContactInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    email = models.TextField()
    message = models.TextField()

    is_viewed = models.BooleanField()
    is_deleted = models.BooleanField()
