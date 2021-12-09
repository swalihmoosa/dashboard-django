import json
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

from product.models import Category, Product
from product.forms import ProductForm


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


def add_new_product(request):
    form = ProductForm()

    context = {
        "form" : form
    }

    return render(request, "add-product.html", context=context)


def add_product_form(request):
    form = ProductForm(request.POST)

    if form.is_valid():
        if not Product.objects.filter(product_name=request.POST.get('product_name').exists()):
            form.save()

            response_data = {
                "status" : "success",
                "title" : "Successfully Added",
                "message" : "You added a new product"
            }
        else:
            response_data = {
                "status" : "error",
                "title" : "Already Added",
                "message" : "You are already added this product"
            }

    else:
        response_data = {
            "status" : "error",
            "title" : "An error Occured",
            "message" : "You can not add the product due to some Error"
        }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")

