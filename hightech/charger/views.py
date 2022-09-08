from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import *
from .forms import *


class ChargerPage(ListView):
    model = Charger
    context_object_name = 'charger'
    template_name = 'charger/chargerpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'HIGHTECH | CHARGERS'
        return context


class CreateChargerPage(CreateView):
    form_class = ChargerCreateForm
    template_name = 'charger/createchargerpage.html'
    success_url = '/'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.company = self.request.user
        self.object.save()
        return super().form_valid(form)


class DetailChargerPage(DetailView):
    model = Charger
    context_object_name = 'detailcharger'
    template_name = 'charger/detailchargerpage.html'