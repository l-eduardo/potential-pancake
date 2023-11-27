from django.db import models
from django.contrib.auth.models import User, Group


class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def user_has_permission(self, user, permission_codename):
        if user == self.owner:
            return True

        shared_card = SharedCard.objects.filter(card=self, shared_with=user).first()
        if shared_card:
            return SharedCard.objects.filter(shared_group__name=shared_card.shared_group.name,
                                             shared_group__permissions__codename=permission_codename).exists()
        return False

    def __str__(self):
        return self.title


class SharedCard(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    shared_with = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_group = models.ForeignKey(Group, on_delete=models.CASCADE)
