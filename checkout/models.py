from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django.utils import timezone


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    user = models.ForeignKey(User, null=True)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    order_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, related_name="item")
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)
    order_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)
    user = models.ForeignKey(User, null=True, default=User)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.product.name, self.product.price)
