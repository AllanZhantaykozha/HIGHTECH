from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import *
from .forms import *


class CasePage(ListView):
    model = Case
    template_name = 'case/casepage.html'
    context_object_name = 'case'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'HIGHTECH | CASES'
        return context

class CreateCasePage(CreateView):
    form_class = CaseCreateForm
    template_name = 'case/createcasepage.html'
    success_url = '/'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.company = self.request.user
        self.object.save()
        return super().form_valid(form)


class DetailCasePage(DetailView):
    model = Case
    context_object_name = 'detailcase'
    template_name = 'case/detailcasepage.html'