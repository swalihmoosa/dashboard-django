import json
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import View

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


def edit_product(request, pk):  
    product = ProductItem.objects.get(pk=pk)
    form = ProductForm(instance = product)

    context = {
        "product" : product,
        "form" : form
    }

    return render(request,'edit-product.html',context=context)


def update(request, pk):
    product = ProductItem.objects.get(pk=pk)
    form = ProductForm(request.POST, request.FILES, instance = product)  

    if form.is_valid():  
        form.save()  
        return redirect("/product")

    return render(request, 'edit-product.html', {'product':product})


def delete_product(request, pk):
    product = ProductItem.objects.filter(pk=pk)
    product.delete()

    return redirect("/product")


def delete_category(request, pk):
    category = Category.objects.filter(pk=pk)
    category.delete()

    return redirect("/product")


class Product_view(View):
    def get(self,request):
        products=ProductItem.objects.all()
        context ={
            "products":products,
        }
        return  render(request,"product.html", context=context)

    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            product_ids=request.POST.getlist('id[]')
            for id in product_ids:
                product = ProductItem.objects.get(pk=id)
                product.delete()
            return redirect("product:productitem")
