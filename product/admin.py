from django.contrib import admin
from product.models import Category, ProductItem


class ProductItemAdmin(admin.ModelAdmin):
    list_display = ["product_name", "units_sold", "in_stock", "expire_date"]

admin.site.register(ProductItem, ProductItemAdmin)


admin.site.register(Category)
