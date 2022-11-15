from django.db import models
from Apps.productos.models import Producto

# Create your models here.


class Proveedores(models.Model):
    codigoProveedores = models.CharField(max_length=100, help_text="Ingrese el Codigo del Proveedor")
    nombreProveedores = models.CharField(max_length=100, help_text="Ingrese el Nombre del Proveedor")
    apellidoProveedores = models.CharField(max_length=100, help_text="Ingrese el Apellido del Proveedor")
    direccionProveedores = models.CharField(max_length=100, help_text="Ingrese la Direccion del Proveedor")
    telefonoProveedores = models.CharField(max_length=12, help_text="Ingrese el Telefono del Proveedor")
    provinviaProveedores = models.CharField(max_length=100, help_text="Ingrese la Provinvia del Proveedor")
    

    def __str__(self):
        return self.nombreProveedores

    class Meta:
        verbose_name = "Proveedores"
        verbose_name_plural = "Proveedores"


#==============================================================#
class Distribuir(models.Model):
    # cantidad = models.IntegerField(verbose_name="Cantidad")
    codigoproducto= models.ForeignKey(Producto,  on_delete=models.CASCADE)
    codigoproveedores = models.ForeignKey(Proveedores,  on_delete=models.CASCADE)
    cantidad_productos = models.IntegerField( verbose_name="cantidad de productos")

    def __str__(self):
        return self.codigoproducto, self.codigoproveedores, self.cantidad_productos

    class Meta:
        verbose_name = "Distribucion"
        verbose_name_plural = "Distribuciones"