from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Car

# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 2)
    page_no = request.GET.get('page')
    try:
        paged_cars  = paginator.page(page_no)
    except PageNotAnInteger:
        paged_cars = paginator.page(1)
    except EmptyPage:
        paged_cars = paginator.page(paginator.num_pages)
    print(f'Test -> {paginator.num_pages}')
    data = {'cars':paged_cars}
    return render(request, 'cars/cars.html', context=data)

def car_detail(request, id):
    object = get_object_or_404(Car, id=id)
    print('Hello World ->', type(object.features))
    data = {'car': object}
    return render(request, 'cars/car_detail.html', context=data)
