from django.shortcuts import render, redirect
from .models import Cliente, Producto
from .forms import AddClientForm
from django.contrib import messages

def ventas_view(request):
    context = {}
    return render(request, "ventas.html",context)

def clientes_view(request):
    clientes = Cliente.objects.all()
    form_personal = AddClientForm()
    context = {
        "clientes":clientes,
        "form_personal" : form_personal,
    }
    return render(request, "clientes.html",context)

def add_client_view(request):
    if request.POST:
        form = AddClientForm(request.POST)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, "Error al guardar cliente")
                return redirect('Clientes')
    return redirect('Clientes')

def edit_client_view(request):
    return redirect('Clientes')

def delete_client_view(request):
    if request.POST:
        #print(request.POST.get("id_personal_eliminar"))
        cliente = Cliente.objects.get(pk = request.POST.get("id_personal_eliminar"))
        cliente.delete()
    return redirect('Clientes')
#modificacion