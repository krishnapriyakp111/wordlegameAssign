from django.db import models

# Create your models here.
   
class game(models.Model):
    word = models.CharField(max_length=100)
    