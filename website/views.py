from django.shortcuts import render
from django.http import HttpResponse
from api.models import Product
from website.forms import ProdForm


# Create your views here.

def prod_views(request):
    search = request.GET.get('search')

    if search:
        products = Product.objects.filter(name__icontains=search).order_by('category')
    else:
        products = Product.objects.all().order_by('category')

    return render(
        request,
        'products.html',
        {'products': products})


def add_product_views(request):

    add_products = ProdForm()

    return render(
        request,
        'add_products.html',
        {'add_products': add_products})




