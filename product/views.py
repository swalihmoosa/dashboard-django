import json
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

from product.models import Category, ProductItem
from product.forms import ProductForm


def productitem(request):
    categories = Category.objects.all()
    products = ProductItem.objects.all()

    context = {
        "categories" : categories,
        "products" : products
    }

    return render(request, "products.html", context=context)


def category(request):
    category_name = request.GET.get("category")

    if category_name:
        if Category.objects.filter(category_name=category_name).exists():
            if ProductItem.objects.filter(category__category_name=category_name).exists():
                products = ProductItem.objects.filter(category__category_name=category_name).values()
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


def add_new_product(request):
    form = ProductForm()

    context = {
        "form" : form
    }

    return render(request, "add-product.html", context=context)


def add_product_form(request):
    form = ProductForm(request.POST)

    if form.is_valid():
        print("#############################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        form.save()

        response_data = {
            "status" : "success",
            "title" : "Successfully Added",
            "message" : "You added a new product"
        }

    else:
        response_data = {
            "status" : "error",
            "title" : "An error Occured",
            "message" : "You can not add the product due to some Error"
        }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")

