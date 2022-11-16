from django.urls import path
from Apps.proveedores.views import ProveedoresView


app_name = "proveedores"
urlpatterns = [
    path('',  ProveedoresView.as_view()),
]
