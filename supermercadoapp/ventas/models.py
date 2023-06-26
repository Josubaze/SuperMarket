from django.db import models


class Cliente(models.Model):
    cedula = models.CharField(max_length=200, unique = True, null = True, blank = False)
    name = models.CharField(max_length=200, null = True, blank = False)
    phone = models.CharField(max_length=200, null = True, blank = False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

    def __str__(self):
        return self.name
    
class Producto(models.Model):
    code = models.CharField(max_length=200, unique = True, null = True, blank = False)
    description = models.CharField(max_length=255, unique = True, null = False)
    imagen = models.ImageField(upload_to="productos", null = False, blank = True)
    price = models.DecimalField(max_digits=15, decimal_places=2, null = True, default = 0)
    base = models.DecimalField(max_digits=15, decimal_places=2, null = True, default = 0)
    amount = models.DecimalField(max_digits=15, decimal_places=2, null = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        order_with_respect_to = "description"

    def __str__(self):
        return self.description
