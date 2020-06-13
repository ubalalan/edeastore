from django.shortcuts import render
from .models import  Order
# Create your views here.

def order(request):
    context = {}
    return render(request, 'customer.html', context)
