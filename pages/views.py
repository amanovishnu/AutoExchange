from django.shortcuts import render
from .models import Team


def home(request):
    teams = Team.objects.all()
    return render(request, 'pages/home.html', context={'teams':teams})


def about(request):
    teams = Team.objects.all().order_by('id')
    return render(request, 'pages/about.html', context={'teams':teams})


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
