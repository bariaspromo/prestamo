from django.db import models
from clientes.models import Cliente
from inventario.models import Producto, EquipoRenta
from django.utils import timezone


class ContratoServicio(models.Model):
    """Contratos de servicio (igualas)"""
    TIPO_CONTRATO = [
        ('IGUALA_EQUIPO', 'Iguala de Equipo'),
        ('IGUALA_SERVICIO', 'Iguala de Servicio'),
        ('MANTENIMIENTO', 'Mantenimiento Preventivo'),
        ('SOPORTE', 'Soporte Técnico'),
        ('RENTA', 'Renta de Equipo'),
    ]
    
    ESTADO_CONTRATO = [
        ('BORRADOR', 'Borrador'),
        ('ACTIVO', 'Activo'),
        ('SUSPENDIDO', 'Suspendido'),
        ('FINALIZADO', 'Finalizado'),
        ('CANCELADO', 'Cancelado'),
    ]
    
    FRECUENCIA_PAGO = [
        ('MENSUAL', 'Mensual'),
        ('TRIMESTRAL', 'Trimestral'),
        ('SEMESTRAL', 'Semestral'),
        ('ANUAL', 'Anual'),
    ]
    
    # Información básica
    numero_contrato = models.CharField(max_length=50, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    tipo_contrato = models.CharField(max_length=30, choices=TIPO_CONTRATO)
    
    # Descripción
    descripcion = models.TextField()
    alcance = models.TextField(help_text='Alcance de los servicios incluidos')
    
    # Fechas
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    fecha_firma = models.DateField(null=True, blank=True)
    
    # Valores
    valor_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    frecuencia_pago = models.CharField(max_length=20, choices=FRECUENCIA_PAGO, default='MENSUAL')
    
    # Estado
    estado = models.CharField(max_length=20, choices=ESTADO_CONTRATO, default='BORRADOR')
    
    # Metadatos
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Contrato de Servicio'
        verbose_name_plural = 'Contratos de Servicio'
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.numero_contrato} - {self.cliente.nombre_completo()}"
    
    def esta_activo(self):
        return self.estado == 'ACTIVO' and self.fecha_inicio <= timezone.now().date() <= self.fecha_fin


class SLA(models.Model):
    """Acuerdos de Nivel de Servicio"""
    PRIORIDAD = [
        ('CRITICA', 'Crítica'),
        ('ALTA', 'Alta'),
        ('MEDIA', 'Media'),
        ('BAJA', 'Baja'),
    ]
    
    contrato = models.ForeignKey(ContratoServicio, on_delete=models.CASCADE, related_name='slas')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    prioridad = models.CharField(max_length=20, choices=PRIORIDAD)
    
    # Tiempos de respuesta (en horas)
    tiempo_respuesta_horas = models.IntegerField(help_text='Tiempo máximo de respuesta en horas')
    tiempo_resolucion_horas = models.IntegerField(help_text='Tiempo máximo de resolución en horas')
    
    # Horarios
    horario_cobertura = models.CharField(max_length=100, default='24/7',
                                        help_text='Ej: 8am-6pm Lunes-Viernes, 24/7, etc.')
    
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'SLA'
        verbose_name_plural = 'SLAs'
    
    def __str__(self):
        return f"{self.nombre} - {self.contrato.numero_contrato}"


class OrdenServicio(models.Model):
    """Órdenes de servicio"""
    TIPO_SERVICIO = [
        ('PREVENTIVO', 'Mantenimiento Preventivo'),
        ('CORRECTIVO', 'Mantenimiento Correctivo'),
        ('INSTALACION', 'Instalación'),
        ('REPARACION', 'Reparación'),
        ('SOPORTE', 'Soporte Técnico'),
        ('OTRO', 'Otro'),
    ]
    
    ESTADO = [
        ('PENDIENTE', 'Pendiente'),
        ('ASIGNADA', 'Asignada'),
        ('EN_PROCESO', 'En Proceso'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
    ]
    
    PRIORIDAD = [
        ('CRITICA', 'Crítica'),
        ('ALTA', 'Alta'),
        ('MEDIA', 'Media'),
        ('BAJA', 'Baja'),
    ]
    
    # Información básica
    numero_orden = models.CharField(max_length=50, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    contrato = models.ForeignKey(ContratoServicio, on_delete=models.SET_NULL, null=True, blank=True)
    sla = models.ForeignKey(SLA, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Tipo de servicio
    tipo_servicio = models.CharField(max_length=30, choices=TIPO_SERVICIO)
    prioridad = models.CharField(max_length=20, choices=PRIORIDAD, default='MEDIA')
    
    # Descripción
    descripcion = models.TextField()
    direccion_servicio = models.TextField()
    
    # Fechas
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_programada = models.DateTimeField()
    fecha_respuesta = models.DateTimeField(null=True, blank=True)
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    fecha_finalizacion = models.DateTimeField(null=True, blank=True)
    
    # Asignación
    tecnico_asignado = models.CharField(max_length=200, blank=True)
    
    # Estado
    estado = models.CharField(max_length=20, choices=ESTADO, default='PENDIENTE')
    
    # Resultados
    diagnostico = models.TextField(blank=True)
    solucion = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    
    # Satisfacción
    calificacion_cliente = models.IntegerField(null=True, blank=True, 
                                              help_text='Calificación de 1 a 5')
    comentarios_cliente = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Orden de Servicio'
        verbose_name_plural = 'Órdenes de Servicio'
        ordering = ['-fecha_solicitud']
    
    def __str__(self):
        return f"{self.numero_orden} - {self.cliente.nombre_completo()}"
    
    def cumple_sla(self):
        """Verifica si cumple con el SLA"""
        if not self.sla:
            return None
        
        if self.fecha_respuesta and self.fecha_solicitud:
            tiempo_respuesta = (self.fecha_respuesta - self.fecha_solicitud).total_seconds() / 3600
            if tiempo_respuesta > self.sla.tiempo_respuesta_horas:
                return False
        
        if self.fecha_finalizacion and self.fecha_solicitud:
            tiempo_resolucion = (self.fecha_finalizacion - self.fecha_solicitud).total_seconds() / 3600
            if tiempo_resolucion > self.sla.tiempo_resolucion_horas:
                return False
        
        return True


class CronogramaServicio(models.Model):
    """Cronograma de servicios recurrentes"""
    FRECUENCIA = [
        ('DIARIA', 'Diaria'),
        ('SEMANAL', 'Semanal'),
        ('QUINCENAL', 'Quincenal'),
        ('MENSUAL', 'Mensual'),
        ('TRIMESTRAL', 'Trimestral'),
        ('SEMESTRAL', 'Semestral'),
        ('ANUAL', 'Anual'),
    ]
    
    contrato = models.ForeignKey(ContratoServicio, on_delete=models.CASCADE, related_name='cronogramas')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    frecuencia = models.CharField(max_length=20, choices=FRECUENCIA)
    
    # Fechas
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    proxima_ejecucion = models.DateField()
    
    # Asignación
    tecnico_predeterminado = models.CharField(max_length=200, blank=True)
    
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Cronograma de Servicio'
        verbose_name_plural = 'Cronogramas de Servicio'
    
    def __str__(self):
        return f"{self.nombre} - {self.frecuencia}"


class ContratoRenta(models.Model):
    """Contratos de renta de equipos o personal"""
    TIPO_RENTA = [
        ('EQUIPO', 'Renta de Equipo'),
        ('PERSONAL', 'Renta de Personal'),
    ]
    
    ESTADO = [
        ('ACTIVO', 'Activo'),
        ('FINALIZADO', 'Finalizado'),
        ('CANCELADO', 'Cancelado'),
    ]
    
    # Información básica
    numero_contrato = models.CharField(max_length=50, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    tipo_renta = models.CharField(max_length=20, choices=TIPO_RENTA)
    
    # Fechas
    fecha_inicio = models.DateField()
    fecha_fin_estimada = models.DateField()
    fecha_fin_real = models.DateField(null=True, blank=True)
    
    # Para renta de equipo
    equipo = models.ForeignKey(EquipoRenta, on_delete=models.PROTECT, null=True, blank=True)
    
    # Para renta de personal
    nombre_personal = models.CharField(max_length=200, blank=True)
    puesto_personal = models.CharField(max_length=100, blank=True)
    
    # Costos
    costo_diario = models.DecimalField(max_digits=10, decimal_places=2)
    deposito_garantia = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # Estado
    estado = models.CharField(max_length=20, choices=ESTADO, default='ACTIVO')
    
    # Metadatos
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    notas = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Contrato de Renta'
        verbose_name_plural = 'Contratos de Renta'
    
    def __str__(self):
        return f"{self.numero_contrato} - {self.cliente.nombre_completo()}"
    
    def dias_rentados(self):
        fecha_fin = self.fecha_fin_real or timezone.now().date()
        return (fecha_fin - self.fecha_inicio).days
    
    def costo_total(self):
        return self.costo_diario * self.dias_rentados()
