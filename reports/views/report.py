from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from reports.models import Report, Image
from reports.serializers import ReportSerializer


class ReportList(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)
