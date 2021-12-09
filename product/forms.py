from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from django.forms.widgets import Select, TextInput, Textarea

from product.models import Category, ProductItem



class ProductForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = ProductItem
        fields = "__all__"
        widgets = {
            "product_name" : TextInput(attrs={
                "class" : "form-control validate col-xl-9 col-lg-8 col-md-8 col-sm-7"
            }),
            "product_description" : Textarea(attrs={
                "class" : "form-control validate col-xl-9 col-lg-8 col-md-8 col-sm-7",
                "rows" : 4
            }),
            "units_sold" : TextInput(attrs={
                "class" : "form-control validate col-xl-9 col-lg-8 col-md-8 col-sm-7"
            }),
            "in_stock" : TextInput(attrs={
                "class" : "form-control validate col-xl-9 col-lg-8 col-md-7 col-sm-7"
            }),
            "expire_date" : TextInput(attrs={
                "class" : "form-control validate col-xl-9 col-lg-8 col-md-8 col-sm-7"
            }),
            "category" : Select()
        }
