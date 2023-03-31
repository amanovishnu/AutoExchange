import random

from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


# Create your models here.
class Car(models.Model):

  state_choice = [
        ['AL', 'Alabama'],
        ['AK', 'Alaska'],
        ['AZ', 'Arizona'],
        ['AR', 'Arkansas'],
        ['CA', 'California'],
        ['CO', 'Colorado'],
        ['CT', 'Connecticut'],
        ['DE', 'Delaware'],
        ['DC', 'District Of Columbia'],
        ['FL', 'Florida'],
        ['GA', 'Georgia'],
        ['HI', 'Hawaii'],
        ['ID', 'Idaho'],
        ['IL', 'Illinois'],
        ['IN', 'Indiana'],
        ['IA', 'Iowa'],
        ['KS', 'Kansas'],
        ['KY', 'Kentucky'],
        ['LA', 'Louisiana'],
        ['ME', 'Maine'],
        ['MD', 'Maryland'],
        ['MA', 'Massachusetts'],
        ['MI', 'Michigan'],
        ['MN', 'Minnesota'],
        ['MS', 'Mississippi'],
        ['MO', 'Missouri'],
        ['MT', 'Montana'],
        ['NE', 'Nebraska'],
        ['NV', 'Nevada'],
        ['NH', 'New Hampshire'],
        ['NJ', 'New Jersey'],
        ['NM', 'New Mexico'],
        ['NY', 'New York'],
        ['NC', 'North Carolina'],
        ['ND', 'North Dakota'],
        ['OH', 'Ohio'],
        ['OK', 'Oklahoma'],
        ['OR', 'Oregon'],
        ['PA', 'Pennsylvania'],
        ['RI', 'Rhode Island'],
        ['SC', 'South Carolina'],
        ['SD', 'South Dakota'],
        ['TN', 'Tennessee'],
        ['TX', 'Texas'],
        ['UT', 'Utah'],
        ['VT', 'Vermont'],
        ['VA', 'Virginia'],
        ['WA', 'Washington'],
        ['WV', 'West Virginia'],
        ['WI', 'Wisconsin'],
        ['WY', 'Wyoming'],
]

  year_choice = []
  for year in range(2000, datetime.now().year+1):
    year_choice.append([year,year])

  features_choices = [
          ['Cruise Control', 'Cruise Control'],
          ['Audio Interface', 'Audio Interface'],
          ['Airbags', 'Airbags'],
          ['Air Conditioning', 'Air Conditioning'],
          ['Seat Heating', 'Seat Heating'],
          ['Alarm System', 'Alarm System'],
          ['ParkAssist', 'ParkAssist'],
          ['Power Steering', 'Power Steering'],
          ['Reversing Camera', 'Reversing Camera'],
          ['Direct Fuel Injection', 'Direct Fuel Injection'],
          ['Auto Start/Stop', 'Auto Start/Stop'],
          ['Wind Deflector', 'Wind Deflector'],
          ['Bluetooth Handset', 'Bluetooth Handset'],
  ]

  door_choices = [
          ['2', '2'],
          ['3', '3'],
          ['4', '4'],
          ['5', '5'],
          ['6', '6'],
      ]

  engine_choices = [
    ['Ford Supercharged 5.2-Liter V8: A Predator', 'Ford Supercharged 5.2-Liter V8: A Predator'],
    ['Ram High Output Turbocharged 6.7-Liter Inline-Six', 'Ram High Output Turbocharged 6.7-Liter Inline-Six'],
    ['Mazda SKYACTIV-G 2.0-Liter Inline-Four', 'Mazda SKYACTIV-G 2.0-Liter Inline-Four'],
    ['Ford High Output 3.5-Liter Twin-Turbo V6', 'Ford High Output 3.5-Liter Twin-Turbo V6'],
    ['Volkswagen Auto Group Twin-Turbo 4.0-Liter V8', 'Volkswagen Auto Group Twin-Turbo 4.0-Liter V8'],
    ['Chevrolet 6.2-Liter V8', 'Chevrolet 6.2-Liter V8'],
    ['Dodge Supercharged 6.2-Liter V8', 'Dodge Supercharged 6.2-Liter V8'],
    ['Ferrari Twin-Turbocharged 3.9-Liter V8', 'Ferrari Twin-Turbocharged 3.9-Liter V8'],
    ['BMW Twin-Turbo 4.4-Liter V8', 'BMW Twin-Turbo 4.4-Liter V8'],
    ['Audi Turbocharged 2.5-Liter Inline-Five', 'Audi Turbocharged 2.5-Liter Inline-Five']
  ]

  transmission_choices = [
    ['Manual ', 'Manual '],
    ['Automatic', 'Automatic '],
    ['Automatic-CVT', 'Automatic-CVT '],
    ['Automatic-SAT', 'Automatic-SAT '],
    ['Automatic-DCT', 'Automatic-DCT '],
  ]

  fuel_choices = [
    ['Petrol', 'Petrol'],
    ['Diesel', 'Diesel'],
    ['Electric', 'Electric'],
    ['Hydrogen', 'Hydrogen'],
    ['Hybrid', 'Hybrid'],
    ['Solar', 'Solar'],
  ]

  owner_choices = [
    ['1','1'],
    ['2','2'],
    ['3','3'],
    ['4','4'],
    ['5','5'],
  ]

  body_style_choices = [
    ['City Car','City Car'],
    ['Super Mini','Super Mini'],
    ['Hatchback','Hatchback'],
    ['MPV', 'MPV'],
    ['Saloon','Saloon'],
    ['Estate','Estate'],
    ['Coupe','Coupe'],
    ['Crossover','Crossover'],
    ['SUV','SUV'],
    ['Cabriolet','Cabriolet'],
    ['Super Car','Super Car']
  ]

  car_title = models.CharField(max_length=255)
  state = models.CharField(max_length=100, choices=state_choice)
  city = models.CharField(max_length=100)
  color = models.CharField(max_length=50, default='white')
  model = models.CharField(max_length=150)
  year = models.IntegerField(choices=year_choice)
  condition = models.CharField(max_length=255, default='Good')
  price = models.IntegerField(default=2000)
  description = RichTextField()
  car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  features = MultiSelectField(choices=features_choices)
  body_style = models.CharField(max_length=255, choices=body_style_choices, default='Super Car')
  engine = models.CharField(max_length=255, choices=engine_choices, default='Audi Turbocharged 2.5-Liter Inline-Five')
  transmission = models.CharField(max_length=255, choices=transmission_choices, default='Manual')
  interior = models.CharField(max_length=255)
  miles = models.IntegerField(default= random.randint(1000,150000))
  doors = models.CharField(max_length=255, choices=door_choices, default='2')
  passengers = models.IntegerField(default=2)
  vin_no = models.CharField(max_length=255)
  mileage = models.IntegerField(default=random.randint(5,20))
  fuel_type = models.CharField(max_length=255, choices=fuel_choices, default='Petrol')
  no_of_owners = models.CharField(max_length=10, choices=owner_choices, default='1')
  is_featured = models.BooleanField(default=False)
  created_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.car_title
