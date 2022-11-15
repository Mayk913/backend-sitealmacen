from django.contrib import admin
from Apps.clientes.models import Cliente
from Apps.clientes.models import Comprar

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comprar)
admin.site.register(Cliente, ClienteAdmin)
