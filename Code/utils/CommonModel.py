from django.db import models


class CommonModel(models.Model):
    id = models.AutoField(primary_key=True)

    is_using = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    in_turn = models.BooleanField(default=True)

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True