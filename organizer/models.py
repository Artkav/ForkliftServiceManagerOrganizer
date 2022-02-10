import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Customer(models.Model):
    name = models.CharField(max_length=128, unique=True)
    legal_name = models.CharField(max_length=128, unique=True, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    caller = models.TextField(null=True, blank=True)
    lifting_equipment = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def url(self):
        return reverse('organizer:customer-detail', kwargs={'pk': self.id})


class CustomerRequest(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests', default='1')
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, blank=True, null=True, related_name='requests')
    date = models.DateTimeField(default=datetime.datetime.now)
    appeal = models.TextField(null=True, blank=True)
    end_of_work = models.BooleanField(default=False)
    agreed = models.BooleanField(default=False)