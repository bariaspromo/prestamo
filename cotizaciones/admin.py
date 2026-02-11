from django.contrib import admin
from .models import Cotizacion, ItemCotizacion, SeguimientoCotizacion, AprobacionCotizacion


class ItemCotizacionInline(admin.TabularInline):
    model = ItemCotizacion
    extra = 1
    readonly_fields = ['subtotal', 'itbis_monto', 'total']


class SeguimientoCotizacionInline(admin.TabularInline):
    model = SeguimientoCotizacion
    extra = 0
    readonly_fields = ['fecha']


@admin.register(Cotizacion)
class CotizacionAdmin(admin.ModelAdmin):
    list_display = ['numero_cotizacion', 'cliente', 'titulo', 'fecha_emision', 'total', 'estado']
    list_filter = ['estado', 'fecha_emision', 'vigencia_dias']
    search_fields = ['numero_cotizacion', 'titulo', 'cliente__nombres', 'cliente__razon_social']
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion', 'subtotal', 'itbis', 'total', 'fecha_vencimiento']
    inlines = [ItemCotizacionInline, SeguimientoCotizacionInline]
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('numero_cotizacion', 'cliente', 'titulo', 'descripcion', 'estado')
        }),
        ('Fechas', {
            'fields': ('fecha_emision', 'vigencia_dias', 'fecha_vencimiento', 'fecha_respuesta_cliente')
        }),
        ('Montos', {
            'fields': ('subtotal', 'descuento', 'itbis', 'total'),
            'classes': ('collapse',)
        }),
        ('Términos', {
            'fields': ('terminos_condiciones', 'forma_pago', 'tiempo_entrega', 'notas'),
            'classes': ('collapse',)
        }),
        ('Respuesta Cliente', {
            'fields': ('motivo_rechazo',),
            'classes': ('collapse',)
        }),
        ('Conversión', {
            'fields': ('factura_generada',),
            'classes': ('collapse',)
        }),
        ('Metadatos', {
            'fields': ('creado_por', 'fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['calcular_totales_cotizaciones']
    
    def calcular_totales_cotizaciones(self, request, queryset):
        for cotizacion in queryset:
            cotizacion.calcular_totales()
        self.message_user(request, f'Totales calculados para {queryset.count()} cotizaciones.')
    calcular_totales_cotizaciones.short_description = 'Calcular totales'


@admin.register(ItemCotizacion)
class ItemCotizacionAdmin(admin.ModelAdmin):
    list_display = ['cotizacion', 'descripcion', 'cantidad', 'precio_unitario', 'total', 'orden']
    search_fields = ['descripcion', 'cotizacion__numero_cotizacion']
    readonly_fields = ['subtotal', 'descuento_monto', 'itbis_monto', 'total']


@admin.register(SeguimientoCotizacion)
class SeguimientoCotizacionAdmin(admin.ModelAdmin):
    list_display = ['cotizacion', 'tipo', 'fecha', 'contacto', 'realizado_por']
    list_filter = ['tipo', 'fecha']
    search_fields = ['cotizacion__numero_cotizacion', 'descripcion', 'contacto']
    readonly_fields = ['fecha']


@admin.register(AprobacionCotizacion)
class AprobacionCotizacionAdmin(admin.ModelAdmin):
    list_display = ['cotizacion', 'nivel', 'aprobador', 'estado', 'fecha_solicitud', 'fecha_respuesta']
    list_filter = ['estado', 'nivel']
    search_fields = ['cotizacion__numero_cotizacion', 'aprobador']
    readonly_fields = ['fecha_solicitud', 'fecha_respuesta']
