from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ListForm

# Create your views here.

def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context)  


def product(request):
    Products = Product.objects.all()
    context = {'Products': Products}
    return render(request, 'product.html', context)

  


def addproduct(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            Products = Product.objects.all()
            context = {'Products': Products}
            return render(request, "addproduct.html", context)
    else:
        Products = Product.objects.all()
        return render(request, "addproduct.html")


def delete(request, product_id):
    products = Product.objects.get(pk=product_id)
    products.delete()
    return redirect("product")
