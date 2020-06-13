from django.urls import path
from . import views

urlpatterns = [

    path('', views.product, name="product"),
    path('addproduct/', views.addproduct, name="addproduct"),
    path('delete/<product_id>/', views.delete, name="delete"),

]
