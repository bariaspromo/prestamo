from django.db import models
from decimal import Decimal


class CategoriaProducto(models.Model):
    """Categorías de productos/servicios"""
    TIPO_CATEGORIA = [
        ('PRODUCTO', 'Producto'),
        ('SERVICIO', 'Servicio'),
        ('EQUIPO', 'Equipo'),
    ]
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CATEGORIA)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Categoría de Producto'
        verbose_name_plural = 'Categorías de Productos'
    
    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


class Producto(models.Model):
    """Productos y servicios"""
    TIPO_INVENTARIO = [
        ('NORMAL', 'Stock Normal'),
        ('CONSIGNACION', 'Consignación'),
        ('DROPSHIPPING', 'Dropshipping'),
        ('SERVICIO', 'Servicio'),
    ]
    
    UNIDAD_MEDIDA = [
        ('UNIDAD', 'Unidad'),
        ('HORA', 'Hora'),
        ('DIA', 'Día'),
        ('MES', 'Mes'),
        ('PAQUETE', 'Paquete'),
    ]
    
    # Información básica
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.PROTECT)
    
    # Tipo de inventario
    tipo_inventario = models.CharField(max_length=20, choices=TIPO_INVENTARIO, default='NORMAL')
    unidad_medida = models.CharField(max_length=20, choices=UNIDAD_MEDIDA, default='UNIDAD')
    
    # Precios
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    precio_renta_dia = models.DecimalField(max_digits=10, decimal_places=2, default=0, 
                                           help_text='Precio de renta por día')
    
    # Impuestos
    itbis = models.DecimalField(max_digits=5, decimal_places=2, default=18.00,
                               help_text='ITBIS (%) aplicable')
    
    # Inventario
    stock_actual = models.IntegerField(default=0)
    stock_minimo = models.IntegerField(default=0)
    stock_maximo = models.IntegerField(default=100)
    
    # Proveedor (para dropshipping/consignación)
    proveedor_nombre = models.CharField(max_length=200, blank=True)
    proveedor_contacto = models.CharField(max_length=200, blank=True)
    
    # Control
    permite_venta = models.BooleanField(default=True)
    permite_renta = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    
    # Metadatos
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
    
    def necesita_reorden(self):
        return self.stock_actual <= self.stock_minimo
    
    def precio_con_itbis(self):
        return self.precio_venta * (1 + self.itbis / 100)


class MovimientoInventario(models.Model):
    """Movimientos de inventario"""
    TIPO_MOVIMIENTO = [
        ('ENTRADA', 'Entrada'),
        ('SALIDA', 'Salida'),
        ('AJUSTE', 'Ajuste'),
        ('DEVOLUCION', 'Devolución'),
    ]
    
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    tipo_movimiento = models.CharField(max_length=20, choices=TIPO_MOVIMIENTO)
    cantidad = models.IntegerField()
    stock_anterior = models.IntegerField()
    stock_nuevo = models.IntegerField()
    motivo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Movimiento de Inventario'
        verbose_name_plural = 'Movimientos de Inventario'
        ordering = ['-fecha']
    
    def __str__(self):
        return f"{self.tipo_movimiento} - {self.producto.nombre} ({self.cantidad})"


class EquipoRenta(models.Model):
    """Equipos disponibles para renta"""
    ESTADO_EQUIPO = [
        ('DISPONIBLE', 'Disponible'),
        ('RENTADO', 'Rentado'),
        ('MANTENIMIENTO', 'En Mantenimiento'),
        ('DAÑADO', 'Dañado'),
    ]
    
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, limit_choices_to={'permite_renta': True})
    numero_serie = models.CharField(max_length=100, unique=True)
    estado = models.CharField(max_length=20, choices=ESTADO_EQUIPO, default='DISPONIBLE')
    ubicacion = models.CharField(max_length=200)
    fecha_adquisicion = models.DateField()
    ultima_fecha_mantenimiento = models.DateField(null=True, blank=True)
    proxima_fecha_mantenimiento = models.DateField(null=True, blank=True)
    notas = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Equipo de Renta'
        verbose_name_plural = 'Equipos de Renta'
    
    def __str__(self):
        return f"{self.producto.nombre} - {self.numero_serie}"
