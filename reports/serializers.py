from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField
from reports.models import Report, Image
from profiles.serializers import UserProfileSerializer


class ReportImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('src',)


class ReportSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True, read_only=True)
    reporter = UserProfileSerializer(read_only=True)
    votes = serializers.SerializerMethodField()
    is_upvoted = serializers.SerializerMethodField()
    location = PointField(required=False)

    class Meta:
        model = Report
        fields = (
            'id',
            'address_uz',
            'address_ru',
            'location',
            'type',
            'comment',
            'reporter',
            'images',
            'votes',
            'is_upvoted',
        )

    def get_votes(self, report):
        return report.votes.count()

    def get_is_upvoted(self, report):
        return report.votes.filter(user_id=self.context['user']).exists()
