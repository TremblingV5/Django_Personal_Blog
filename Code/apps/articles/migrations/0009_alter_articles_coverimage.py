# Generated by Django 3.2 on 2021-04-23 13:03

from django.db import migrations, models

import apps.articles.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_alter_articles_coverimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='coverImage',
            field=models.ImageField(storage=apps.articles.models.DataStorage(), upload_to=apps.articles.models.coverImage_uploadTo),
        ),
    ]
