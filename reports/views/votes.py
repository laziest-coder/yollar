from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.db import IntegrityError
from reports.models import Report, Vote
from reports.serializers import ReportSerializer


class ReportUpVote(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        try:
            report = Report.objects.get(pk=pk)
            serializer = ReportSerializer(report, context={'user': request.user})
        except Report.DoesNotExist:
            return Response({"error": "Report not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            report_vote = Vote.objects.create(report=report, user=request.user)
            return Response(serializer.data)
        except Vote.DoesNotExist:
            return Response({'message': 'Whoops! Looks like smth went wrong.'}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response({'message': 'You have already upvoted the report!'}, status=status.HTTP_400_BAD_REQUEST)


class ReportUnVote(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        try:
            report = Report.objects.get(pk=pk)
            serializer = ReportSerializer(report, context={'user': request.user})
        except Report.DoesNotExist:
            return Response({"error": "Report not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            report_vote = Vote.objects.get(report=report, user=request.user)
            report_vote.delete()
            return Response(serializer.data)
        except Vote.DoesNotExist:
            return Response({'message': 'You have not liked the report!'}, status=status.HTTP_400_BAD_REQUEST)
