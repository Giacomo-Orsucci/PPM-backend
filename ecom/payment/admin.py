from django.contrib import admin
from .models import ShippingAddress

#to register the models on the admin panel

admin.site.register(ShippingAddress)