from django.db import models
from django.conf import settings


class Report(models.Model):

    TRAFFIC_LIGHT = "traffic_light"
    SIDEWALK = "sidewalk"
    ROAD = "road"
    SIGN = "sign"
    OTHER = "other"

    TYPE_CHOICES = (
        (TRAFFIC_LIGHT, "Traffic Light"),
        (SIDEWALK, "Sidewalk"),
        (ROAD, "Road"),
        (SIGN, "Sign"),
        (OTHER, "Other")
    )

    address_uz = models.CharField(max_length=255)
    address_ru = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    comment = models.TextField(blank=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default=OTHER)
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='users', on_delete=models.SET_NULL)

    class Meta:
        db_table = 'reports'
