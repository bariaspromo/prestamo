from django.contrib import admin
from .models import SecuenciaNCF, Factura, ItemFactura, Pago, NotaCredito


class ItemFacturaInline(admin.TabularInline):
    model = ItemFactura
    extra = 1
    readonly_fields = ['subtotal', 'itbis_monto', 'total']


class PagoInline(admin.TabularInline):
    model = Pago
    extra = 0
    readonly_fields = ['fecha_registro']


@admin.register(SecuenciaNCF)
class SecuenciaNCFAdmin(admin.ModelAdmin):
    list_display = ['tipo_comprobante', 'serie', 'numero_actual', 'numero_desde', 'numero_hasta', 'fecha_vencimiento', 'activo']
    list_filter = ['tipo_comprobante', 'activo']


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ['numero_factura', 'ncf', 'cliente', 'tipo_ingreso', 'fecha_emision', 'total', 'estado']
    list_filter = ['tipo_ingreso', 'estado', 'fecha_emision']
    search_fields = ['numero_factura', 'ncf', 'cliente__nombres', 'cliente__razon_social']
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion', 'subtotal', 'itbis', 'total']
    inlines = [ItemFacturaInline, PagoInline]
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('numero_factura', 'ncf', 'tipo_ncf', 'cliente', 'tipo_ingreso', 'estado')
        }),
        ('Fechas', {
            'fields': ('fecha_emision', 'fecha_vencimiento')
        }),
        ('Montos', {
            'fields': ('subtotal', 'descuento', 'itbis', 'otros_impuestos', 'total', 'monto_pagado'),
            'classes': ('collapse',)
        }),
        ('Notas', {
            'fields': ('observaciones', 'terminos_condiciones'),
            'classes': ('collapse',)
        }),
        ('Metadatos', {
            'fields': ('creado_por', 'fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['calcular_totales_facturas']
    
    def calcular_totales_facturas(self, request, queryset):
        for factura in queryset:
            factura.calcular_totales()
        self.message_user(request, f'Totales calculados para {queryset.count()} facturas.')
    calcular_totales_facturas.short_description = 'Calcular totales'


@admin.register(ItemFactura)
class ItemFacturaAdmin(admin.ModelAdmin):
    list_display = ['factura', 'descripcion', 'cantidad', 'precio_unitario', 'total']
    search_fields = ['descripcion', 'factura__numero_factura']
    readonly_fields = ['subtotal', 'descuento_monto', 'itbis_monto', 'total']


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ['numero_recibo', 'factura', 'fecha_pago', 'monto', 'metodo_pago']
    list_filter = ['metodo_pago', 'fecha_pago']
    search_fields = ['numero_recibo', 'factura__numero_factura', 'referencia']
    readonly_fields = ['fecha_registro']


@admin.register(NotaCredito)
class NotaCreditoAdmin(admin.ModelAdmin):
    list_display = ['numero_nota', 'ncf', 'factura_original', 'motivo', 'monto', 'fecha_emision']
    list_filter = ['motivo', 'fecha_emision']
    search_fields = ['numero_nota', 'ncf', 'factura_original__numero_factura']
    readonly_fields = ['fecha_creacion']
