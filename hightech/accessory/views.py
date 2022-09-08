from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Accessory
from .forms import *


class AccessoryPage(ListView):
    model = Accessory
    template_name = 'accessory/accessorypage.html'
    context_object_name = 'accessory'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'HIGHTECH | ACCESSORIES'
        return context

class CreateAccessoryPage(CreateView):
    form_class = AccessoryCreateForm
    template_name = 'accessory/createaccessorypage.html'
    success_url = '/'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.company = self.request.user
        self.object.save()
        return super().form_valid(form)


class DetailAccessoryPage(DetailView):
    model = Accessory
    context_object_name = 'detailaccessory'
    template_name = 'accessory/detailaccessorypage.html'