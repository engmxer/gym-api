from django.contrib import admin
from .models import Client, Workout, Booking
# Register your models here.
admin.site.register(Client)
admin.site.register(Workout)
admin.site.register(Booking)
