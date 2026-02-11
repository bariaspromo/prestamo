from django.db import models
from servicios.models import ContratoServicio, OrdenServicio


class Empleado(models.Model):
    """Personal de la empresa"""
    TIPO_EMPLEADO = [
        ('TECNICO', 'Técnico'),
        ('VENDEDOR', 'Vendedor'),
        ('ADMINISTRATIVO', 'Administrativo'),
        ('GERENTE', 'Gerente'),
    ]
    
    ESTADO = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
        ('VACACIONES', 'De Vacaciones'),
        ('LICENCIA', 'En Licencia'),
    ]
    
    # Información personal
    codigo_empleado = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    
    # Contacto
    telefono = models.CharField(max_length=17)
    email = models.EmailField()
    direccion = models.TextField()
    
    # Datos laborales
    tipo_empleado = models.CharField(max_length=20, choices=TIPO_EMPLEADO)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO, default='ACTIVO')
    
    # Datos del cargo
    puesto = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Especialidades (para técnicos)
    especialidades = models.TextField(blank=True, help_text='Especialidades técnicas, separadas por comas')
    certificaciones = models.TextField(blank=True)
    
    # Disponibilidad
    horario_trabajo = models.CharField(max_length=200, default='8am-5pm Lun-Vie')
    disponible_emergencias = models.BooleanField(default=False)
    
    # Foto
    foto = models.ImageField(upload_to='fotos_empleados/', blank=True)
    
    # Metadatos
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    notas = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['apellidos', 'nombres']
    
    def __str__(self):
        return f"{self.codigo_empleado} - {self.nombres} {self.apellidos}"
    
    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"


class AsignacionServicio(models.Model):
    """Asignación de personal a servicios"""
    ESTADO_ASIGNACION = [
        ('ASIGNADA', 'Asignada'),
        ('EN_PROCESO', 'En Proceso'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
    ]
    
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    orden_servicio = models.ForeignKey(OrdenServicio, on_delete=models.CASCADE)
    
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    
    estado = models.CharField(max_length=20, choices=ESTADO_ASIGNACION, default='ASIGNADA')
    
    # Horas trabajadas
    horas_estimadas = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    horas_reales = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    
    observaciones = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Asignación de Servicio'
        verbose_name_plural = 'Asignaciones de Servicio'
    
    def __str__(self):
        return f"{self.empleado.nombre_completo()} - {self.orden_servicio.numero_orden}"


class AsignacionContrato(models.Model):
    """Asignación de personal a contratos de servicio"""
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    contrato = models.ForeignKey(ContratoServicio, on_delete=models.CASCADE)
    
    rol = models.CharField(max_length=100, help_text='Rol del empleado en este contrato')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    
    es_responsable_principal = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Asignación a Contrato'
        verbose_name_plural = 'Asignaciones a Contratos'
    
    def __str__(self):
        return f"{self.empleado.nombre_completo()} - {self.contrato.numero_contrato}"


class DisponibilidadEmpleado(models.Model):
    """Calendario de disponibilidad de empleados"""
    TIPO_EVENTO = [
        ('VACACIONES', 'Vacaciones'),
        ('LICENCIA', 'Licencia'),
        ('CAPACITACION', 'Capacitación'),
        ('AUSENCIA', 'Ausencia'),
    ]
    
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tipo_evento = models.CharField(max_length=20, choices=TIPO_EVENTO)
    
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    
    motivo = models.TextField()
    aprobado = models.BooleanField(default=False)
    aprobado_por = models.CharField(max_length=100, blank=True)
    
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Disponibilidad'
        verbose_name_plural = 'Disponibilidades'
    
    def __str__(self):
        return f"{self.empleado.nombre_completo()} - {self.tipo_evento}"


class RendimientoEmpleado(models.Model):
    """Métricas de rendimiento de empleados"""
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    periodo = models.DateField(help_text='Mes/Año del reporte')
    
    # Métricas de servicio
    servicios_asignados = models.IntegerField(default=0)
    servicios_completados = models.IntegerField(default=0)
    servicios_a_tiempo = models.IntegerField(default=0)
    
    # Calificación del cliente
    calificacion_promedio = models.DecimalField(max_digits=3, decimal_places=2, default=0,
                                                help_text='Calificación promedio 1-5')
    
    # Horas trabajadas
    horas_trabajadas = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    horas_extra = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    
    # Observaciones
    observaciones = models.TextField(blank=True)
    
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Rendimiento'
        verbose_name_plural = 'Rendimientos'
        unique_together = ['empleado', 'periodo']
    
    def __str__(self):
        return f"{self.empleado.nombre_completo()} - {self.periodo.strftime('%B %Y')}"
    
    def tasa_cumplimiento(self):
        if self.servicios_asignados > 0:
            return (self.servicios_completados / self.servicios_asignados) * 100
        return 0
