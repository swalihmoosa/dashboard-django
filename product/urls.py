from django.urls import path
from product.views import product, category


app_name = "product"


urlpatterns = [
    path('', product, name="product" ),
    path('category', category, name="category" )
]