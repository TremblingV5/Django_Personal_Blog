# Generated by Django 3.2 on 2021-06-10 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_alter_articles_coverimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='coverImage_url',
            field=models.TextField(null=True),
        ),
    ]
