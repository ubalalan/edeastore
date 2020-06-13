from django import forms
from .models import Product


class ListForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "description", "finished", "date"]
