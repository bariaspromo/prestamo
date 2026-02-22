from django.db import models
from django.core.validators import RegexValidator


class Cliente(models.Model):
    """Modelo para gestión de clientes"""
    TIPO_CLIENTE = [
        ('PERSONA', 'Persona Física'),
        ('EMPRESA', 'Empresa'),
    ]
    
    TIPO_DOCUMENTO = [
        ('CEDULA', 'Cédula'),
        ('RNC', 'RNC'),
        ('PASAPORTE', 'Pasaporte'),
    ]
    
    # Información básica
    tipo_cliente = models.CharField(max_length=10, choices=TIPO_CLIENTE, default='PERSONA')
    tipo_documento = models.CharField(max_length=20, choices=TIPO_DOCUMENTO)
    numero_documento = models.CharField(max_length=50, unique=True)
    
    # Persona física
    nombres = models.CharField(max_length=100, blank=True)
    apellidos = models.CharField(max_length=100, blank=True)
    
    # Empresa
    razon_social = models.CharField(max_length=200, blank=True)
    nombre_comercial = models.CharField(max_length=200, blank=True)
    
    # Contacto
    telefono_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="El número de teléfono debe estar en formato: '+999999999'. Hasta 15 dígitos permitidos."
    )
    telefono_principal = models.CharField(validators=[telefono_validator], max_length=17)
    telefono_secundario = models.CharField(validators=[telefono_validator], max_length=17, blank=True)
    email = models.EmailField()
    
    # Dirección
    direccion = models.TextField()
    ciudad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20, blank=True)
    
    # Datos fiscales (DGII)
    ncf_tipo = models.CharField(max_length=50, blank=True, help_text='Tipo de NCF para facturación')
    es_contribuyente = models.BooleanField(default=False)
    
    # Metadatos
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    notas = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-fecha_registro']
    
    def __str__(self):
        if self.tipo_cliente == 'EMPRESA':
            return f"{self.razon_social} ({self.numero_documento})"
        return f"{self.nombres} {self.apellidos} ({self.numero_documento})"
    
    def nombre_completo(self):
        if self.tipo_cliente == 'EMPRESA':
            return self.razon_social
        return f"{self.nombres} {self.apellidos}"


class ContactoCliente(models.Model):
    """Contactos adicionales del cliente"""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contactos')
    nombre = models.CharField(max_length=200)
    cargo = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=17)
    email = models.EmailField()
    es_principal = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
    
    def __str__(self):
        return f"{self.nombre} - {self.cliente}"


class DocumentoCliente(models.Model):
    """Documentos asociados al cliente"""
    TIPO_DOCUMENTO = [
        ('CONTRATO', 'Contrato'),
        ('CEDULA', 'Cédula/RNC'),
        ('COMPROBANTE', 'Comprobante de Pago'),
        ('OTRO', 'Otro'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='documentos')
    tipo = models.CharField(max_length=20, choices=TIPO_DOCUMENTO)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    archivo = models.FileField(upload_to='documentos_clientes/%Y/%m/')
    fecha_subida = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        ordering = ['-fecha_subida']
    
    def __str__(self):
        return f"{self.titulo} - {self.cliente}"
