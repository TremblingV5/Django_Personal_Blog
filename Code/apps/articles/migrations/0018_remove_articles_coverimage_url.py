# Generated by Django 3.2 on 2021-06-10 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_articles_coverimage_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='coverImage_url',
        ),
    ]