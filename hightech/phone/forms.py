from django import forms
from .models import *


class PhoneCreateForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = [
            'model', 'content', 'photo', 'cpu', 'ram', 'memory', 
            'battery', 'os', 'back_camera', 'front_camera', 'price'
            ]

