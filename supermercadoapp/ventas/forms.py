from django import forms
from ventas.models import Cliente

class AddClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('cedula', 'name', 'phone')
        labels = {
            "cedula": "Cédula",
            "name": "Nombre",
            "phone": "Télefono",
        }