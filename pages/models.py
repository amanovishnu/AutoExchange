from django.db import models

# Create your models here.
class Team (models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    facebook_link = models.URLField(max_length=255)
    twitter_link = models.URLField(max_length=255)
    google_link = models.URLField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
