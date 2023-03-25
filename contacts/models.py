from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  car_id = models.IntegerField()
  customer_query = models.CharField(max_length=255)
  car_title = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  phone_number = models.CharField(max_length=255)
  comments = models.TextField(max_length=255, blank=True)
  user_id = models.IntegerField()
  created_date = models.DateTimeField(blank=True, default=datetime.now)

  def __str__(self):
    return self.email
