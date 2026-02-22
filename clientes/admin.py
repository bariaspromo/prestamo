from django.contrib import admin
from .models import Cliente, ContactoCliente, DocumentoCliente


class ContactoClienteInline(admin.TabularInline):
    model = ContactoCliente
    extra = 1


class DocumentoClienteInline(admin.TabularInline):
    model = DocumentoCliente
    extra = 0


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['numero_documento', 'nombre_completo', 'tipo_cliente', 'telefono_principal', 'email', 'activo']
    list_filter = ['tipo_cliente', 'activo', 'es_contribuyente', 'provincia']
    search_fields = ['numero_documento', 'nombres', 'apellidos', 'razon_social', 'email']
    readonly_fields = ['fecha_registro', 'fecha_actualizacion']
    inlines = [ContactoClienteInline, DocumentoClienteInline]
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('tipo_cliente', 'tipo_documento', 'numero_documento')
        }),
        ('Persona Física', {
            'fields': ('nombres', 'apellidos'),
            'classes': ('collapse',),
        }),
        ('Empresa', {
            'fields': ('razon_social', 'nombre_comercial'),
            'classes': ('collapse',),
        }),
        ('Contacto', {
            'fields': ('telefono_principal', 'telefono_secundario', 'email')
        }),
        ('Dirección', {
            'fields': ('direccion', 'ciudad', 'provincia', 'codigo_postal')
        }),
        ('Datos Fiscales (DGII)', {
            'fields': ('es_contribuyente', 'ncf_tipo')
        }),
        ('Control', {
            'fields': ('activo', 'notas', 'fecha_registro', 'fecha_actualizacion')
        }),
    )


@admin.register(ContactoCliente)
class ContactoClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cliente', 'cargo', 'telefono', 'email', 'es_principal', 'activo']
    list_filter = ['es_principal', 'activo']
    search_fields = ['nombre', 'email', 'cliente__nombres', 'cliente__razon_social']


@admin.register(DocumentoCliente)
class DocumentoClienteAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'cliente', 'tipo', 'fecha_subida']
    list_filter = ['tipo', 'fecha_subida']
    search_fields = ['titulo', 'descripcion', 'cliente__nombres', 'cliente__razon_social']
