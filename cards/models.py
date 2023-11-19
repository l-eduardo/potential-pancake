from django.db import models
from django.contrib.auth.models import User, Group


class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class SharedCard(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    shared_with = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_group = models.ForeignKey(Group, on_delete=models.CASCADE)
