from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
