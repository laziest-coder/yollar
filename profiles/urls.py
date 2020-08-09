from django.urls import path
from profiles import views

urlpatterns = [
    path('', views.UserProfileApiView.as_view()),
    path('register', views.CustomAuthToken.as_view()),
]