from django.contrib import admin
from django.utils.html import format_html
from .models import Car


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(f'<img src={object.car_photo_0.url} width="50px" style="border-radius:5px" />')

    thumbnail.short_description = 'photo'

    list_display = ['thumbnail', 'car_title', 'miles',  'color', 'model', 'price', 'engine', 'transmission', 'is_featured']
    list_display_links= ['thumbnail', 'car_title']
    list_filter = ['fuel_type', 'condition', 'features', 'body_style', 'transmission', 'doors']
    list_editable = ['is_featured']
    search_fields = ['id', 'car_title', 'city', 'fuel_type', 'transmission', 'description']

admin.site.register(Car, CarAdmin)
