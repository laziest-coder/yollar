from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from reports.models import Report, Image
from reports.serializers import ReportSerializer
from django.http import Http404


class ReportList(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True, context={'user': request.user})
        return Response(serializer.data)

    def post(self, request):
        serializer = ReportSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save(reporter=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReportDetail(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            report = Report.objects.get(pk=pk)
            serializer = ReportSerializer(report, context={'user': request.user})
            return Response(serializer.data)
        except Report.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        try:
            report = Report.objects.get(pk=pk, reporter_id=request.user)
            serializer = ReportSerializer(report, data=request.data, context={'user': request.user})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Report.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        try:
            report = Report.objects.get(pk=pk, reporter_id=request.user)
            report.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Report.DoesNotExist:
            raise Http404


class ReportImage(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        try:
            report = Report.objects.get(pk=pk, reporter_id=request.user)
            images = request.FILES
            Image.objects.filter(report=report).delete()
            for image in images.getlist('images'):
                Image.objects.create(report=report, src=image)
            serializer = ReportSerializer(report, context={'user': request.user})
            return Response(serializer.data)
        except Report.DoesNotExist:
            raise Http404
