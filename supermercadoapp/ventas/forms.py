from django import forms
from ventas.models import Cliente, Producto

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
        fields = ('code','description', 'base', 'price','amount', 'imagen')
        labels = {
            "code": "Código",
            "description": "Descripción",
            "base": "Base",
            "price": "Precio",
            "amount": "Cantidad",
            "imagen": "Imagen"
        }