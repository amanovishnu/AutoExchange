from django.db import models


class Car(models.Model):

    state_choicd = (
        ()
    )

    car_title = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    features = models.CharField(max_length=255)


    def __str__(self):
        return self.title
