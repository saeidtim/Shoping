from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import CreateUser


urlpatterns = [
    path('signup/', CreateUser.as_view(), name='signup'),
]