from django.contrib import admin
from django.urls import path, include
from profiles import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api/profile/register', views.CustomAuthToken.as_view()),
    path('api/profile/', views.UserProfileApiView.as_view()),
    path('api/reports/', include('reports.urls'))
]
