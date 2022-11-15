from django.urls import path
from Apps.productos.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]