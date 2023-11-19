from django import forms
from .models import Card, SharedCard


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('id', 'title', 'description', 'owner')


class SharedCardForm(forms.ModelForm):
    class Meta:
        model = SharedCard
        fields = ('card', 'shared_with', 'shared_group')
