from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .forms import PhoneCreateForm
from .models import *
from django.contrib import messages


class PhonePage(ListView):
    model = Phone
    context_object_name = 'phone'
    template_name = 'phone/phonepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'HIGHTECH'
        return context

class CreatePhonePage(CreateView):
    form_class = PhoneCreateForm
    template_name = 'phone/createphonepage.html'
    success_url = '/'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.company = self.request.user
        self.object.save()
        return super().form_valid(form)

class DetailPhonePage(DetailView):
    model = Phone
    context_object_name = 'detailphone'
    template_name = 'phone/detailphonepage.html'