from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        add_product = ProdForm(request.POST, request.FILES)
        if add_product.is_valid():
            add_product.save()
            return redirect('prod_list')
    else:
        add_products = ProdForm()

    return render(
        request,
        'add_products.html',
        {'add_products': add_products})
