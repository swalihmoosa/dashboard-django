from django.urls import path
from product.views import category, add_new_product, add_product_form, productitem, edit_product, update, delete_product, delete_category, delete_multiple


app_name = "product"


urlpatterns = [
    path('', productitem, name="ProductItem" ),
    path('category', category, name="category" ),
    path('add_new_product', add_new_product, name="add_new_product"),
    path('add_product_form', add_product_form, name="add_product_form"),
    path('edit_product/<pk>', edit_product, name="edit_product"),
    path('update/<pk>', update, name="update"),
    path('delete_product/<pk>', delete_product, name="delete_product"),
    path('delete_category/<pk>', delete_category, name="delete_category"),
    path('delete_multiple', delete_multiple, name="delete_multiple")
]