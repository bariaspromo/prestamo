# 🏢 Sistema de Gestión de Servicios - República Dominicana

[![Licencia](https://img.shields.io/badge/Licencia-Privada-red.svg)]()
[![Versión](https://img.shields.io/badge/Versión-1.0-blue.svg)]()
[![Python](https://img.shields.io/badge/Python-3.12-green.svg)]()
[![Django](https://img.shields.io/badge/Django-6.0-green.svg)]()

---

## 📌 Descripción

Sistema integral de gestión empresarial para empresas de servicios y productos de:
- 💻 Informática
- 🔌 Electrónica
- ⚡ Electricidad
- 🔒 Seguridad Electrónica

Con cumplimiento fiscal **DGII (República Dominicana)** integrado.

---

## 🏗️ Arquitectura del Sistema

```
Sistema de Gestión de Servicios
├── 👥 Clientes (CRM)
│   ├── Gestión de clientes personas/empresas
│   ├── Contactos múltiples por cliente
│   ├── Documentos y archivos
│   └── Datos fiscales DGII
│
├── 📦 Inventario
│   ├── Productos y servicios
│   ├── Stock normal
│   ├── Consignación
│   ├── Dropshipping
│   ├── Equipos de renta
│   └── Movimientos de inventario
│
├── 🔧 Servicios
│   ├── Contratos de servicio (igualas)
│   ├── Órdenes de servicio
│   ├── SLA (Acuerdos de Nivel de Servicio)
│   ├── Cronogramas de servicios
│   └── Contratos de renta (equipos/personal)
│
├── 💰 Facturación
│   ├── Facturas con NCF (DGII)
│   ├── Secuencias NCF
│   ├── Pagos y recibos
│   ├── Notas de crédito
│   └── Cumplimiento fiscal RD
│
├── 📋 Cotizaciones
│   ├── Generación de cotizaciones
│   ├── Seguimiento
│   ├── Aprobaciones
│   └── Conversión a factura
│
└── 👷 Personal
    ├── Empleados y técnicos
    ├── Asignación a servicios
    ├── Asignación a contratos
    ├── Disponibilidad
    └── Rendimiento
```

---

## ✨ Características Principales

### 🧾 Facturación DGII Compliant
- ✅ Números de Comprobante Fiscal (NCF)
- ✅ Tipos de NCF (B01, B02, B14, B15, B16)
- ✅ ITBIS (18%)
- ✅ Secuencias de NCF con control de vencimiento
- ✅ Notas de crédito

### 📊 Gestión de Servicios
- Contratos de servicio (igualas de equipos y servicios)
- Órdenes de servicio con seguimiento completo
- SLA (Service Level Agreements)
- Cronogramas de servicios recurrentes
- Calificación de satisfacción del cliente

### 💼 Gestión de Clientes (CRM)
- Clientes personas físicas y empresas
- Cédula, RNC, Pasaporte
- Múltiples contactos por cliente
- Gestión documental
- Historial completo

### 📦 Inventario Avanzado
- Stock normal
- Inventario en consignación
- Dropshipping
- Control de stock mínimo/máximo
- Movimientos de inventario
- Equipos de renta con seguimiento

### 💵 Cotizaciones
- Generación de cotizaciones profesionales
- Seguimiento de cotizaciones
- Flujo de aprobación
- Conversión automática a factura

### 👥 Gestión de Personal
- Empleados/técnicos
- Asignación a servicios
- Asignación a contratos
- Control de disponibilidad
- Métricas de rendimiento

---

## 🚀 Instalación

### Requisitos Previos
- Python 3.12+
- pip

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/bariaspromo/prestamo.git
cd prestamo
```

2. **Crear entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Ejecutar migraciones**
```bash
python manage.py migrate
```

5. **Crear superusuario**
```bash
python manage.py createsuperuser
```

6. **Iniciar servidor de desarrollo**
```bash
python manage.py runserver
```

7. **Acceder al panel de administración**
```
http://127.0.0.1:8000/admin
```

---

## 📁 Estructura del Proyecto

```
prestamo/
├── manage.py
├── requirements.txt
├── .gitignore
├── servicios_core/          # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── clientes/                # App de clientes
│   ├── models.py           # Cliente, Contacto, Documento
│   └── admin.py
├── inventario/             # App de inventario
│   ├── models.py          # Producto, Categoría, Movimiento, EquipoRenta
│   └── admin.py
├── servicios/              # App de servicios
│   ├── models.py          # Contrato, SLA, OrdenServicio, Cronograma, ContratoRenta
│   └── admin.py
├── facturacion/            # App de facturación
│   ├── models.py          # Factura, ItemFactura, Pago, NCF, NotaCredito
│   └── admin.py
├── cotizaciones/           # App de cotizaciones
│   ├── models.py          # Cotizacion, Item, Seguimiento, Aprobacion
│   └── admin.py
└── personal/               # App de personal
    ├── models.py          # Empleado, Asignacion, Disponibilidad, Rendimiento
    └── admin.py
```

---

## 🔐 Seguridad

- Validación de datos en todos los modelos
- Protección CSRF habilitada
- Autenticación requerida para acceso al admin
- Control de acceso basado en permisos de Django

---

## 📊 Modelos de Datos Principales

### Cliente
- Persona física o empresa
- Cédula / RNC / Pasaporte
- Datos fiscales para DGII
- Múltiples contactos

### Producto
- Productos físicos o servicios
- Stock normal / Consignación / Dropshipping
- Control de inventario
- Precios de venta y renta

### Contrato de Servicio
- Igualas de equipos y servicios
- SLA configurables
- Cronogramas de servicios recurrentes

### Factura
- NCF (DGII compliant)
- ITBIS automático
- Multiple items
- Pagos parciales/completos
- Estados: Borrador, Emitida, Pagada, Vencida, Anulada

### Orden de Servicio
- Tipos: Preventivo, Correctivo, Instalación, Reparación
- Prioridades y estados
- Asignación de técnicos
- Tracking de SLA
- Calificación del cliente

---

## 🇩🇴 Cumplimiento DGII

### Números de Comprobante Fiscal (NCF)

El sistema soporta todos los tipos de NCF:

| Tipo | Descripción |
|------|-------------|
| B01  | Facturas de Crédito Fiscal |
| B02  | Facturas de Consumo |
| B14  | Régimen Especial de Tributación |
| B15  | Gubernamental |
| B16  | Exportaciones |

### Características
- Secuencias NCF con control de rango y vencimiento
- Generación automática de NCF al emitir factura
- ITBIS (18%) calculado automáticamente
- Soporte para notas de crédito

---

## 🛠️ Tecnologías Utilizadas

| Categoría | Tecnología |
|-----------|------------|
| Backend | Python 3.12, Django 6.0 |
| Base de Datos | SQLite (desarrollo), PostgreSQL/MySQL (producción) |
| Admin UI | Django Admin |
| Validación | Django Forms & Validators |

---

## 📈 Próximas Características

- [ ] API REST con Django REST Framework
- [ ] Frontend web (React/Vue)
- [ ] Reportes en PDF
- [ ] Dashboard con gráficos
- [ ] Notificaciones por email/SMS
- [ ] Integración con WhatsApp Business
- [ ] App móvil para técnicos
- [ ] Portal de autoservicio para clientes
- [ ] Generación automática de NCF electrónicos
- [ ] Integración con bancos para pagos

---

## 📄 Licencia

Este proyecto es de uso **privado**. Todos los derechos reservados.

---

## 👤 Autor

**bariaspromo** — Sistema de gestión para empresas de servicios de informática y electrónica.

---

## 📞 Soporte

Para soporte técnico o consultas, contactar al administrador del sistema.

---

> **📌 Nota:** Este es un sistema empresarial completo diseñado específicamente para empresas de servicios técnicos en República Dominicana con cumplimiento fiscal DGII.