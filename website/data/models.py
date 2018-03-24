from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# Create your models here.
class PagesLiked(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    accesstoken = models.CharField(max_length = 300)
    likedpages = models.CharField(max_length = 600)

    def __str__(self):
        return self.id