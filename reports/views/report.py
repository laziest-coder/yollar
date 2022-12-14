from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.http import Http404
from django.db.models import Q
from reports.models import Report, Image
from reports.serializers import ReportSerializer


class ReportList(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        reports = Report.objects.all().filter(is_verified=True)
        if request.GET.get("query"):
            query = request.GET['query']
            reports = reports.filter(
                Q(region_uz__contains=query) | Q(region_ru__contains=query) |
                Q(district_uz__contains=query) | Q(district_ru__contains=query) |
                Q(street_uz__contains=query) | Q(street_ru__contains=query)
            )
        serializer = ReportSerializer(reports, many=True, context={'user': request.user, 'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ReportSerializer(data=request.data, context={'user': request.user, 'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(reporter=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReportDetail(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            report = Report.objects.get(pk=pk)
            serializer = ReportSerializer(report, context={'user': request.user, 'request': request})
            return Response(serializer.data)
        except Report.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        try:
            report = Report.objects.get(pk=pk, reporter_id=request.user)
            serializer = ReportSerializer(report, data=request.data, context={'user': request.user, 'request': request})
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
            if len(images) > 4:
                return Response({'error': 'Max number of images to uplaod is 4.'}, status=status.HTTP_400_BAD_REQUEST)
            Image.objects.filter(report=report).delete()
            for image in images.getlist('images'):
                Image.objects.create(report=report, src=image)
            serializer = ReportSerializer(report, context={'user': request.user, 'request': request})
            return Response(serializer.data)
        except Report.DoesNotExist:
            raise Http404
