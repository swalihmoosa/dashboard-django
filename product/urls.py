from django.urls import path
from product.views import category, add_new_product, add_product_form, productitem


app_name = "product"


urlpatterns = [
    path('', productitem, name="ProductItem" ),
    path('category', category, name="category" ),
    path('add_new_product', add_new_product, name="add_new_product"),
    path('add_product_form', add_product_form, name="add_product_form")
]