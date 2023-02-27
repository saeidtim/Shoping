from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11, blank=True, null=True)
    age = models.PositiveIntegerField(default=18, blank=True, null=True)
