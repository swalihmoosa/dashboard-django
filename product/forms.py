from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets

from product.models import Category, Product



class ProductForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "product_name" : widgets.TextInput(attrs={
                "class" : "form-control validate col-xl-9 col-lg-8 col-md-8 col-sm-7"
            }),
            "product_description" : widgets.Textarea(attrs={
                "class" : "form-control validate col-xl-9 col-lg-8 col-md-8 col-sm-7"
            }),
            "units_sold" : widgets.TextInput(attrs={
                "class" : "form-control validate col-xl-9 col-lg-8 col-md-8 col-sm-7"
            }),
            "in_stock" : widgets.TextInput(attrs={
                "class" : "form-control validate col-xl-9 col-lg-8 col-md-7 col-sm-7"
            }),
            "expire_date" : widgets.DateInput(attrs={
                "class" : "form-control validate col-xl-9 col-lg-8 col-md-8 col-sm-7"
            }),
            "category" : widgets.Select()
        }
