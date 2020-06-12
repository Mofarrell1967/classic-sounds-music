from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=254, default='')
    email = models.CharField(max_length=254, default='')
    subject = models.CharField(max_length=254, default='')
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
