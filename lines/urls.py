import imp
from django.urls import path, include
from django.contrib.auth.models import User
from .views import AppView, HomeView

urlpatterns = [
    path('calculations/', AppView.as_view(), name='calc'),
    path('', HomeView.as_view(), name='home')
]
