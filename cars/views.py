from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Car

def cars(request):
    cars = Car.objects.all().order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    paginator = Paginator(cars,2)
    try:
        page_number = request.GET['page']
    except:
        page_number = 1
    page_cars = paginator.get_page(page_number)

    data = {
        'cars':page_cars,
        'model_search':model_search,
        'year_search':year_search,
        'city_search':city_search,
        'body_style_search':body_style_search,
        }
    return render(request, 'cars/cars.html', context=data)


def car_detail(request, id):
    car = get_object_or_404(Car, pk=id)
    print(type(car.features))
    data = {'car':car}
    return render(request, 'cars/car_detail.html', context=data)


def search(request):
    cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()


    if 'keyword' in request.GET and request.GET['keyword'] != '':
        keyword = request.GET['keyword']
        cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET and request.GET['model'] != '':
        model = request.GET['model']
        cars = cars.filter(model__iexact=model)

    if 'year' in request.GET and request.GET['year'] != '':
        year = request.GET['year']
        cars = cars.filter(year__iexact=year)

    if 'city' in request.GET and request.GET['city'] != '':
        city = request.GET['city']
        cars = cars.filter(city__iexact=city)

    if 'body_style' in request.GET and request.GET['body_style'] != '':
        body_style = request.GET['body_style']
        cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET and 'max_price' in request.GET and request.GET['min_price'] != '' and request.GET['max_price'] != '' :
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        cars = cars.filter(price__gte=min_price, price__lte=max_price)

    if 'transmission' in request.GET and request.GET['transmission'] != '':
        transmission = request.GET['transmission']
        cars = cars.filter(transmission__iexact=transmission)

    data = {
        'cars':cars,
        'model_search':model_search,
        'year_search':year_search,
        'city_search':city_search,
        'body_style_search':body_style_search,
        'transmission_search':transmission_search,
        }
    return render(request, 'cars/search.html', context=data)
