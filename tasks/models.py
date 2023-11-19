from django.db import models

from cards.models import Card


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
