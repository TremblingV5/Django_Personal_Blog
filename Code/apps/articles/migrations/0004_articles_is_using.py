# Generated by Django 3.2 on 2021-04-23 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_articles_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='is_using',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
