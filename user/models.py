from django.db import models

# Create your models here.
class Order(models.Model):
    order_numer = models.CharField(max_length=100)

    def __str__(self):
        return self.order_numer