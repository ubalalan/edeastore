from django.urls import path
from . import views

urlpatterns = [

    path('', views.accounting, name="accounting"),

]