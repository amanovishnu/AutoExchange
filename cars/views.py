from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Car

# Create your views here.
def cars(request):
    model_field = Car.objects.values_list('model', flat=True).distinct()
    city_field = Car.objects.values_list('city', flat=True).distinct()
    year_field = Car.objects.values_list('year', flat=True).distinct()
    body_style_field = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_field = Car.objects.values_list('transmission', flat=True).distinct()
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 4)
    page_no = request.GET.get('page')
    try:
        paged_cars  = paginator.page(page_no)
    except PageNotAnInteger:
        paged_cars = paginator.page(1)
    except EmptyPage:
        paged_cars = paginator.page(paginator.num_pages)
    data = {
        'cars':paged_cars,
        'model_field': model_field,
        'city_field': city_field,
        'year_field': year_field,
        'body_style_field': body_style_field,
        'transmission_field': transmission_field,
    }
    return render(request, 'cars/cars.html', context=data)

def car_detail(request, id):
    object = get_object_or_404(Car, id=id)
    data = {'car': object}
    return render(request, 'cars/car_detail.html', context=data)

def search(request):
    model_field = Car.objects.values_list('model', flat=True).distinct()
    city_field = Car.objects.values_list('city', flat=True).distinct()
    year_field = Car.objects.values_list('year', flat=True).distinct()
    body_style_field = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_field = Car.objects.values_list('transmission', flat=True).distinct()
    color_field = Car.objects.values_list('color', flat=True).distinct()
    cars = Car.objects.order_by('-created_date')

    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')
        if keyword:
            cars = cars.filter(description__icontains = keyword)

    if 'model' in request.GET:
        model = request.GET.get('model')
        if model:
            cars = cars.filter(model__iexact = model)

    if 'year' in request.GET:
        year = request.GET.get('year')
        if year:
            cars = cars.filter(year__iexact = year)

    if 'city' in request.GET:
        city = request.GET.get('city')
        if city:
            cars = cars.filter(city__iexact = city)

    if 'body_style' in request.GET:
        body_style = request.GET.get('body_style')
        if body_style:
            cars = cars.filter(body_style__iexact = body_style)

    if 'transmission' in request.GET:
        transmission = request.GET.get('transmission')
        if transmission:
            cars = cars.filter(transmission__iexact = transmission)

    if 'color' in request.GET:
        color = request.GET.get('color')
        if color:
            cars = cars.filter(color__iexact = color)


    if 'min_price' in request.GET or 'max_price' in request.GET:
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        cars = cars.filter(price__gte = min_price, price__lte = max_price) # Using And Condition

    data = {
        'cars': cars,
        'model_field': model_field,
        'city_field': city_field,
        'year_field': year_field,
        'body_style_field': body_style_field,
        'transmission_field': transmission_field,
        'color_field': color_field,
    }
    return render(request, 'cars/search.html', context=data)
