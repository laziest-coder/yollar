from rest_framework import serializers
from reports.models import Report
from profiles.serializers import UserProfileSerializer


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ('id', 'latitude', 'longitude', 'comment', 'type', 'votes')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['reporter'] = UserProfileSerializer(instance.reporter).data
        representation['address'] = {"uz": instance.address_uz, "ru": instance.address_ru}
        return representation

