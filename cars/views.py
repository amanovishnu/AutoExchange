from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Car

def cars(request):
    cars = Car.objects.all().order_by('-created_date')
    paginator = Paginator(cars,2)
    page_number = request.GET['page']
    page_cars = paginator.get_page(page_number)
    data = {'cars':page_cars}
    return render(request, 'cars/cars.html', context=data)


def car_detail(request, id):
    car = get_object_or_404(Car, pk=id)
    print(type(car.features))
    data = {'car':car}
    return render(request, 'cars/car_detail.html', context=data)
