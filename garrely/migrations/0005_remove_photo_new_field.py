# Generated by Django 2.0.7 on 2018-07-10 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garrely', '0004_auto_20180710_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='new_field',
        ),
    ]
