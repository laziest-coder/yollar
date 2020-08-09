from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from reports.models import Report, Vote
from reports.serializers import ReportSerializer


class ReportVote(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        try:
            report = Report.objects.get(pk=pk)
            report.current_user = request.user
            serializer = ReportSerializer(report)
        except Report.DoesNotExist:
            return Response({"error": "Report not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            report_vote = Vote.objects.get(report=report, reporter=request.user)
            report_vote.delete()
            return Response(serializer.data)
        except Vote.DoesNotExist:
            Vote.objects.create(report=report, reporter=request.user)
            return Response(serializer.data)
