from django.contrib import admin
from api.models import Employee, Product, Category


# Register your models here.

class EAdmin (admin.ModelAdmin):
    list_display = ('name', 'lastname', 'cpf', 'service_time', 'remunetarion')
    search_fields = 'name'

    admin.site.register(Employee)
    admin.site.register(Product)
    admin.site.register(Category)
