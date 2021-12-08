from django.http.response import JsonResponse
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


def category(request):
    category_name = request.GET.get("category")

    if category_name:
        if Category.objects.filter(category_name=category_name).exists():
            if Product.objects.filter(category__category_name=category_name).exists():
                products = Product.objects.filter(category__category_name=category_name).values()
                data = list(products)

                response_data = {
                    "title" : "Success",
                    "data" : data
                }
            else:
                response_data = {
                    "title" : "Failed",
                    "data" : "Product not found"
                }
        else:
            response_data = {
                    "title" : "Failed",
                    "data" : "Category not found"
                }
    else:
        response_data = {
            "title" : "Failed",
            "data" : "No Category"
        }

    return JsonResponse({'response_data' : response_data})
