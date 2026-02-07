# 🏦 LoanMaster AI v2.0 — Sistema Integral de Gestión de Préstamos

[![Licencia](https://img.shields.io/badge/Licencia-Privada-red.svg)]()
[![Versión](https://img.shields.io/badge/Versión-2.0-blue.svg)]()
[![Módulos](https://img.shields.io/badge/Módulos-22-green.svg)]()
[![Funciones](https://img.shields.io/badge/Funciones-500%2B-orange.svg)]()

---

## 📌 Descripción

**LoanMaster AI v2.0** es un sistema de inteligencia artificial de nivel empresarial diseñado para la **gestión integral del ciclo de vida de préstamos de dinero**. Cubre desde la prospección del cliente hasta el cierre final y archivo del expediente, operando como el motor inteligente central de una plataforma financiera completa.

Su arquitectura está inspirada en las mejores soluciones open source y comerciales del mercado: **Frappe Lending**, **Apache Fineract**, **Mifos X**, **CredFlow**, **HES LoanBox**, **CreditOnline**, entre otros.

---

## 🏗️ Arquitectura del Sistema

```
LoanMaster AI v2.0
├── 📋 Módulo 1:  Gestión de Clientes (CRM Financiero)
├── 💰 Módulo 2:  Productos de Préstamo
├── 📝 Módulo 3:  Solicitud y Evaluación de Préstamos
├── 🧮 Módulo 4:  Cálculos Financieros
├── 💵 Módulo 5:  Desembolso
├── 📆 Módulo 6:  Gestión de Pagos y Cobros
├── ⚠️ Módulo 7:  Gestión de Morosidad y Cobranza
├── 🔄 Módulo 8:  Refinanciamiento y Reestructuración
├── 🛡️ Módulo 9:  Garantías y Colaterales
├── 📊 Módulo 10: Reportes y Analítica
├── 👥 Módulo 11: Gestión de Usuarios y Roles
├── 🔔 Módulo 12: Notificaciones y Comunicación
├── ⚙️ Módulo 13: Configuración del Sistema
├── 🏪 Módulo 14: Portal de Autoservicio (Cliente)
├── 💼 Módulo 15: Contabilidad e Integración Financiera
├── 🔒 Módulo 16: Prevención de Lavado de Dinero (PLD/FT)
├── 📱 Módulo 17: Aplicación Móvil / Gestión en Campo
├── 🤝 Módulo 18: Préstamos P2P y Grupales
├── 📈 Módulo 19: Inteligencia Artificial y Machine Learning
├── 🌐 Módulo 20: API y Ecosistema Digital
├── 🔐 Módulo 21: Seguridad y Protección de Datos
└── 📋 Módulo 22: Cumplimiento Regulatorio y Auditoría
```

---

## 🌐 Marcos Regulatorios Soportados

| País | Regulador Principal | Tasa de Referencia |
|------|--------------------|--------------------|
| 🇲🇽 México | CNBV / CONDUSEF | TIIE |
| 🇨🇴 Colombia | Superintendencia Financiera | DTF |
| 🇵🇪 Perú | SBS | TAMN/TAMEX |
| 🇪🇨 Ecuador | Superintendencia de Bancos | BCE |
| 🇦🇷 Argentina | BCRA | Badlar |
| 🇨🇱 Chile | CMF | UF |
| 🇩🇴 Rep. Dominicana | SIB | — |
| 🇪🇸 España | Banco de España | Euribor |
| 🇺🇸 Estados Unidos | CFPB | Federal Funds Rate |

---

## 🚀 Características Principales

### Originación y Evaluación Crediticia
- Scoring crediticio interno con sistema de puntos (0-100)
- Consulta automática a burós de crédito
- Evaluación de capacidad de pago con ratio deuda/ingreso
- Flujos de aprobación configurables por monto y riesgo
- Cruce automático contra listas PLD/OFAC/ONU

### Cálculos Financieros Avanzados
- Métodos de amortización: Francés, Alemán, Americano, Flat, Balloon, Irregular
- Frecuencias de pago: Diario, Semanal, Catorcenal, Quincenal, Mensual y más
- Cálculo de CAT, APR, TAE, CFT según regulación por país
- Simulación de escenarios múltiples

### Inteligencia Artificial y Machine Learning
- Scoring crediticio con modelos ML (XGBoost, Random Forest, Neural Networks)
- Predicción de morosidad con Early Warning System
- Optimización de estrategias de cobranza
- Detección de fraude con Graph Analytics
- Chatbot inteligente con NLP y análisis de sentimiento
- Pricing dinámico basado en riesgo

### Cobranza Inteligente
- Clasificación automática por etapas de mora (preventiva → castigo)
- Asignación automática de cartera a cobradores
- App móvil para gestión en campo con geolocalización
- Predicción de probabilidad de recuperación
- Gestión de promesas de pago y acuerdos

### Seguridad Empresarial
- Cifrado AES-256 en reposo y TLS 1.3 en tránsito
- Autenticación multifactor (2FA)
- Control de acceso basado en roles (14 roles predefinidos)
- Auditoría completa de cada operación
- Cumplimiento PLD/FT con cruce de listas internacionales

---

## 📁 Estructura del Repositorio

```
prestamo/
├── README.md
└── docs/
    └── prompt-sistema/
        ├── parte1-modulos-1-8.md        # Módulos 1-8: Core del negocio
        ├── parte2-modulos-9-15.md       # Módulos 9-15: Operaciones y reportes
        └── parte3-modulos-16-22.md      # Módulos 16-22: Seguridad, IA y APIs
```

---

## 📊 Métricas del Prompt

| Métrica | Valor |
|---------|-------|
| Módulos funcionales | 22 |
| Funciones detalladas | 500+ |
| Reglas de negocio críticas | 48 |
| Marcos regulatorios | 9 países |
| Procesos batch automatizados | Diarios, semanales, mensuales, anuales |
| Roles de usuario | 14 predefinidos |
| Canales de comunicación | SMS, Email, WhatsApp, Push, IVR, Carta |
| Métodos de amortización | 6 |

---

## 📏 Reglas de Negocio Críticas (Resumen)

- ❌ **NUNCA** aprobar si ratio deuda/ingreso > 40%
- ❌ **NUNCA** desembolsar sin contrato firmado
- ❌ **NUNCA** exceder tasa máxima legal (usura)
- ✅ **SIEMPRE** aplicar pagos en orden: gastos → moratorios → intereses → capital
- ✅ **SIEMPRE** generar recibo por cada pago
- ✅ **SIEMPRE** registrar auditoría de cada operación
- ✅ **SIEMPRE** cifrar datos sensibles
- ✅ **SIEMPRE** cumplir normativa del país de operación

---

## 🛠️ Tecnologías de Referencia

| Categoría | Tecnologías |
|-----------|-------------|
| Core Banking | Apache Fineract, Mifos X |
| Gestión Empresarial | Frappe Lending, HES LoanBox |
| ML/IA | XGBoost, LightGBM, Random Forest, SHAP |
| Detección Fraude | Graph Analytics (Neo4j) |
| API | REST, OAuth 2.0, JWT, Webhooks, OpenAPI/Swagger |
| Comunicaciones | Twilio, SendGrid, WhatsApp Business API |
| Facturación | CFDI (México), DIAN (Colombia), SUNAT (Perú) |
| Integraciones | Zapier, Power Automate, Make |

---

## 📄 Licencia

Este proyecto es de uso **privado**. Todos los derechos reservados.

---

## 👤 Autor

**bariaspromo** — Sistema diseñado para operaciones de préstamo empresarial.

---

> **📌 Nota:** Este repositorio contiene la documentación del prompt de sistema. La implementación del código fuente se desarrollará de forma progresiva siguiendo la arquitectura de los 22 módulos definidos.