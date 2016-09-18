import uuid
import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

@python_2_unicode_compatible
class User(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=100)
    #tracked_stocks = array of tracked stocks
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        full_name = first_name + ' ' + last_name
        return self.full_name

class Stock(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=7)

    def __str__(self):
        stock = name + ": " + ticker
        return self.stock
