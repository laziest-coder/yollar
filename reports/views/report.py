from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from reports.models import Report, Image


class ReportList(APIView):

    def get(self, request):
        reports = Report.objects.all()
        return Response(reports)
