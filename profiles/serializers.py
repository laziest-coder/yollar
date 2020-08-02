from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ("id", "device_id")
