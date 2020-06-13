from django.shortcuts import render
from .models import Vendor
# Create your views here.


def vendor(request):
    context = {}
    return render(request, 'ship.html', context)
