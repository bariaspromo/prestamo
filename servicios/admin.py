from django.contrib import admin
from .models import (
    ContratoServicio, SLA, OrdenServicio, CronogramaServicio, ContratoRenta
)


class SLAInline(admin.TabularInline):
    model = SLA
    extra = 1


@admin.register(ContratoServicio)
class ContratoServicioAdmin(admin.ModelAdmin):
    list_display = ['numero_contrato', 'cliente', 'tipo_contrato', 'estado', 'fecha_inicio', 'fecha_fin', 'valor_mensual']
    list_filter = ['tipo_contrato', 'estado', 'frecuencia_pago']
    search_fields = ['numero_contrato', 'cliente__nombres', 'cliente__razon_social', 'descripcion']
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']
    inlines = [SLAInline]
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('numero_contrato', 'cliente', 'tipo_contrato', 'estado')
        }),
        ('Descripción', {
            'fields': ('descripcion', 'alcance')
        }),
        ('Fechas', {
            'fields': ('fecha_inicio', 'fecha_fin', 'fecha_firma')
        }),
        ('Valores', {
            'fields': ('valor_mensual', 'frecuencia_pago')
        }),
        ('Metadatos', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )


@admin.register(SLA)
class SLAAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'contrato', 'prioridad', 'tiempo_respuesta_horas', 'tiempo_resolucion_horas', 'activo']
    list_filter = ['prioridad', 'activo']
    search_fields = ['nombre', 'contrato__numero_contrato']


@admin.register(OrdenServicio)
class OrdenServicioAdmin(admin.ModelAdmin):
    list_display = ['numero_orden', 'cliente', 'tipo_servicio', 'prioridad', 'estado', 'fecha_programada', 'tecnico_asignado']
    list_filter = ['tipo_servicio', 'prioridad', 'estado', 'fecha_programada']
    search_fields = ['numero_orden', 'cliente__nombres', 'cliente__razon_social', 'descripcion']
    readonly_fields = ['fecha_solicitud']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('numero_orden', 'cliente', 'contrato', 'sla')
        }),
        ('Tipo de Servicio', {
            'fields': ('tipo_servicio', 'prioridad', 'estado')
        }),
        ('Descripción', {
            'fields': ('descripcion', 'direccion_servicio')
        }),
        ('Fechas', {
            'fields': ('fecha_solicitud', 'fecha_programada', 'fecha_respuesta', 'fecha_inicio', 'fecha_finalizacion')
        }),
        ('Asignación', {
            'fields': ('tecnico_asignado',)
        }),
        ('Resultados', {
            'fields': ('diagnostico', 'solucion', 'observaciones'),
            'classes': ('collapse',)
        }),
        ('Satisfacción del Cliente', {
            'fields': ('calificacion_cliente', 'comentarios_cliente'),
            'classes': ('collapse',)
        }),
    )


@admin.register(CronogramaServicio)
class CronogramaServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'contrato', 'frecuencia', 'proxima_ejecucion', 'activo']
    list_filter = ['frecuencia', 'activo']
    search_fields = ['nombre', 'contrato__numero_contrato']


@admin.register(ContratoRenta)
class ContratoRentaAdmin(admin.ModelAdmin):
    list_display = ['numero_contrato', 'cliente', 'tipo_renta', 'fecha_inicio', 'fecha_fin_estimada', 'costo_diario', 'estado']
    list_filter = ['tipo_renta', 'estado']
    search_fields = ['numero_contrato', 'cliente__nombres', 'cliente__razon_social']
    readonly_fields = ['fecha_creacion']
