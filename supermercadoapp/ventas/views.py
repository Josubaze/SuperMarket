from django.shortcuts import render, redirect
from .models import Cliente, Producto
from .forms import AddClientForm, EditClientForm, AddProductForm
from django.contrib import messages


def ventas_view(request):
    context = {}
    return render(request, "ventas.html",context)

def clientes_view(request):
    clientes = Cliente.objects.all()
    form_personal = AddClientForm()
    form_editar = EditClientForm()
    context = {
        "clientes":clientes,
        "form_personal" : form_personal,
        "form_editar" : form_editar
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
    if request.POST:
            cliente = Cliente.objects.get(pk = request.POST.get("id_personal_editar"))
            form = EditClientForm(request.POST, instance = cliente)
            if form.is_valid:
                try:
                    form.save()
                except:
                    messages(request, "Error al guardar cliente")
                    return redirect('Clientes')
    return redirect('Clientes')

def delete_client_view(request):
    if request.POST:
        #print(request.POST.get("id_personal_eliminar"))
        cliente = Cliente.objects.get(pk = request.POST.get("id_personal_eliminar"))
        cliente.delete()
    return redirect('Clientes')



def productos_view(request):

    productos = Producto.objects.all()
    form_product = AddProductForm()

    context = {
        "productos" : productos,
        "form_product" : form_product
    }
    return render(request, "productos.html",context)

def add_product_view(request):
    if request.POST:
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, "Error al guardar Producto")
                return redirect('Productos')
    return redirect('Productos')