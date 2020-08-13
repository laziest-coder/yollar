from django.conf import settings
from django.contrib.gis.db import models


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
    location = models.PointField()
    comment = models.TextField(blank=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default=OTHER)
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='users', on_delete=models.SET_NULL)
    is_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'reports'

    def get_latitude(self):
        return self.location.coords[1]

    def get_longitude(self):
        return self.location.coords[0]
