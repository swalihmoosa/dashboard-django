from django.shortcuts import render

from product.models import Category, Product


def product(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        "categories" : categories,
        "products" : products
    }
    
    return render(request, "products.html", context=context)