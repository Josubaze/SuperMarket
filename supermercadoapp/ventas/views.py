from django.shortcuts import render, redirect
from .models import Cliente, Producto, Egreso, ProductosEgreso, Empresa, Proveedor
from .forms import AddClientForm, EditClientForm, AddProductForm, EditProductForm, ProveedorForm, EditarProveedorForm, EmpresaForm
from django.contrib import messages
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse
from weasyprint.text.fonts import FontConfiguration
from django.template.loader import get_template
from weasyprint import HTML, CSS
from django.conf import settings
from datetime import date, datetime
HOY = datetime.today().strftime('%Y-%m-%d')
import os


def egresos_view(request):
    egresos = Egreso.objects.all()
    empresa = Empresa.objects.get(pk=1)
    moneda = empresa.moneda

    context = {
        'egresos': egresos,
        'moneda': moneda
    }

    return render(request, 'egresos.html', context)

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
        if form.is_valid():
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
            if form.is_valid():
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
    form_agregar = AddProductForm()
    form_editar = EditProductForm()

    context = {
        "productos" : productos,
        "form_agregar" : form_agregar,
        "form_editar" : form_editar,
    }
    return render(request, "productos.html",context)

def add_product_view(request):
    if request.POST:
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request, "Error al guardar Producto")
                return redirect('Productos')
    return redirect('Productos')

def edit_product_view(request):
    if request.POST:
            producto = Producto.objects.get(pk = request.POST.get("id_producto_editar"))
            form = EditProductForm(request.POST, request.FILES, instance = producto)
            if form.is_valid():
                try:
                    form.save()
                except:
                    messages(request, "Error al guardar Producto")
                    return redirect('Productos')
    return redirect('Productos')

def delete_product_view(request):
    if request.POST:
        producto = Producto.objects.get(pk = request.POST.get("id_producto_eliminar"))
        producto.delete()
    return redirect('Productos')

class Venta(ListView):
    template_name = 'add_ventas.html'
    model = Egreso

    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    """
    def get_queryset(self):
        return ProductosPreventivo.objects.filter(
            preventivo=self.kwargs['id']
        )
    """
    def post(self, request,*ars, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'autocomplete':
                data = []
                for i in Producto.objects.filter(descripcion__icontains=request.POST["term"])[0:10]:
                    item = i.toJSON()
                    item['value'] = i.descripcion
                    data.append(item)
            else:
                data['error'] = "Ha ocurrido un error"
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data,safe=False)

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context["productos_lista"] = Producto.objects.all()
        context["HOY"] = HOY
        context["clientes_lista"] = Cliente.objects.all()
        empresa = Empresa.objects.get(pk=1)
        moneda = empresa.moneda
        context["moneda"] = moneda
        try:
            context["last_id"] = int(Egreso.objects.latest('id').id) + 1
        except Exception as e:
            context["last_id"] = 1
        return context
    

def export_pdf_view(request, id, iva):
    #print(id)
    template = get_template("ticket.html")
    #print(id)
    subtotal = 0 
    iva_suma = 0 

    venta = Egreso.objects.get(pk=float(id))
    datos = ProductosEgreso.objects.filter(egreso=venta)
    for i in datos:
        subtotal = subtotal + float(i.subtotal)
        iva_suma = iva_suma + float(i.iva)

    empresa = "Mi empresa S.A. De C.V"
    context ={
        'num_ticket': id,
        'iva': iva,
        'fecha': venta.fecha_pedido,
        'cliente': venta.cliente.nombre,
        'items': datos, 
        'total': venta.total, 
        'empresa': empresa,
        'comentarios': venta.comentarios,
        'subtotal': subtotal,
        'iva_suma': iva_suma,
    }
    html_template = template.render(context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; ticket.pdf"
    css_url = os.path.join(settings.BASE_DIR,'index\static\index\css/bootstrap.min.css')
    #HTML(string=html_template).write_pdf(target="ticket.pdf", stylesheets=[CSS(css_url)])
   
    font_config = FontConfiguration()
    HTML(string=html_template, base_url=request.build_absolute_uri()).write_pdf(target=response, font_config=font_config,stylesheets=[CSS(css_url)])

    return response

def empresa_view(request):
    
    empresa = Empresa.objects.get(pk=1)
    form_empresa = EmpresaForm(instance=empresa)

    if request.POST:
        empresa = Empresa.objects.get(pk=1)
        form_empresa = EmpresaForm(
            request.POST, request.FILES, instance=empresa)
        if form_empresa.is_valid():
            form_empresa.save()
            form_empresa = EmpresaForm(instance=empresa)
            messages.info(request,"Cambios efectuados con éxito")
    context = {
        'form_empresa': form_empresa,
        'empresa': empresa
    }

    return render(request, 'empresa.html', context)

def proveedor_view(request):
    
    form_personal = ProveedorForm()
    form_editar_personal = EditarProveedorForm()
    personal = Proveedor.objects.all()
    num_personal = len(personal)

    context = {
        'form_personal': form_personal,
        'form_editar_personal': form_editar_personal,
        'personal': personal,
        'num_personal': num_personal
    }
    return render(request, 'proveedores.html', context)


def add_proveedor_view(request):
    if request.POST:
        #print(request.POST)
        form = ProveedorForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages.warning(request,"Proveedor ya agregado o datos incorrectos")
                return redirect('Proveedor')


    return redirect('Proveedor')


def edit_proveedor_view(request):
    if request.POST:
        producto = Proveedor.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditarProveedorForm(
            request.POST, request.FILES, instance=producto)
        if form.is_valid:
            form.save()

    return redirect('Proveedor')


def delete_proveedor_view(request):
    if request.POST:
        if int(request.POST.get('id_personal_eliminar')) == 1:
            messages.warning(request, "No es posible eliminar este proveedor")
            return redirect('Proveedor')
        personal = Proveedor.objects.get(pk=request.POST.get('id_personal_eliminar'))
        personal.delete()
        
    return redirect('Proveedor')

def save_venta_view(request):
    if request.POST:
        data =[]
        try:
            action = request.POST['action']
            if action == "save":
                datos = json.loads(request.POST["verts"])
                id_cliente = request.POST["id_cliente"]
                comentarios = request.POST["comentarios"]
                cliente = Cliente.objects.get(pk=id_cliente)
                total = float(datos["total"])
                fecha = request.POST["fecha"]
                ticket_num = float( request.POST["ticket"])
                efectivo = float( request.POST["efectivo"])
                tarjeta = float( request.POST["tarjeta"])
                transferencia = float( request.POST["transferencia"])
                vales = float( request.POST["vales"])
                otro = float( request.POST["otro"])
                pagado = efectivo + tarjeta + transferencia + vales + otro
                #desglosar_num = float( request.POST["desglosar"])

                if ticket_num == 1:
                    ticket =True
                elif ticket_num == 0:
                    ticket = False
                '''
                if desglosar_num == 1:
                    desglosar =True
                elif desglosar_num == 0:
                    desglosar = False
                '''

                venta = Egreso(cliente=cliente, fecha_pedido=fecha, total=total, pagado=pagado, comentarios=comentarios, ticket=ticket)
                venta.save()

                metodo = MetodoPago(egreso=venta,efectivo=efectivo, tarjeta=tarjeta, transferencia=transferencia, vales=vales, otro=otro)
                metodo.save()

                data.append(venta.id)
                data.append(venta.ticket)
                '''
                #data.append(venta.desglosar)
                
                for i in datos["products"]:
                    pr_save = Producto.objects.get(pk=float(i["id"]))

                    if pr_save.servicio == False:
                        porcion_convertida = float(i["cantidad"]) * (1/float(pr_save.porcion))
                        suma = float(pr_save.cantidad) - porcion_convertida
                        pr_save.cantidad = suma
                        pr_save.save()

                   
                    iva_producto = float(pr_save.iva)

                    if iva_producto != 0:
                        subtotal = float(i["subtotal"]) / (1+iva_producto)
                        iva = subtotal * iva_producto
                    else:
                        subtotal = float(i["subtotal"])
                        iva = 0

                    product = ProductosEgreso(egreso=venta, producto=pr_save,cantidad=float(i["cantidad"]),precio=float(i["precio"]),subtotal=subtotal,iva=iva,total=float(i["subtotal"]))
                    product.save()
                    print(i["subtotal"])
                '''
                messages.info(request,"Venta agregada con éxito")
        except Exception as e:
            data['error'] = str(e)

    return JsonResponse(data,safe=False)