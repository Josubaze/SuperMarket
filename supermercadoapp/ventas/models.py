from django.db import models
from django.forms import model_to_dict
from django_resized import ResizedImageField
from datetime import date
TODAY = date.today()

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

class Proveedor(models.Model):
    codigo = models.CharField(max_length=255, null=True, blank = True)
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    imagen = models.ImageField(upload_to='proveedor', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='proveedor'
        verbose_name_plural = 'proveedores'
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    code = models.CharField(max_length=200, unique = True, null = True, blank = False)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL , null=True , related_name='proveedorr')
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

class Egreso(models.Model):
    fecha_pedido = models.DateField(max_length=255)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL , null=True , related_name='clientee')
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    pagado = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    comentarios = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    ticket = models.BooleanField(default=True)
    #desglosar = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=True , null=True)

    class Meta:
        verbose_name='egreso'
        verbose_name_plural = 'egresos'
        order_with_respect_to = 'fecha_pedido'
    
    def __str__(self):
        return str(self.id)
   

class ProductosEgreso(models.Model):
    egreso = models.ForeignKey(Egreso, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=20, decimal_places=2 , null=False)
    precio = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    subtotal = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    iva = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    created = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=True)
    devolucion = models.BooleanField(default=False)

    class Meta:
        verbose_name='producto egreso'
        verbose_name_plural = 'productos egreso'
        order_with_respect_to = 'created'
    
    def __str__(self):
        return self.producto
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['created'])
        return item

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255, null=True)
    telefono = models.CharField(max_length=255, null=True)
    imagen = ResizedImageField(size=[100, 100], upload_to='empresa', blank=True, null=True)
    moneda = models.CharField(max_length=255, null=False, blank=False, default="$" )
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='empresa'
        verbose_name_plural = 'empresa'
    
    def __str__(self):
        return self.nombre

class Iva (models.Model):
    monto = models.DecimalField(max_digits=15, decimal_places=2, null=False)

    class Meta:
        verbose_name='iva'
        verbose_name_plural = 'iva'
    
    def __str__(self):
        return str(self.monto)

class MetodoPago(models.Model):
    egreso = models.ForeignKey(Egreso, on_delete=models.CASCADE)
    efectivo = models.DecimalField(max_digits=20, decimal_places=2 , default=0)
    tarjeta = models.DecimalField(max_digits=20, decimal_places=2 , default=0)
    transferencia = models.DecimalField(max_digits=20, decimal_places=2 , default=0)
    vales = models.DecimalField(max_digits=20, decimal_places=2 , default=0)
    otro = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    class Meta:
        verbose_name='metodo pago'
        verbose_name_plural = 'metodos pago'
    
    def __str__(self):
        return str(self.id)

class PagosEgreso(models.Model):
    egreso = models.ForeignKey(Egreso, on_delete=models.CASCADE)
    fecha = models.DateField(max_length=255)
    monto = models.DecimalField(max_digits=20, decimal_places=2 , null=False)
    comentarios = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='pagos egreso'
        verbose_name_plural = 'pagos egreso'
        order_with_respect_to = 'created'
    
    def __str__(self):
        return self.monto
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['created'])
        return item