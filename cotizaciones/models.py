from django.db import models
from clientes.models import Cliente
from inventario.models import Producto


class Cotizacion(models.Model):
    """Cotizaciones para clientes"""
    ESTADO = [
        ('BORRADOR', 'Borrador'),
        ('ENVIADA', 'Enviada'),
        ('APROBADA', 'Aprobada'),
        ('RECHAZADA', 'Rechazada'),
        ('VENCIDA', 'Vencida'),
        ('CONVERTIDA', 'Convertida a Factura'),
    ]
    
    VIGENCIA_DIAS = [
        (7, '7 días'),
        (15, '15 días'),
        (30, '30 días'),
        (60, '60 días'),
        (90, '90 días'),
    ]
    
    # Información básica
    numero_cotizacion = models.CharField(max_length=50, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    
    # Detalles
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    
    # Fechas
    fecha_emision = models.DateField()
    vigencia_dias = models.IntegerField(choices=VIGENCIA_DIAS, default=30)
    fecha_vencimiento = models.DateField()
    
    # Montos
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    descuento = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    itbis = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    # Estado y seguimiento
    estado = models.CharField(max_length=20, choices=ESTADO, default='BORRADOR')
    fecha_respuesta_cliente = models.DateField(null=True, blank=True)
    motivo_rechazo = models.TextField(blank=True)
    
    # Términos
    terminos_condiciones = models.TextField(blank=True)
    notas = models.TextField(blank=True)
    forma_pago = models.CharField(max_length=200, blank=True)
    tiempo_entrega = models.CharField(max_length=200, blank=True)
    
    # Conversión a factura
    factura_generada = models.CharField(max_length=50, blank=True,
                                       help_text='Número de factura generada')
    
    # Metadatos
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    creado_por = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Cotización'
        verbose_name_plural = 'Cotizaciones'
        ordering = ['-fecha_emision']
    
    def __str__(self):
        return f"{self.numero_cotizacion} - {self.cliente.nombre_completo()}"
    
    def calcular_totales(self):
        """Calcula los totales de la cotización"""
        items = self.items.all()
        self.subtotal = sum(item.total for item in items)
        self.itbis = sum(item.itbis_monto for item in items)
        self.total = self.subtotal + self.itbis - self.descuento
        self.save()
    
    def esta_vigente(self):
        from django.utils import timezone
        return self.estado == 'ENVIADA' and self.fecha_vencimiento >= timezone.now().date()
    
    def save(self, *args, **kwargs):
        # Calcular fecha de vencimiento
        if not self.fecha_vencimiento and self.fecha_emision:
            from datetime import timedelta
            self.fecha_vencimiento = self.fecha_emision + timedelta(days=self.vigencia_dias)
        super().save(*args, **kwargs)


class ItemCotizacion(models.Model):
    """Items de cotización"""
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, null=True, blank=True)
    
    # Descripción
    descripcion = models.CharField(max_length=500)
    especificaciones = models.TextField(blank=True)
    
    # Cantidades y precios
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Descuento
    descuento_porcentaje = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    descuento_monto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # ITBIS
    itbis_porcentaje = models.DecimalField(max_digits=5, decimal_places=2, default=18.00)
    itbis_monto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # Totales
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # Orden
    orden = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = 'Item de Cotización'
        verbose_name_plural = 'Items de Cotización'
        ordering = ['orden']
    
    def __str__(self):
        return f"{self.descripcion} x {self.cantidad}"
    
    def save(self, *args, **kwargs):
        from decimal import Decimal
        # Convertir todos a Decimal para evitar errores de tipo
        cantidad = Decimal(str(self.cantidad))
        precio_unitario = Decimal(str(self.precio_unitario))
        descuento_porcentaje = Decimal(str(self.descuento_porcentaje))
        itbis_porcentaje = Decimal(str(self.itbis_porcentaje))
        
        # Calcular totales antes de guardar
        self.subtotal = cantidad * precio_unitario
        self.descuento_monto = self.subtotal * (descuento_porcentaje / Decimal('100'))
        base_imponible = self.subtotal - self.descuento_monto
        self.itbis_monto = base_imponible * (itbis_porcentaje / Decimal('100'))
        self.total = self.subtotal - self.descuento_monto
        super().save(*args, **kwargs)


class SeguimientoCotizacion(models.Model):
    """Seguimiento de cotizaciones"""
    TIPO_SEGUIMIENTO = [
        ('ENVIO', 'Envío'),
        ('LLAMADA', 'Llamada'),
        ('EMAIL', 'Email'),
        ('REUNION', 'Reunión'),
        ('OTRO', 'Otro'),
    ]
    
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE, related_name='seguimientos')
    fecha = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=20, choices=TIPO_SEGUIMIENTO)
    descripcion = models.TextField()
    contacto = models.CharField(max_length=200, blank=True)
    proximo_seguimiento = models.DateField(null=True, blank=True)
    realizado_por = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Seguimiento'
        verbose_name_plural = 'Seguimientos'
        ordering = ['-fecha']
    
    def __str__(self):
        return f"{self.tipo} - {self.cotizacion.numero_cotizacion}"


class AprobacionCotizacion(models.Model):
    """Flujo de aprobación de cotizaciones"""
    ESTADO_APROBACION = [
        ('PENDIENTE', 'Pendiente'),
        ('APROBADA', 'Aprobada'),
        ('RECHAZADA', 'Rechazada'),
    ]
    
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE, related_name='aprobaciones')
    nivel = models.IntegerField(help_text='Nivel de aprobación')
    aprobador = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=ESTADO_APROBACION, default='PENDIENTE')
    
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_respuesta = models.DateTimeField(null=True, blank=True)
    
    comentarios = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Aprobación'
        verbose_name_plural = 'Aprobaciones'
        ordering = ['nivel', '-fecha_solicitud']
    
    def __str__(self):
        return f"Nivel {self.nivel} - {self.estado}"
