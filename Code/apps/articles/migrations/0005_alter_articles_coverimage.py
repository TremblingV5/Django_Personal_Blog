# Generated by Django 3.2 on 2021-04-23 06:46

from django.db import migrations, models

import apps.articles.models
import utils.uploader


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_articles_is_using'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='coverImage',
            field=models.ImageField(storage=apps.articles.models.DataStorage(), upload_to=utils.uploader.coverImage_uploadTo),
        ),
    ]
