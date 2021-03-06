# Generated by Django 2.0.7 on 2018-07-10 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garrely', '0003_auto_20180709_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='camera',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='location',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='new_field',
            field=models.CharField(default='SOME STRING', max_length=140),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.CharField(max_length=50),
        ),
    ]
