from django.contrib import admin
from django.urls import path, include

from .views import CreateUser


urlpatterns = [
    path('signup/', CreateUser.as_view(), name='signup'),
]