# Generated by Django 3.2 on 2021-04-23 13:20

import apps.articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_alter_articles_coverimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='coverImage',
            field=models.FileField(storage=apps.articles.models.DataStorage(), upload_to='.'),
        ),
    ]
