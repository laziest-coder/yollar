from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import UserProfileSerializer
from .models import UserProfileManager

UserModel = get_user_model()


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        try:
            user = UserModel.objects.get(
                device_id=request.data['device_id'],
            )
        except UserModel.DoesNotExist:
            user = UserModel.objects.create(
                device_id=request.data['device_id'],
                username=UserProfileManager.generate_random_device_id()
            )
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class UserProfileApiView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
