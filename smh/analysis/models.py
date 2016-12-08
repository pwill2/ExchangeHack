from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class tweetAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.CharField(max_length=140)
    cleaned_tweet = models.CharField(max_length=140)
    
