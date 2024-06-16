from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem

#to register the models on the admin panel

admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)