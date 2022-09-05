from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class ChargerPage(ListView):
    model = Charger
    context_object_name = 'charger'
    template_name = 'charger/chargerpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'HIGHTECH | CHARGERS'
        return context

