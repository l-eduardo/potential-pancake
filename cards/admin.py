from django.contrib import admin

from cards.models import Card, SharedCard

# Register your models here.
admin.site.register(Card)
admin.site.register(SharedCard)
