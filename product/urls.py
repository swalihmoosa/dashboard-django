from django.urls import path
from product.views import product, category, add_new_product


app_name = "product"


urlpatterns = [
    path('', product, name="product" ),
    path('category', category, name="category" ),
    path('add_new_product', add_new_product, name="add_new_product")
]