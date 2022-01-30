import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class CustomerRequest(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests', default='1')
    # customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, blank=True, null=True, related_name='requests')
    date = models.DateTimeField(default=datetime.datetime.now)
    appeal = models.TextField(null=True, blank=True)
    end_of_work = models.BooleanField(default=False)
    agreed = models.BooleanField(default=False)