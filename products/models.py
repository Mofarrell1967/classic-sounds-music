from django.db import models

"""
Model for the fields for the site products

"""


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    category = models.CharField(max_length=25, default='')
    description_summary = models.CharField(max_length=100, default='')
    model = models.CharField(max_length=50, default='')
    description = models.TextField(default='')
    maker = models.CharField(max_length=25, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image1 = models.ImageField(upload_to='images', null=True, blank=True)
    image2 = models.ImageField(upload_to='images', null=True, blank=True)
    image3 = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.name
