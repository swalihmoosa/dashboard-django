from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.forms.widgets import DateInput, Select, TextInput, Textarea

from product.models import Category, ProductItem



class ProductForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = ProductItem
        exclude = ('units_sold',)
        widgets = {
            "product_name" : TextInput(attrs={
                "class" : "form-control validate col-xl-9 col-lg-8 col-md-8 col-sm-7"
            }),
            "product_description" : Textarea(attrs={
                "class" : "form-control validate col-xl-9 col-lg-8 col-md-8 col-sm-7",
                "rows" : 4
            }),
            "in_stock" : TextInput(attrs={
                "class" : "form-control validate col-xl-9 col-lg-8 col-md-7 col-sm-7"
            }),
            "expire_date" : DateInput(attrs={
                "class" : "form-control validate col-xl-9 col-lg-8 col-md-8 col-sm-7",
                'type':'date'
            }),
            "category" : Select()
        }
