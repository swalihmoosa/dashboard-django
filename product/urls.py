from django.urls import path
from product.views import product, category, add_new_product, add_product_form


app_name = "product"


urlpatterns = [
    path('', product, name="product" ),
    path('category', category, name="category" ),
    path('add_new_product', add_new_product, name="add_new_product"),
    path('add_product_form', add_product_form, name="add_product_form")
]