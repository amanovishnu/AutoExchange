from django.shortcuts import render
from .models import Team
from cars.models import Car
from pprint import pprint


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    latest_cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams':teams,
        'featured_cars':featured_cars,
        'latest_cars':latest_cars,
        'model_search':model_search,
        'year_search':year_search,
        'city_search':city_search,
        'body_style_search':body_style_search,
    }
    return render(request, 'pages/home.html', context=data)


def about(request):
    teams = Team.objects.all().order_by('id')
    return render(request, 'pages/about.html', context={'teams':teams})


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
