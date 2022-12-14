# Generated by Django 3.0.8 on 2020-08-02 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_userprofile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='device_id',
            field=models.CharField(max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
