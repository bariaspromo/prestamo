from django.db import models
from clientes.models import Cliente
from inventario.models import Producto
from decimal import Decimal


class SecuenciaNCF(models.Model):
    """Secuencias de Números de Comprobante Fiscal (NCF) - DGII"""
    TIPO_NCF = [
        ('B01', 'Facturas de Crédito Fiscal'),
        ('B02', 'Facturas de Consumo'),
        ('B14', 'Régimen Especial de Tributación'),
        ('B15', 'Gubernamental'),
        ('B16', 'Exportaciones'),
    ]
    
    tipo_comprobante = models.CharField(max_length=3, choices=TIPO_NCF, unique=True)
    serie = models.CharField(max_length=1, default='E', help_text='Serie del NCF (ej: E)')
    numero_actual = models.IntegerField(default=1)
    numero_desde = models.IntegerField(default=1)
    numero_hasta = models.IntegerField()
    fecha_vencimiento = models.DateField()
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Secuencia NCF'
        verbose_name_plural = 'Secuencias NCF'
    
    def __str__(self):
        return f"{self.tipo_comprobante} - {self.serie}{self.numero_actual:08d}"
    
    def obtener_siguiente_ncf(self):
        """Obtiene el siguiente NCF disponible"""
        if self.numero_actual > self.numero_hasta:
            raise ValueError('Se agotaron los NCF de esta secuencia')
        
        ncf = f"{self.tipo_comprobante}{self.serie}{self.numero_actual:08d}"
        self.numero_actual += 1
        self.save()
        return ncf


class Factura(models.Model):
    """Facturas con cumplimiento DGII"""
    ESTADO = [
        ('BORRADOR', 'Borrador'),
        ('EMITIDA', 'Emitida'),
        ('PAGADA', 'Pagada'),
        ('PARCIAL', 'Pago Parcial'),
        ('VENCIDA', 'Vencida'),
        ('ANULADA', 'Anulada'),
    ]
    
    TIPO_INGRESO = [
        ('PRODUCTO', 'Venta de Producto'),
        ('SERVICIO', 'Servicio'),
        ('RENTA', 'Renta'),
        ('IGUALA', 'Iguala'),
    ]
    
    # Información básica
    numero_factura = models.CharField(max_length=50, unique=True)
    ncf = models.CharField(max_length=13, unique=True, blank=True,
                          help_text='Número de Comprobante Fiscal (DGII)')
    tipo_ncf = models.CharField(max_length=3, blank=True)
    
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    tipo_ingreso = models.CharField(max_length=20, choices=TIPO_INGRESO)
    
    # Fechas
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    
    # Montos
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    descuento = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    itbis = models.DecimalField(max_digits=12, decimal_places=2, default=0,
                               help_text='Impuesto ITBIS (18%)')
    otros_impuestos = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    monto_pagado = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    # Estado
    estado = models.CharField(max_length=20, choices=ESTADO, default='BORRADOR')
    
    # Notas
    observaciones = models.TextField(blank=True)
    terminos_condiciones = models.TextField(blank=True)
    
    # Metadatos
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    creado_por = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
        ordering = ['-fecha_emision']
    
    def __str__(self):
        return f"{self.numero_factura} - {self.cliente.nombre_completo()}"
    
    def calcular_totales(self):
        """Calcula los totales de la factura"""
        items = self.items.all()
        self.subtotal = sum(item.total for item in items)
        self.itbis = sum(item.itbis_monto for item in items)
        self.total = self.subtotal + self.itbis + self.otros_impuestos - self.descuento
        self.save()
    
    def saldo_pendiente(self):
        return self.total - self.monto_pagado
    
    def esta_vencida(self):
        from django.utils import timezone
        return self.estado in ['EMITIDA', 'PARCIAL'] and self.fecha_vencimiento < timezone.now().date()


class ItemFactura(models.Model):
    """Items de factura"""
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, null=True, blank=True)
    
    # Descripción (puede ser diferente del producto)
    descripcion = models.CharField(max_length=500)
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
    
    class Meta:
        verbose_name = 'Item de Factura'
        verbose_name_plural = 'Items de Factura'
    
    def __str__(self):
        return f"{self.descripcion} x {self.cantidad}"
    
    def save(self, *args, **kwargs):
        # Calcular totales antes de guardar
        self.subtotal = self.cantidad * self.precio_unitario
        self.descuento_monto = self.subtotal * (self.descuento_porcentaje / 100)
        base_imponible = self.subtotal - self.descuento_monto
        self.itbis_monto = base_imponible * (self.itbis_porcentaje / 100)
        self.total = self.subtotal - self.descuento_monto
        super().save(*args, **kwargs)


class Pago(models.Model):
    """Pagos recibidos"""
    METODO_PAGO = [
        ('EFECTIVO', 'Efectivo'),
        ('CHEQUE', 'Cheque'),
        ('TRANSFERENCIA', 'Transferencia Bancaria'),
        ('TARJETA_CREDITO', 'Tarjeta de Crédito'),
        ('TARJETA_DEBITO', 'Tarjeta de Débito'),
    ]
    
    # Información básica
    numero_recibo = models.CharField(max_length=50, unique=True)
    factura = models.ForeignKey(Factura, on_delete=models.PROTECT, related_name='pagos')
    
    # Detalles del pago
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    metodo_pago = models.CharField(max_length=20, choices=METODO_PAGO)
    
    # Referencias
    referencia = models.CharField(max_length=100, blank=True,
                                 help_text='Número de cheque, referencia de transferencia, etc.')
    banco = models.CharField(max_length=100, blank=True)
    
    # Notas
    observaciones = models.TextField(blank=True)
    
    # Metadatos
    fecha_registro = models.DateTimeField(auto_now_add=True)
    registrado_por = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        ordering = ['-fecha_pago']
    
    def __str__(self):
        return f"{self.numero_recibo} - RD${self.monto}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Actualizar el monto pagado de la factura
        self.factura.monto_pagado = sum(p.monto for p in self.factura.pagos.all())
        
        # Actualizar estado de la factura
        if self.factura.monto_pagado >= self.factura.total:
            self.factura.estado = 'PAGADA'
        elif self.factura.monto_pagado > 0:
            self.factura.estado = 'PARCIAL'
        
        self.factura.save()


class NotaCredito(models.Model):
    """Notas de crédito"""
    MOTIVO = [
        ('DEVOLUCION', 'Devolución'),
        ('DESCUENTO', 'Descuento'),
        ('ERROR', 'Error en Factura'),
        ('OTRO', 'Otro'),
    ]
    
    numero_nota = models.CharField(max_length=50, unique=True)
    ncf = models.CharField(max_length=13, unique=True, blank=True)
    factura_original = models.ForeignKey(Factura, on_delete=models.PROTECT)
    
    fecha_emision = models.DateField()
    motivo = models.CharField(max_length=20, choices=MOTIVO)
    descripcion = models.TextField()
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Nota de Crédito'
        verbose_name_plural = 'Notas de Crédito'
    
    def __str__(self):
        return f"{self.numero_nota} - RD${self.monto}"
