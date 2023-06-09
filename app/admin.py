from django.contrib import admin
from .models import Marca,producto,arrendar, Mecanico, OrdenReparacion, Usuario

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display= ["nombre", "precio", "nuevo","Marca"]
    list_editable= ["precio"]
    search_fields = ["nombre"]
    list_filter =["Marca","nuevo"]

admin.site.register(Marca)
admin.site.register(producto,ProductoAdmin)
admin.site.register(arrendar)
admin.site.register(Mecanico)
admin.site.register(OrdenReparacion)
admin.site.register(Usuario)