from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Contact (models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=CharField(max_length=100)
    def __str__(self):
        return self.name
    