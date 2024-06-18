from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User

#to register the models on the admin panel

admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)

#to inline an OrderItem
class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0 #to not show any extra OrderItem not ordered

#extending Order Model
class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ["date_ordered"]
    fields = ["user", "full_name", "email", "shipping_address", "amount_paid", "date_ordered", "shipped", "date_shipped"]
    inlines = [OrderItemInline]
#it is necessary to unregister the Order model before registering it again
admin.site.unregister(Order)
admin.site.register(Order, OrderAdmin)