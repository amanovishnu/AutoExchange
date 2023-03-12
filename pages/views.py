from django.shortcuts import render
from .models import Team
from cars.models import Car


def home(request):
  teams = Team.objects.all()
  featured_cars = Car.objects.order_by('-created_date').filter(is_featured = True)
  latest_cars = Car.objects.order_by('-created_date')
  model_field = Car.objects.values_list('model', flat=True).distinct()
  city_field = Car.objects.values_list('city', flat=True).distinct()
  year_field = Car.objects.values_list('year', flat=True).distinct()
  body_style_field = Car.objects.values_list('body_style', flat=True).distinct()
  data = {
    'teams': teams,
    'featured_cars': featured_cars,
    'latest_cars': latest_cars,
    'model_field': model_field,
    'city_field': city_field,
    'year_field': year_field,
    'body_style_field': body_style_field,
    }
  return render(request, 'pages/home.html', context = data)

def about(request):
  teams = Team.objects.all()
  data = {'teams': teams}
  return render(request, 'pages/about.html', context = data)

def services(request):
  return render(request, 'pages/services.html')

def contact(request):
  return render(request, 'pages/contact.html')
