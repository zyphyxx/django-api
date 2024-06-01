from django.shortcuts import render
from django.http import HttpResponse
from api.models import Product


# Create your views here.

def prod_views(request):
    search = request.GET.get('search')

    if search:
        products = Product.objects.filter(name__icontains=search).order_by('category')
    else:
        products = Product.objects.all().order_by('category')

    print(request.GET)

    return render(
        request,
        'products.html',
        {'products': products})
