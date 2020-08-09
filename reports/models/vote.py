from django.db import models
from django.conf import settings


class Vote(models.Model):
    report = models.ForeignKey('reports.Report', related_name='votes', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='votes', on_delete=models.SET_NULL)

    class Meta:
        db_table = 'report_votes'
