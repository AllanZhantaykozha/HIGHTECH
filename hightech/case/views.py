from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class CasePage(ListView):
    model = Case
    template_name = 'case/casepage.html'
    context_object_name = 'case'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'HIGHTECH | CASES'
        return context
