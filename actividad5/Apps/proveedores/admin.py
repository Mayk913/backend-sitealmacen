from django.contrib import admin
from Apps.proveedores.models import Proveedores, Distribuir
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Distribuir)
admin.site.register(Proveedores, ClienteAdmin)