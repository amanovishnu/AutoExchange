from django.contrib import admin
from .models import Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html(f'<img src="{object.photo.url}" width="30" style="border-radius:5px;" alt="{object.first_name}"/>')
    thumbnail.short_description = 'Photo'

    list_display = ['id', 'thumbnail', 'first_name', 'last_name', 'designation', 'created_date']
    list_display_links = ['id', 'thumbnail', 'first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'designation']
    list_filter = ['designation']
    ordering = ['id']


admin.site.register(Team, TeamAdmin)
