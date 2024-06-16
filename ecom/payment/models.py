from django.db import models
from django.contrib.auth.models import User

class ShippingAddress(models.Model):
    #to not oblige to save a shipping address
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_full_name = models.CharField(max_length=255)
    shipping_email = models.EmailField(max_length=255)
    shipping_address1 = models.CharField(max_length=255)
    shipping_address2 = models.CharField(max_length=255, null=True, blank=True)
    shipping_city = models.CharField(max_length=255)
    shipping_state = models.CharField(max_length=255, null=True, blank=True)
    shipping_zipcode = models.CharField(max_length=255)
    shipping_country = models.CharField(max_length=255)

    #to pluralize correctly the name of the model in the admin panel
    class Meta:
        verbose_name_plural = 'Shipping Addresses'

    def __str__(self):
        return f'ShippingAddress - {str(self.id)}'
