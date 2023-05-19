from django.db import models

# Create your models here.

class PublicModel(models.Model):
    view = models.IntegerField(default=0)
