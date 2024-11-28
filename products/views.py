from django.shortcuts import render
from .models import Product

# Create your views here.
def product_view(request):
    return render(request, 'products/product.html')
def products_view(request):

    return render(request, 'products/products.html', {'pro': Product.objects.get(name='Ahmed')})
