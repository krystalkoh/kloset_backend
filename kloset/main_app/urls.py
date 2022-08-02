from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('cost/', views.cost, name='cost'),
]