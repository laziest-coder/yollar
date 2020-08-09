from django.urls import path
from .views import report

urlpatterns = [
    path('', report.ReportList.as_view()),
    path('<int:pk>/', report.ReportDetail.as_view()),
    path('<int:pk>/attach-images', report.ReportImage.as_view())
]