from django.shortcuts import render
from django.http import HttpResponse
from api.models import Product


# Create your views here.

def prod_views(request):
    products = Product.objects.all()

    return render(
        request,
        'products.html',
        {'products': products})
