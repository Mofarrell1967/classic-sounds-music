from django.db import models

"""
Model for the fields for the site products

"""


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    category = models.CharField(max_length=25, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
