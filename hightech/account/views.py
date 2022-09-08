from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView
from .forms import *
from django.contrib.auth import login as login_def, logout as logout_def
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = AccountRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login_def(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('phone')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = AccountRegisterForm()
    return render(request, 'account/register.html', {"form": form})

def login(request):
    if request.method == 'POST':
        form = AccountLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login_def(request, user)
            messages.success(request, 'Вы успешно авторизовались')
            return redirect('phone')
        else:
            messages.error(request, 'Ошибка авторизации')
    else:
        form = AccountLoginForm() 
    return render(request, 'account/login.html', {"form": form})

    
def logout(request):
    logout_def(request)
    return redirect('login')


class AccountPage(ListView):
    model = User
    context_object_name = 'user'
    template_name = 'account/accountpage.html'