from rest_framework import serializers
from reports.models import Report, Image
from profiles.serializers import UserProfileSerializer


class ReportImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('src',)


class ReportSerializer(serializers.ModelSerializer):
    images = ReportImageSerializer(many=True, read_only=True)
    reporter = UserProfileSerializer(read_only=True)
    votes = serializers.SerializerMethodField()
    is_upvoted = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = (
            'id',
            'address_uz',
            'address_ru',
            'latitude',
            'longitude',
            'type',
            'comment',
            'reporter',
            'images',
            'votes',
            'is_upvoted'
        )

    def get_votes(self, report):
        return report.votes.count()

    def get_is_upvoted(self, report):
        return report.votes.filter(reporter_id=self.context['user']).exists()


