from django.shortcuts import render

from products.models import ProductCategory, Product


# Create your views here.
def index(request):
    context = {'title': 'Test Title',
               'is_promotion': False, }
    return render(request, 'products/index.html', context=context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context=context)
