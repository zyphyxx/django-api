from django.contrib import admin
from .models import Employee, Product, Category


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'cpf', 'service_time', 'remuneration')
    search_fields = ('name', 'lastname', 'cpf')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category')
    search_fields = ('name', 'description', 'price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
