from django.db import models
from django.contrib.auth.models import AbstractUser

############################################################
#User class
#===========================================================
#This class replace the default user class
############################################################
class User(AbstractUser):
    address = models.TextField()
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    studies = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)