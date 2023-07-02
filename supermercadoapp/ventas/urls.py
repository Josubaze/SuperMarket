from django.urls import path
from . import views

urlpatterns = [
    path("", views.ventas_view, name="Ventas"),
    path("clientes/", views.clientes_view, name="Clientes"),

    path("add_client/", views.add_client_view, name="AddCliente"),
    path("edit_client/", views.edit_client_view, name="EditCliente"),
    path("delete_client/", views.delete_client_view, name="DeleteCliente"),

    path("products/", views.productos_view, name="Productos"),

    path("add_product/", views.add_product_view, name="AddProducto"),
    path("edit_product/", views.edit_product_view, name="EditProducto"),
    path("delete_product/", views.delete_product_view, name="DeleteProducto"),

    path('add_ventas/',views.add_venta.as_view(), name='AddVenta'),
    path('export/', views.export_pdf_view, name="ExportPDF" ),
    path('export/<id>/<iva>', views.export_pdf_view, name="ExportPDF" ),

    path('empresa/', views.empresa_view, name='Empresa'),

]