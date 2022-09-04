from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class PhonePage(ListView):
    model = Phone
    context_object_name = 'phone'
    template_name = 'phone/phonepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'HIGHTECH'
        return context
