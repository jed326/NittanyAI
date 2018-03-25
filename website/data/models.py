from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# Create your models here.
class PagesLiked(models.Model):
    uuid = models.UUIDField(null = True)
    accesstoken = models.CharField(max_length = 300)
    abouttext = models.TextField(blank= True, null = True)
    missiontext = models.TextField(blank = True, null = True)
