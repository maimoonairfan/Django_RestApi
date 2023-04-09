from django.db import models

# Create your models here.
class Product(models.Model):
    category = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    name = models.CharField(max_length = 100)

    def __str___(self):
        return self.name