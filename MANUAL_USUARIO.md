# 📘 Manual de Usuario - Sistema de Gestión de Servicios

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Acceso al Sistema](#acceso-al-sistema)
3. [Módulos del Sistema](#módulos-del-sistema)
4. [Guías de Uso](#guías-de-uso)

---

## Introducción

Sistema integral de gestión empresarial diseñado para empresas de servicios técnicos en República Dominicana. Incluye:

- ✅ Gestión de Clientes (CRM)
- ✅ Inventario y Productos
- ✅ Servicios y Contratos
- ✅ Facturación con NCF (DGII)
- ✅ Cotizaciones
- ✅ Personal y Técnicos

---

## Acceso al Sistema

### Iniciar el Sistema

```bash
# Activar entorno virtual
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Iniciar servidor
python manage.py runserver
```

### Acceder al Panel de Administración

1. Abrir navegador en: `http://127.0.0.1:8000/admin`
2. Ingresar credenciales de administrador
3. Navegar por los módulos disponibles

---

## Módulos del Sistema

### 👥 CLIENTES

**Gestión de clientes personas físicas y empresas**

#### Campos Principales:
- **Tipo de Cliente**: Persona o Empresa
- **Tipo de Documento**: Cédula, RNC, Pasaporte
- **Número de Documento**: Identificación única
- **Datos de Contacto**: Teléfono, email, dirección
- **Datos Fiscales**: Tipo de NCF, si es contribuyente

#### Funcionalidades:
- Registro de clientes personas y empresas
- Múltiples contactos por cliente
- Gestión de documentos adjuntos
- Historial completo de transacciones

---

### 📦 INVENTARIO

**Gestión de productos, servicios y equipos**

#### Tipos de Inventario:
1. **Stock Normal**: Inventario propio
2. **Consignación**: Productos de terceros
3. **Dropshipping**: Envío directo del proveedor
4. **Servicio**: Servicios técnicos

#### Características:
- Control de stock mínimo/máximo
- Precios de venta y renta
- ITBIS configurable (18% por defecto)
- Movimientos de inventario rastreados
- Equipos de renta individualizados

---

### 🔧 SERVICIOS

**Gestión de contratos y órdenes de servicio**

#### 1. Contratos de Servicio (Igualas)

**Tipos de Contratos:**
- Iguala de Equipo
- Iguala de Servicio
- Mantenimiento Preventivo
- Soporte Técnico
- Renta de Equipo/Personal

**Estados:**
- Borrador
- Activo
- Suspendido
- Finalizado
- Cancelado

#### 2. SLA (Service Level Agreements)

Define los tiempos de respuesta y resolución:
- **Tiempo de Respuesta**: Horas para primera respuesta
- **Tiempo de Resolución**: Horas para solucionar
- **Horario de Cobertura**: 24/7, horario laboral, etc.
- **Prioridad**: Crítica, Alta, Media, Baja

#### 3. Órdenes de Servicio

**Tipos de Servicio:**
- Mantenimiento Preventivo
- Mantenimiento Correctivo
- Instalación
- Reparación
- Soporte Técnico

**Flujo de Trabajo:**
1. Pendiente → Cliente solicita servicio
2. Asignada → Se asigna técnico
3. En Proceso → Técnico trabajando
4. Completada → Servicio finalizado
5. Cancelada → Servicio cancelado

**Tracking de SLA:**
- El sistema verifica automáticamente si se cumple el SLA
- Calcula tiempos de respuesta y resolución
- Alerta sobre incumplimientos

#### 4. Cronogramas de Servicios

Servicios recurrentes automáticos:
- Diario, Semanal, Quincenal, Mensual, etc.
- Asignación automática de técnico
- Generación automática de órdenes

---

### 💰 FACTURACIÓN (DGII Compliant)

**Sistema de facturación con cumplimiento fiscal dominicano**

#### Números de Comprobante Fiscal (NCF)

El sistema maneja los tipos oficiales de NCF:

| Tipo | Uso |
|------|-----|
| B01  | Facturas de Crédito Fiscal (con ITBIS) |
| B02  | Facturas de Consumo (sin ITBIS) |
| B14  | Régimen Especial de Tributación |
| B15  | Gubernamental |
| B16  | Exportaciones |

#### Configuración de Secuencias NCF:

Antes de facturar, configurar:
1. **Tipo de Comprobante**: B01, B02, etc.
2. **Serie**: Generalmente 'E'
3. **Rango**: Desde - Hasta
4. **Fecha de Vencimiento**: Según DGII

#### Proceso de Facturación:

1. **Crear Factura**
   - Seleccionar cliente
   - El NCF se asigna automáticamente
   - Agregar items (productos/servicios)
   - El sistema calcula ITBIS automáticamente

2. **Items de Factura**
   - Descripción del producto/servicio
   - Cantidad
   - Precio unitario
   - Descuento (opcional)
   - ITBIS se calcula automáticamente (18%)

3. **Registrar Pagos**
   - Efectivo, Cheque, Transferencia, Tarjeta
   - Pagos parciales o completos
   - Se genera recibo automáticamente
   - Estado de factura se actualiza automáticamente

4. **Notas de Crédito**
   - Para devoluciones o ajustes
   - Se asigna NCF automáticamente
   - Referencia a factura original

---

### 📋 COTIZACIONES

**Sistema de cotizaciones con seguimiento**

#### Proceso de Cotización:

1. **Crear Cotización**
   - Cliente
   - Título y descripción
   - Vigencia (7, 15, 30, 60, 90 días)

2. **Agregar Items**
   - Productos/servicios del catálogo
   - Cantidades y precios
   - Descuentos
   - ITBIS calculado automáticamente

3. **Seguimiento**
   - Envíos, llamadas, reuniones
   - Historial completo
   - Próximos seguimientos programados

4. **Aprobación**
   - Flujo de aprobación por niveles
   - Comentarios de aprobadores
   - Estado: Pendiente, Aprobada, Rechazada

5. **Conversión a Factura**
   - Una vez aprobada, convertir a factura
   - Se transfieren todos los items
   - Se genera NCF automáticamente

---

### 👷 PERSONAL

**Gestión de empleados y técnicos**

#### Registro de Empleados:

**Tipos de Empleado:**
- Técnico
- Vendedor
- Administrativo
- Gerente

**Información Importante:**
- Datos personales y laborales
- Especialidades técnicas
- Certificaciones
- Horario de trabajo
- Disponibilidad para emergencias

#### Asignación de Servicios:

- Asignar técnico a orden de servicio
- Registrar horas trabajadas
- Seguimiento de estado

#### Asignación a Contratos:

- Asignar personal a contratos de servicio
- Definir rol en el contrato
- Responsable principal

#### Control de Disponibilidad:

**Tipos de Eventos:**
- Vacaciones
- Licencias
- Capacitación
- Ausencias

#### Métricas de Rendimiento:

**Por período (mes):**
- Servicios asignados
- Servicios completados
- Servicios a tiempo
- Calificación promedio (1-5)
- Horas trabajadas
- Tasa de cumplimiento

---

## Guías de Uso

### 📝 Cómo Crear una Factura Completa

1. **Configurar Secuencia NCF** (Una vez)
   - Ir a Facturación → Secuencias NCF
   - Agregar secuencia con tipo B01 o B02
   - Establecer rango y vencimiento

2. **Crear Factura**
   - Ir a Facturación → Facturas → Agregar
   - Seleccionar cliente
   - El número de factura y NCF se asignan automáticamente
   - Establecer fechas de emisión y vencimiento

3. **Agregar Items**
   - En la misma pantalla, sección "Items de factura"
   - Agregar línea: producto/servicio, cantidad, precio
   - El sistema calcula ITBIS y totales automáticamente

4. **Guardar**
   - El estado será "Borrador" inicialmente
   - Cambiar a "Emitida" cuando esté lista

5. **Registrar Pago**
   - Ir a la factura
   - Sección "Pagos" → Agregar
   - Método, monto, referencia
   - El sistema actualiza estado automáticamente

### 🔧 Cómo Gestionar un Servicio de Inicio a Fin

1. **Crear Contrato de Servicio**
   - Clientes → Seleccionar cliente
   - Servicios → Contratos → Agregar
   - Tipo: Iguala de Servicio
   - Definir alcance, fechas, valor

2. **Definir SLA**
   - En el mismo contrato, agregar SLA
   - Tiempos de respuesta y resolución
   - Horario de cobertura

3. **Crear Cronograma** (Opcional para servicios recurrentes)
   - Servicios → Cronogramas → Agregar
   - Frecuencia: Mensual, etc.
   - Técnico predeterminado

4. **Generar Orden de Servicio**
   - Servicios → Órdenes de Servicio → Agregar
   - Asociar a contrato y SLA
   - Asignar técnico
   - Programar fecha

5. **Ejecutar Servicio**
   - El técnico actualiza estado:
     - Asignada → En Proceso → Completada
   - Registra diagnóstico y solución
   - Cliente califica servicio (1-5)

6. **Verificar Cumplimiento de SLA**
   - El sistema calcula automáticamente
   - Se muestra en la orden de servicio

### 💼 Cómo Gestionar una Cotización

1. **Crear Cotización**
   - Cotizaciones → Agregar
   - Cliente, título, descripción
   - Vigencia (días)

2. **Agregar Productos/Servicios**
   - Items de cotización
   - Del catálogo o manual
   - Cantidades, precios, descuentos

3. **Calcular Totales**
   - Usar acción "Calcular totales" si es necesario
   - Sistema calcula ITBIS automáticamente

4. **Enviar al Cliente**
   - Cambiar estado a "Enviada"
   - Registrar seguimiento (envío email/físico)

5. **Seguimiento**
   - Registrar llamadas, reuniones, emails
   - Programar próximos seguimientos

6. **Respuesta del Cliente**
   - Si aprueba: Estado → "Aprobada"
   - Si rechaza: Estado → "Rechazada" + motivo

7. **Convertir a Factura**
   - Si aprobada, crear factura con los mismos items
   - Guardar número de factura en cotización

---

## 🔍 Reportes Disponibles

### Desde el Admin de Django:

1. **Filtros Avanzados**
   - Todos los listados tienen filtros por fecha, estado, etc.
   
2. **Búsqueda**
   - Buscar por número de documento, nombre, etc.

3. **Exportación**
   - Seleccionar registros
   - Usar acciones disponibles

### Reportes Futuros (Próximas Versiones):

- Reporte de ventas por período
- Reporte de servicios por técnico
- Reporte de cumplimiento de SLA
- Reporte de inventario
- Reporte fiscal (DGII)

---

## 🔐 Seguridad y Permisos

### Usuarios y Roles:

Django Admin permite crear usuarios con diferentes permisos:

1. **Superusuario**: Acceso total
2. **Staff**: Acceso al admin
3. **Permisos Personalizados**: Por modelo

### Configurar Permisos:

1. Ir a Auth → Usuarios
2. Editar usuario
3. Marcar "Staff status" para acceso al admin
4. Asignar permisos específicos por modelo

---

## 📞 Soporte

Para asistencia técnica o preguntas, contactar al administrador del sistema.

---

## 📚 Recursos Adicionales

- **Documentación Django**: https://docs.djangoproject.com
- **DGII (Impuestos RD)**: https://www.dgii.gov.do
- **Normativa NCF**: Ver sitio web DGII

---

> **💡 Tip**: Use los filtros y búsquedas en cada sección para encontrar rápidamente lo que necesita.

> **⚠️ Importante**: Siempre mantenga actualizadas las secuencias de NCF antes de que venzan para evitar problemas de facturación.
