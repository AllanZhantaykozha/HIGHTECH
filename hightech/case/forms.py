from django import forms
from .models import *


class CaseCreateForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['model', 'content', 'photo', 'phone_model', 'price']

