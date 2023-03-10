from django.db import models


class Team(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  designation = models.CharField(max_length=255)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  facebook_link = models.URLField(max_length=100, blank=True, default='https://www.facebook.com')
  twitter_link = models.URLField(max_length=100, blank=True, default='https://twitter.com')
  linkedin_link = models.URLField(max_length=100, blank=True, default='https://www.linkedin.com')
  created_date = models.DateField(auto_now_add=True)

  def __str__(self):
    return f'{self.first_name} {self.last_name}'
