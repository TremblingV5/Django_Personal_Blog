from django.db import models
from utils.CommonModel import CommonModel
from utils.mdeditor.fields import MDTextField


class AboutMe(CommonModel):
    content = MDTextField()
