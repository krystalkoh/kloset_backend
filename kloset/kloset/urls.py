from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main_app.urls')),
    path('jwt-api/', include('restful_apis_with_jwt.urls')),
]

