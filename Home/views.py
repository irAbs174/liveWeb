from django.shortcuts import render , redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import View
from .models import PageAdmin


class Home(View):
    def get(self, request, *args, **kwargs):
        page = PageAdmin.objects.all()
        return render(request, 'Home/index.html', context={'key':page})


class PanelView(View):
    def get(self, request, *args, **kwargs):
        page = PageAdmin.objects.all()
        return render(request, 'Home/panel.html', context={'key':page})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            
            user = form.save()
            auth_login(request, user)
            return redirect('/accounts/panel')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})