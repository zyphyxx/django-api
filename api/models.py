from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    lastname = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    service_time = models.IntegerField(default=0, null=False, blank=False)
    remuneration = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return f"{self.name} {self.lastname}"


class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', default=1)
    photo = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.name
