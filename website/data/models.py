from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class PagesLiked(models.Model):
    pagename = models.CharField(null = True, max_length = 400)
    id2 = models.IntegerField(null = True)
    accesstoken = models.CharField(max_length = 300)
    abouttext = models.TextField(blank= True, null = True)
    missiontext = models.TextField(blank = True, null = True)
    def __str__(self):
        return str(self.id2) + " " + str(self.pagename)