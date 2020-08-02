from django.db import models


class Image(models.Model):
    report = models.ForeignKey('reports.Report', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='reports/')

    class Meta:
        db_table = 'report_images'
