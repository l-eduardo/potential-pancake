from django import forms
from .models import Task


class CardsForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'owner')
