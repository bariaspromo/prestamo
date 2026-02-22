"""
Script para poblar la base de datos con datos de ejemplo
"""
import os
import django
from datetime import date, timedelta, datetime
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'servicios_core.settings')
django.setup()

from clientes.models import Cliente, ContactoCliente
from inventario.models import CategoriaProducto, Producto, EquipoRenta
from servicios.models import ContratoServicio, SLA, OrdenServicio, CronogramaServicio
from facturacion.models import SecuenciaNCF, Factura, ItemFactura, Pago
from cotizaciones.models import Cotizacion, ItemCotizacion
from personal.models import Empleado

def crear_datos_ejemplo():
    print("🚀 Creando datos de ejemplo...")
    
    # 1. Clientes
    print("\n👥 Creando clientes...")
    cliente1 = Cliente.objects.create(
        tipo_cliente='EMPRESA',
        tipo_documento='RNC',
        numero_documento='131234567',
        razon_social='Tecnología Dominicana SRL',
        nombre_comercial='TecnoDom',
        telefono_principal='+18095551234',
        email='info@tecnodom.do',
        direccion='Av. Winston Churchill #123',
        ciudad='Santo Domingo',
        provincia='Distrito Nacional',
        es_contribuyente=True,
        ncf_tipo='B01'
    )
    print(f"✅ Cliente empresa creado: {cliente1}")
    
    cliente2 = Cliente.objects.create(
        tipo_cliente='PERSONA',
        tipo_documento='CEDULA',
        numero_documento='40212345678',
        nombres='Juan Carlos',
        apellidos='Pérez García',
        telefono_principal='+18095559876',
        email='jperez@email.com',
        direccion='Calle Principal #45',
        ciudad='Santiago',
        provincia='Santiago',
        es_contribuyente=False,
        ncf_tipo='B02'
    )
    print(f"✅ Cliente persona creado: {cliente2}")
    
    # Contacto adicional
    ContactoCliente.objects.create(
        cliente=cliente1,
        nombre='María Rodríguez',
        cargo='Gerente de IT',
        telefono='+18095551235',
        email='mrodriguez@tecnodom.do',
        es_principal=True
    )
    
    # 2. Categorías y Productos
    print("\n📦 Creando productos y servicios...")
    cat_hardware = CategoriaProducto.objects.create(
        nombre='Hardware',
        tipo='PRODUCTO',
        descripcion='Equipos de computación y electrónica'
    )
    
    cat_servicio = CategoriaProducto.objects.create(
        nombre='Servicios Técnicos',
        tipo='SERVICIO',
        descripcion='Servicios de mantenimiento y soporte'
    )
    
    producto1 = Producto.objects.create(
        codigo='COMP-001',
        nombre='Laptop Dell Latitude 5420',
        descripcion='Laptop empresarial i5, 16GB RAM, 512GB SSD',
        categoria=cat_hardware,
        tipo_inventario='NORMAL',
        precio_compra=Decimal('45000.00'),
        precio_venta=Decimal('60000.00'),
        precio_renta_dia=Decimal('500.00'),
        stock_actual=10,
        stock_minimo=5,
        permite_venta=True,
        permite_renta=True
    )
    print(f"✅ Producto creado: {producto1}")
    
    servicio1 = Producto.objects.create(
        codigo='SERV-001',
        nombre='Mantenimiento Preventivo PC',
        descripcion='Limpieza, actualización de software, optimización',
        categoria=cat_servicio,
        tipo_inventario='SERVICIO',
        unidad_medida='HORA',
        precio_venta=Decimal('800.00'),
        stock_actual=0,
        permite_venta=True
    )
    print(f"✅ Servicio creado: {servicio1}")
    
    # Equipo de renta
    equipo1 = EquipoRenta.objects.create(
        producto=producto1,
        numero_serie='LAT5420-2024-001',
        estado='DISPONIBLE',
        ubicacion='Almacén Principal',
        fecha_adquisicion=date(2024, 1, 15)
    )
    print(f"✅ Equipo de renta creado: {equipo1}")
    
    # 3. Personal
    print("\n👷 Creando empleados...")
    tecnico1 = Empleado.objects.create(
        codigo_empleado='TEC-001',
        nombres='Carlos',
        apellidos='Martínez',
        cedula='40298765432',
        fecha_nacimiento=date(1990, 5, 15),
        telefono='+18095551111',
        email='cmartinez@empresa.do',
        direccion='Calle 5 #10',
        tipo_empleado='TECNICO',
        puesto='Técnico Senior',
        departamento='Servicios Técnicos',
        salario=Decimal('35000.00'),
        fecha_ingreso=date(2020, 1, 1),
        especialidades='Redes, Seguridad, Hardware'
    )
    print(f"✅ Empleado creado: {tecnico1}")
    
    # 4. Contrato de Servicio
    print("\n📋 Creando contrato de servicio...")
    contrato1 = ContratoServicio.objects.create(
        numero_contrato='CONT-2024-001',
        cliente=cliente1,
        tipo_contrato='IGUALA_SERVICIO',
        descripcion='Soporte técnico mensual',
        alcance='Mantenimiento preventivo mensual de 50 equipos, soporte remoto ilimitado',
        fecha_inicio=date(2024, 1, 1),
        fecha_fin=date(2024, 12, 31),
        valor_mensual=Decimal('25000.00'),
        frecuencia_pago='MENSUAL',
        estado='ACTIVO'
    )
    print(f"✅ Contrato creado: {contrato1}")
    
    # SLA asociado
    sla1 = SLA.objects.create(
        contrato=contrato1,
        nombre='SLA Soporte Crítico',
        descripcion='Respuesta inmediata para incidentes críticos',
        prioridad='CRITICA',
        tiempo_respuesta_horas=2,
        tiempo_resolucion_horas=4,
        horario_cobertura='24/7'
    )
    print(f"✅ SLA creado: {sla1}")
    
    # Cronograma
    CronogramaServicio.objects.create(
        contrato=contrato1,
        nombre='Mantenimiento Mensual',
        descripcion='Mantenimiento preventivo de equipos',
        frecuencia='MENSUAL',
        fecha_inicio=date(2024, 1, 1),
        proxima_ejecucion=date(2024, 2, 1),
        tecnico_predeterminado='Carlos Martínez'
    )
    
    # 5. Orden de Servicio
    print("\n🔧 Creando orden de servicio...")
    orden1 = OrdenServicio.objects.create(
        numero_orden='OS-2024-0001',
        cliente=cliente1,
        contrato=contrato1,
        sla=sla1,
        tipo_servicio='PREVENTIVO',
        prioridad='MEDIA',
        descripcion='Mantenimiento preventivo mensual',
        direccion_servicio='Av. Winston Churchill #123, Santo Domingo',
        fecha_programada=datetime(2024, 2, 15, 9, 0),
        tecnico_asignado='Carlos Martínez',
        estado='ASIGNADA'
    )
    print(f"✅ Orden de servicio creada: {orden1}")
    
    # 6. Secuencias NCF
    print("\n🧾 Creando secuencias NCF...")
    SecuenciaNCF.objects.create(
        tipo_comprobante='B01',
        serie='E',
        numero_actual=1,
        numero_desde=1,
        numero_hasta=10000,
        fecha_vencimiento=date(2024, 12, 31)
    )
    
    SecuenciaNCF.objects.create(
        tipo_comprobante='B02',
        serie='E',
        numero_actual=1,
        numero_desde=1,
        numero_hasta=10000,
        fecha_vencimiento=date(2024, 12, 31)
    )
    print("✅ Secuencias NCF creadas")
    
    # 7. Cotización
    print("\n📄 Creando cotización...")
    cotizacion1 = Cotizacion.objects.create(
        numero_cotizacion='COT-2024-0001',
        cliente=cliente2,
        titulo='Equipos de Computación',
        descripcion='Cotización para compra de equipos',
        fecha_emision=date.today(),
        vigencia_dias=30,
        estado='ENVIADA',
        creado_por='Admin'
    )
    print(f"✅ Cotización creada: {cotizacion1}")
    
    # Items de cotización
    item_cot = ItemCotizacion.objects.create(
        cotizacion=cotizacion1,
        producto=producto1,
        descripcion=producto1.nombre,
        cantidad=Decimal('5'),
        precio_unitario=producto1.precio_venta,
        orden=1
    )
    cotizacion1.calcular_totales()
    print(f"✅ Items de cotización agregados")
    
    # 8. Factura
    print("\n💰 Creando factura...")
    factura1 = Factura.objects.create(
        numero_factura='FAC-2024-0001',
        ncf='B0100000001',
        tipo_ncf='B01',
        cliente=cliente1,
        tipo_ingreso='SERVICIO',
        fecha_emision=date.today(),
        fecha_vencimiento=date.today() + timedelta(days=30),
        estado='EMITIDA',
        creado_por='Admin'
    )
    
    # Items de factura
    ItemFactura.objects.create(
        factura=factura1,
        producto=servicio1,
        descripcion='Mantenimiento Preventivo - 10 PCs',
        cantidad=Decimal('10'),
        precio_unitario=Decimal('800.00')
    )
    
    factura1.calcular_totales()
    print(f"✅ Factura creada: {factura1} - Total: RD${factura1.total}")
    
    # Pago
    pago1 = Pago.objects.create(
        numero_recibo='REC-2024-0001',
        factura=factura1,
        fecha_pago=date.today(),
        monto=factura1.total,
        metodo_pago='TRANSFERENCIA',
        referencia='TRANS-12345',
        banco='Banco Popular',
        registrado_por='Admin'
    )
    print(f"✅ Pago registrado: {pago1}")
    
    print("\n" + "="*60)
    print("✅ Datos de ejemplo creados exitosamente!")
    print("="*60)
    print("\n📊 Resumen:")
    print(f"   👥 Clientes: {Cliente.objects.count()}")
    print(f"   📦 Productos: {Producto.objects.count()}")
    print(f"   👷 Empleados: {Empleado.objects.count()}")
    print(f"   📋 Contratos: {ContratoServicio.objects.count()}")
    print(f"   🔧 Órdenes de Servicio: {OrdenServicio.objects.count()}")
    print(f"   💰 Facturas: {Factura.objects.count()}")
    print(f"   📄 Cotizaciones: {Cotizacion.objects.count()}")
    print("\n🌐 Inicia el servidor con: python manage.py runserver")
    print("🔐 Accede al admin en: http://127.0.0.1:8000/admin")

if __name__ == '__main__':
    crear_datos_ejemplo()
