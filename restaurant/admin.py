from django.contrib import admin
from .models import Menu, Booking

# class MenuAdmin(admin.ModelAdmin):
#     list_display = ['title', 'get_item', 'price', 'inventory']

# Register your models here.
admin.site.register(Menu)
admin.site.register(Booking)
