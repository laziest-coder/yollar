from rest_framework import serializers
from reports.models import Report, Image
from profiles.serializers import UserProfileSerializer


class ReportImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('src',)


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ('id', 'latitude', 'longitude', 'comment', 'type')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['reporter'] = UserProfileSerializer(instance.reporter).data
        representation['address'] = {"uz": instance.address_uz, "ru": instance.address_ru}
        images = Image.objects.filter(report_id=instance.id).values()
        representation['images'] = [image.get('src') for image in images]
        return representation

