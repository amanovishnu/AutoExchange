from datetime import datetime
from ckeditor.fields import RichTextField
from django.db import models
from multiselectfield import MultiSelectField


class Car(models.Model):

    state_choice = [
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming')
    ]

    year_choice = [(x,x) for x in range(2000, datetime.now().year+1)]

    features_choices = [
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset')
    ]

    door_choices = [
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6')
    ]

    fuel_choices = [
        ('Petrol','Petrol'),
        ('Diesel','Diesel'),
        ('Electric','Electric'),
        ('Hybrid', 'Hybrid')
    ]

    color_choices = [
        ('Silver', 'Silver'),
        ('White', 'White'),
        ('Black', 'Black'),
        ('Gray', 'Gray'),
        ('Red','Red'),
        ('Blue', 'Blue'),
        ('Brown', 'Brown'),
        ('Beige', 'Beige'),
        ('Orange', 'Orange'),
        ('Gold', 'Gold'),
        ('Yellow', 'Yellow'),
        ('Purple', 'Purple')
    ]

    body_style_choices = [
        ('Sedan', 'Sedan'),
        ('Coupe', 'Coupe'),
        ('Sports Car', 'Sports Car'),
        ('Station Wagon', 'Station Wagon'),
        ('Hatchback', 'Hatchback'),
        ('Convertible', 'Convertible'),
        ('SUV', 'SUV'),
        ('Minivan', 'Minivan'),
        ('Pickup Truck', 'Pickup Truck')
    ]

    transmission_choices = [
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
        ('Semi Automatic', 'Semi Automatic')
    ]

    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=255, default='Alabama')
    city = models.CharField(max_length=255, default='Auburn')
    color = models.CharField(choices=color_choices, max_length=255, default='White')
    model = models.CharField(max_length=255)
    year = models.IntegerField(choices=year_choice)
    condition = models.CharField(max_length=255)
    price = models.IntegerField()
    description = RichTextField()
    car_photo_0 = models.ImageField(upload_to='photos/%Y/%M%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%M%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%M%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%M%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%M%d/', blank=True)
    features = MultiSelectField(choices = features_choices)
    body_style = models.CharField(choices=body_style_choices, max_length=255)
    engine = models.CharField(max_length=255)
    transmission = models.CharField(choices=transmission_choices, max_length=255)
    interior = models.CharField(max_length=255)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=255, default='4')
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=255, default='MSR4562MVM1234USD')
    mileage = models.IntegerField()
    fuel_type = models.CharField(choices=fuel_choices, default='Petrol', max_length=255)
    no_of_owners = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default = datetime.now, blank=True)

    def __str__(self):
        return self.car_title
