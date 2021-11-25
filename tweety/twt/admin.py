from django.contrib import admin
from .models import *


class twtadmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'time_crate', 'img')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')


admin.site.register(TWEET,twtadmin)