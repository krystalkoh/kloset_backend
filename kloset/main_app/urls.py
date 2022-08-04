from django.urls import path
from . import views

urlpatterns = [
    path('clothes/', views.ClothesList.as_view(), name='clothes'),
    path('users/', views.UsersList.as_view(), name='users'),
    path('jwt-details/', views.JwtDetails.as_view(), name='jwt-details'),
    ]
