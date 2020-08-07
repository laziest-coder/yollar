from django.db import models


class Image(models.Model):
    report = models.ForeignKey('reports.Report', related_name='images', on_delete=models.CASCADE)
    src = models.ImageField(upload_to='reports/')

    class Meta:
        db_table = 'report_images'

    def __str__(self):
        return str(self.src)

