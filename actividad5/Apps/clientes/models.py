from django.db import models
from Apps.productos.models import Producto


# Create your models here.


class Cliente(models.Model):
    codigoC = models.CharField( max_length=100,  help_text="Ingrese el Codigo del Cliente")
    nombreCliente = models.CharField(max_length=100,  help_text="Ingrese el Nombre del Cliente")
    apellidoCliente = models.CharField(max_length=100, help_text="Ingrese el Apellido del Cliente")
    direccionCliente = models.CharField(max_length=100,  help_text="Ingrese la Direccion del Cliente")
    telefonoCliente = models.CharField(max_length=12, help_text="Ingrese el Telefono del Cliente")
    

    def __str__(self):
        return self.nombreCliente 

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"


class Comprar(models.Model):
    fechadecompra= models.CharField(max_length=100, verbose_name="fecha de compra")
    codigoproducto= models.ForeignKey(Producto, on_delete=models.CASCADE)
    codigoC= models.ForeignKey(Cliente,null=True,  on_delete=models.CASCADE)

    def __str__(self):
        return self.codigoproducto, self.fechadecompra, self.codigoC

    class Meta:
        verbose_name = "Comprar"
        verbose_name_plural = "Comprar"