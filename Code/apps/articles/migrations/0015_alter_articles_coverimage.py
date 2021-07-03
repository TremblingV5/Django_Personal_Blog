# Generated by Django 3.2 on 2021-04-23 17:21

from django.db import migrations, models

import apps.articles.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_auto_20210424_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='coverImage',
            field=models.FileField(null=True, storage=apps.articles.models.DataStorage(), upload_to=apps.articles.models.coverImage_uploadTo),
        ),
    ]
