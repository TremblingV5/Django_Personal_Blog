# Generated by Django 3.2 on 2021-04-23 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_alter_basicinfo_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='type',
            field=models.CharField(max_length=3),
        ),
    ]
