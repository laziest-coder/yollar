from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import UserProfileSerializer

UserModel = get_user_model()


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        try:
            user, created = UserModel.objects.get_or_create(
                device_id=request.data['device_id']
            )
            user.save()

            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        except:
            return Response({"error": "Whoops! Looks like something went wrong."}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileApiView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
