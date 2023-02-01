from django.db import models

# Create your models here.


class customer(models.Model):
    customerName = models.CharField(max_length=50)
    customerEmail= models.EmailField(max_length=254)
    city  = models.CharField(max_length=50)



    def __str__(self):
        return self.customerName
