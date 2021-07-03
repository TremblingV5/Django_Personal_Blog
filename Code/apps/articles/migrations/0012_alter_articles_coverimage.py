# Generated by Django 3.2 on 2021-04-23 13:13

from django.db import migrations, models

import apps.articles.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_alter_articles_coverimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='coverImage',
            field=models.FileField(storage=apps.articles.models.DataStorage(), upload_to='../../resources/'),
        ),
    ]
