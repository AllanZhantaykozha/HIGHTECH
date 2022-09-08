from django import forms
from .models import *


class ChargerCreateForm(forms.ModelForm):
    class Meta:
        model = Charger
        fields = ['model', 'content', 'photo', 'power', 'types', 'price']

