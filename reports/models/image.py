import os
from uuid import uuid4
from django.db import models


def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(path, filename)
    return wrapper


class Image(models.Model):
    report = models.ForeignKey('reports.Report', related_name='images', on_delete=models.CASCADE)
    src = models.ImageField(upload_to=path_and_rename('reports/'))

    class Meta:
        db_table = 'report_images'

    def __str__(self):
        return str(self.src)

