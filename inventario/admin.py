from django.contrib import admin
from .models import CategoriaProducto, Producto, MovimientoInventario, EquipoRenta


@admin.register(CategoriaProducto)
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo', 'activo']
    list_filter = ['tipo', 'activo']
    search_fields = ['nombre', 'descripcion']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'categoria', 'tipo_inventario', 'precio_venta', 'stock_actual', 'activo']
    list_filter = ['categoria', 'tipo_inventario', 'activo', 'permite_venta', 'permite_renta']
    search_fields = ['codigo', 'nombre', 'descripcion']
    readonly_fields = ['fecha_registro', 'fecha_actualizacion']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('codigo', 'nombre', 'descripcion', 'categoria')
        }),
        ('Tipo de Inventario', {
            'fields': ('tipo_inventario', 'unidad_medida')
        }),
        ('Precios', {
            'fields': ('precio_compra', 'precio_venta', 'precio_renta_dia', 'itbis')
        }),
        ('Inventario', {
            'fields': ('stock_actual', 'stock_minimo', 'stock_maximo')
        }),
        ('Proveedor', {
            'fields': ('proveedor_nombre', 'proveedor_contacto'),
            'classes': ('collapse',),
        }),
        ('Control', {
            'fields': ('permite_venta', 'permite_renta', 'activo', 'fecha_registro', 'fecha_actualizacion')
        }),
    )


@admin.register(MovimientoInventario)
class MovimientoInventarioAdmin(admin.ModelAdmin):
    list_display = ['producto', 'tipo_movimiento', 'cantidad', 'stock_anterior', 'stock_nuevo', 'fecha', 'usuario']
    list_filter = ['tipo_movimiento', 'fecha']
    search_fields = ['producto__nombre', 'motivo', 'usuario']
    readonly_fields = ['fecha']


@admin.register(EquipoRenta)
class EquipoRentaAdmin(admin.ModelAdmin):
    list_display = ['numero_serie', 'producto', 'estado', 'ubicacion', 'proxima_fecha_mantenimiento']
    list_filter = ['estado', 'ubicacion']
    search_fields = ['numero_serie', 'producto__nombre']
