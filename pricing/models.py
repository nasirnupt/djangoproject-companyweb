from django.db import models


# Create your models here.
class Pricing(models.Model):
    title = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(default=0, max_digits=1000, decimal_places=2)
    data_1 = models.CharField(max_length=200, blank=True)
    data_2 = models.CharField(max_length=200, blank=True)
    data_3 = models.CharField(max_length=200, blank=True)
    data_4 = models.CharField(max_length=200, blank=True)
    data_5 = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
