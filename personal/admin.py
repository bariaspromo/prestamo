from django.contrib import admin
from .models import (
    Empleado, AsignacionServicio, AsignacionContrato, 
    DisponibilidadEmpleado, RendimientoEmpleado
)


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['codigo_empleado', 'nombre_completo', 'tipo_empleado', 'puesto', 'estado', 'fecha_ingreso']
    list_filter = ['tipo_empleado', 'estado', 'departamento']
    search_fields = ['codigo_empleado', 'nombres', 'apellidos', 'cedula', 'email']
    readonly_fields = ['fecha_creacion']
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('codigo_empleado', 'nombres', 'apellidos', 'cedula', 'fecha_nacimiento', 'foto')
        }),
        ('Contacto', {
            'fields': ('telefono', 'email', 'direccion')
        }),
        ('Datos Laborales', {
            'fields': ('tipo_empleado', 'puesto', 'departamento', 'salario', 'fecha_ingreso', 'fecha_salida', 'estado')
        }),
        ('Especialidades', {
            'fields': ('especialidades', 'certificaciones'),
            'classes': ('collapse',)
        }),
        ('Disponibilidad', {
            'fields': ('horario_trabajo', 'disponible_emergencias'),
            'classes': ('collapse',)
        }),
        ('Notas', {
            'fields': ('notas', 'fecha_creacion'),
            'classes': ('collapse',)
        }),
    )


@admin.register(AsignacionServicio)
class AsignacionServicioAdmin(admin.ModelAdmin):
    list_display = ['empleado', 'orden_servicio', 'estado', 'fecha_asignacion', 'horas_reales']
    list_filter = ['estado', 'fecha_asignacion']
    search_fields = ['empleado__nombres', 'empleado__apellidos', 'orden_servicio__numero_orden']
    readonly_fields = ['fecha_asignacion']


@admin.register(AsignacionContrato)
class AsignacionContratoAdmin(admin.ModelAdmin):
    list_display = ['empleado', 'contrato', 'rol', 'fecha_inicio', 'es_responsable_principal', 'activo']
    list_filter = ['es_responsable_principal', 'activo']
    search_fields = ['empleado__nombres', 'empleado__apellidos', 'contrato__numero_contrato']


@admin.register(DisponibilidadEmpleado)
class DisponibilidadEmpleadoAdmin(admin.ModelAdmin):
    list_display = ['empleado', 'tipo_evento', 'fecha_inicio', 'fecha_fin', 'aprobado']
    list_filter = ['tipo_evento', 'aprobado']
    search_fields = ['empleado__nombres', 'empleado__apellidos', 'motivo']
    readonly_fields = ['fecha_solicitud']


@admin.register(RendimientoEmpleado)
class RendimientoEmpleadoAdmin(admin.ModelAdmin):
    list_display = ['empleado', 'periodo', 'servicios_completados', 'calificacion_promedio', 'horas_trabajadas']
    list_filter = ['periodo']
    search_fields = ['empleado__nombres', 'empleado__apellidos']
    readonly_fields = ['fecha_generacion']
