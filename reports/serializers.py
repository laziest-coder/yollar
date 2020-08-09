from rest_framework import serializers
from reports.models import Report, Image, Vote
from profiles.serializers import UserProfileSerializer
from rest_framework.fields import CurrentUserDefault


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
        votes = Vote.objects.filter(report=instance.id).count()
        representation['images'] = [image.get('src') for image in images]
        if instance and hasattr(instance, "current_user"):
            is_current_user_upvoted = Vote.objects.filter(report=instance.id, reporter=instance.current_user).exists()
        else:
            is_current_user_upvoted = 0
        representation['votes'] = {"count": votes, "is_upvoted": is_current_user_upvoted}
        return representation

