from django import forms
from .models import *


class AccessoryCreateForm(forms.ModelForm):
    class Meta:
        model = Accessory
        fields = ['model', 'content', 'photo', 'price']

