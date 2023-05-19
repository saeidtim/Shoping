from django.contrib import admin
from django.urls import path, include
from .views import HomePageView

handler404 = 'pages.views.handler404'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]