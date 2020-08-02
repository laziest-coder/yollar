# Generated by Django 3.0.8 on 2020-08-02 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20200802_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='device_id',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterUniqueTogether(
            name='userprofile',
            unique_together={('device_id', 'username')},
        ),
    ]