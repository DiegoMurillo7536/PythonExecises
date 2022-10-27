from tabnanny import verbose
from django.db import models

#crear modelo 
class Categoria (models.Model):
    name = models.CharField (max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255)

    def __str__(self) :
        return self.name

    class Meta:
        verbose_name = 'Categoría'
        verbose_name = 'Categorías'
        db_table = 'Categoría'

class Marca (models.Model):
    name = models.CharField (max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255)

    def __str__(self) :
        return self.name

    class Meta:
        verbose_name = 'Marca'
        verbose_name = 'Marcas'
        db_table = 'Marca'
        

class Product(models.Model):
    name = models.CharField (max_length=100, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    price = models.PositiveIntegerField(verbose_name='Precio')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categpría')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name='Marca')

    def __str__(self) :
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name = 'Productos'
        db_table = 'Producto'
        ordering = ['id']