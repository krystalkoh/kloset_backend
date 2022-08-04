from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('routes/', include('main_app.urls')),
    path('admin/', admin.site.urls),
]

