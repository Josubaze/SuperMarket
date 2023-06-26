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
]