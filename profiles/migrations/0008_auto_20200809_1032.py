# Generated by Django 3.0.8 on 2020-08-09 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20200809_1017'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userprofile',
            unique_together=set(),
        ),
    ]