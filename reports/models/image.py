import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible
from django.db import models


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)


path_and_rename = PathAndRename("reports/")


class Image(models.Model):
    report = models.ForeignKey('reports.Report', related_name='images', on_delete=models.CASCADE)
    src = models.ImageField(upload_to=path_and_rename)

    class Meta:
        db_table = 'report_images'

    def __str__(self):
        return str(self.src)

