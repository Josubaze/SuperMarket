from django.contrib import admin
from ventas.models import Cliente, Producto

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'cedula')
    search_fields = ['name']
    readonly_fields = ('created', 'updated')
    filter_horizontal = () 
    list_filter = ()
    fieldsets = ()

admin.site.register(Cliente, ClientAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'cost')
    search_fields = ['description']
    readonly_fields = ('created', 'updated')
    filter_horizontal = () 
    list_filter = ()
    fieldsets = ()

admin.site.register(Producto, ProductAdmin)