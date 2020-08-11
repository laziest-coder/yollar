from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Report, Image

admin.site.register(Image)


@admin.register(Report)
class ReportAdmin(OSMGeoAdmin):
    list_display = ('address_uz', 'location')
