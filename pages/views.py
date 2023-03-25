from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages


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
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    phone_number = request.POST.get('phone_number')
    message = request.POST.get('message')

    admin_info = User.objects.get(is_superuser=True)
    admin_email_id = admin_info.email

    message_body = f'''
      Name: {name},
      Email: {email},
      Phone Number: {phone_number},
      Message: {message}
    '''

    # send_mail(
    #   subject,
    #   message_body,
    #   'dev.geekymano@gmail.com',
    #   [admin_email_id],
    #   fail_silently=False
    # )

    messages.success(request,'Thank you for contacting us. we will get back to you shortly.')
    return redirect('contact')

  return render(request, 'pages/contact.html')
