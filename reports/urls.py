from django.urls import path
from .views import report, votes

urlpatterns = [
    path('', report.ReportList.as_view()),
    path('<int:pk>/', report.ReportDetail.as_view()),
    path('<int:pk>/attach-images', report.ReportImage.as_view()),
    path('<int:pk>/upvote', votes.ReportUpVote.as_view()),
    path('<int:pk>/unvote', votes.ReportUnVote.as_view()),
]