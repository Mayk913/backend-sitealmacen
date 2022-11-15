from django.db import models

# Create your models here.



class Producto(models.Model):
    codigoProducto = models.CharField(max_length=100,  help_text="Ingrese el Codigo del Producto")
    descripcion = models.CharField(max_length=500, verbose_name="descripcion del producto")
    precio = models.FloatField(verbose_name="Precio")
    numeroEsxistencias = models.IntegerField(verbose_name="numero de existencias")
    

    def __str__(self):
        return self.codigoProducto

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = " productos"


# class Distribuir(models.Model):
#     cantidad = models.IntegerField(verbose_name="Cantidad")
#     codigoproducto= models.ForeignKey(Producto,null=True, blank=True, on_delete=models.CASCADE)
