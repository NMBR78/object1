from django.conf import settings
from django.db import models
from django.utils import timezone

class Name(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name+ ' ' + self.last_name

class Person(models.Model):
    nickname = models.CharField('PALATA', max_length=120)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=300)
    date = models.DateTimeField('Date')
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nickname