from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from profiles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/profile/register', views.CustomAuthToken.as_view()),
    path('api/profile/', views.UserProfileApiView.as_view()),
    path('api/reports/', include('reports.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)