from django import forms
from ventas.models import Cliente, Producto, Empresa, ProductosEgreso, Egreso, Proveedor
from datetime import date

moneda = Empresa.objects.get(pk=1).moneda
TODAY = date.today()
class AddClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('cedula', 'name', 'phone')
        labels = {
            "cedula": "Cédula",
            "name": "Nombre",
            "phone": "Télefono",
        }

class EditClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('cedula', 'name', 'phone')
        labels = {
            "cedula": "Cédula",
            "name": "Nombre",
            "phone": "Télefono",
        }
        widgets = {
           'cedula' : forms.TextInput(attrs = {'type':'text', 'id':'cedula_editar'}),
           'name' : forms.TextInput(attrs = {'id':'nombre_editar'}),
           'phone' : forms.TextInput(attrs = { 'id':'telefono_editar'}),
        }


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('code','description', 'base', 'price','amount', 'proveedor', 'imagen')
        labels = {
            "code": "Código",
            "description": "Descripción",
            "base": "Base",
            "price": "Precio",
            "amount": "Cantidad",
            "proveedor": "Proveedor",
            "imagen": "Imagen"
        }

class EditProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('code','description', 'base', 'price','amount', 'proveedor', 'imagen')
        labels = {
            "code": "Código",
            "description": "Descripción",
            "base": "Base",
            "price": "Precio",
            "amount": "Cantidad",
            "proveedor": "Proveedor",
            "imagen": "Imagen"
        }
        widgets = {
            "code": forms.TextInput(attrs = {'type':'text', 'id':'codigo_editar'}),
            "description": forms.TextInput(attrs = {'id':'descripcion_editar'}),
            "base": forms.TextInput(attrs = {'id':'base_editar'}),
            "price": forms.TextInput(attrs = {'id':'precio_editar'}),
            "amount": forms.TextInput(attrs = {'id':'cantidad_editar'}),
            "proveedor": forms.TextInput(attrs = {'id':'proveedor_editar'}),

        }

class ProveedorForm(forms.ModelForm):
    class Meta:
        imagen = forms.ImageField()
        model = Proveedor
        fields = ('codigo','nombre', 'telefono', 'imagen')
        labels = {
            'codigo': 'Código: ',
            'telefono': 'Telefono: ',
            'imagen': 'Imagen: ',
            'nombre': 'Descripcion: '
        }

class EditarProveedorForm(forms.ModelForm):

    class Meta:
        imagen = forms.ImageField()
        model = Proveedor
        fields = ('codigo','nombre', 'telefono', 'imagen')
        labels = {
            'codigo': 'Código: ',
            'telefono': 'Telefono: ',
            'imagen': 'Imagen: ',
            'nombre': 'Descripcion: '
        }

        widgets = {
            'codigo': forms.TextInput(attrs={'type': 'text', 'id': 'codigo_editar'}),
            'nombre': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'telefono': forms.TextInput(attrs={'id': 'telefono_editar'}),
        }
'''
class PagosEgresoForm(forms.ModelForm):
    
    class Meta:
        model = PagosEgreso
        fields = ('fecha','monto','comentarios')
        labels = {
            'fecha': 'Fecha: ',
            'monto': f'Monto {moneda} : ',
            'comentarios': 'Comentarios: '
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date' , 'value': TODAY }),
        }
'''
class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('nombre','domicilio', 'telefono', 'imagen', 'moneda')
        labels = {
            'nombre': 'Nombre:',
            'telefono': 'Contacto: ',
            'domicilio': 'Domicilio: ', 
            'imagen': 'Imagen: ',
            'moneda': 'Moneda: '
        }