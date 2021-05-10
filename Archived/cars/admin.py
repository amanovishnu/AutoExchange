from django.contrib import admin
from django.utils.html import format_html
from .models import Car
# Register your models here.

class CarAdmin (admin.ModelAdmin):

    def thumbnail(self,object):
        return format_html('<img src="{}" width="20" style="border-radius: 10px" />'.format(object.car_photo.url))

    thumbnail.short_description ='Car image'
    list_display =['id','thumbnail','car_title','city','color','model','year','body_style','fuel_type','is_featured','price']
    list_display_links = ['id','thumbnail','car_title']
    list_editable = ['is_featured']
    search_fields =['id','car_title','city','model','year','price','body_style','fuel_type']
    list_filter=['city','model','year','body_style','fuel_type']

admin.site.register(Car, CarAdmin)