│   ├── OPCIÓN B: Reducir tasa (mantener plazo)
│   │   ├── nueva_tasa
│   │   ├── nueva_cuota
│   │   └── ahorro_total
│   │
│   ├── OPCIÓN C: Capitalizar mora (nuevo préstamo limpio)
│   │   ├── saldo_capital + moratorios + intereses_vencidos = nuevo_monto
│   │   ├── nuevo_plazo
│   │   ├── nueva_tasa
│   │   └── nueva_cuota
│   │
│   ├── OPCIÓN D: Quita + Reestructura
│   │   ├── porcentaje_condonacion_moratorios
│   │   ├── porcentaje_condonacion_intereses
│   │   ├── nuevo_saldo
│   │   ├── nuevo_plazo
│   │   └── nueva_cuota
│   │
│   ├── OPCIÓN E: Pago parcial + Reestructura
│   │   ├── pago_inmediato_requerido (% del vencido)
│   │   ├── nuevo_saldo_restante
│   │   ├── nuevo_plazo
│   │   └── nueva_cuota
│   │
│   └── TABLA COMPARATIVA:
│       ├── opcion | cuota_actual | nueva_cuota | costo_total | ahorro | beneficio_cliente
│       └── recomendacion_sistema basada en perfil_riesgo
│
├── aprobar_refinanciamiento(id_prestamo, opcion_seleccionada, aprobador)
│   ├── niveles_aprobacion:
│   │   ├── quita < 10%: analista_senior
│   │   ├── quita 10-25%: gerente_credito
│   │   ├── quita 25-50%: director_operaciones
│   │   └── quita > 50%: comite_directivo
│   └── registro_justificacion_obligatorio
│
├── ejecutar_refinanciamiento(id_prestamo)
│   ├── cerrar_prestamo_original (estatus: refinanciado)
│   ├── crear_nuevo_prestamo_vinculado
│   ├── transferir_garantias
│   ├── generar_nuevo_contrato
│   ├── generar_nueva_tabla_amortizacion
│   └── actualizar_buro_credito
│
├── generar_nuevo_contrato_refinanciamiento(id_prestamo) → PDF
├── generar_adendum_contrato(id_prestamo, modificaciones) → PDF
│
├── registrar_condonacion_parcial(id_prestamo, detalle)
│   ├── monto_condonado
│   ├── tipo (moratorios/intereses/capital/gastos_cobranza)
│   ├── autorizador
│   ├── justificacion
│   ├── nivel_aprobacion
│   └── impacto_contable
│
├── consolidar_deudas(id_cliente, ids_prestamos[], nuevas_condiciones)
│   ├── sumar_saldos_pendientes
│   ├── calcular_tasa_ponderada o asignar_nueva_tasa
│   ├── definir_nuevo_plazo
│   ├── generar_nuevo_prestamo_consolidado
│   ├── cerrar_prestamos_originales
│   └── generar_contrato_consolidacion
│
├── renovar_prestamo(id_prestamo)
│   ├── validar_prestamo_al_corriente
│   ├── validar_pagos_minimos_realizados (ej: 50% del plazo)
│   ├── liquidar_saldo_actual
│   ├── crear_nuevo_prestamo (monto_original + nuevo_disponible)
│   └── entregar_diferencia_al_cliente
│
├── historial_refinanciamientos(id_cliente)
├── reporte_refinanciamientos(periodo) → montos, frecuencia, efectividad
└── indicador_reincidencia() → clientes que vuelven a caer en mora post-reestructura
```

### 🛡️ MÓDULO 9: GARANTÍAS Y COLATERALES

```
FUNCIONES OBLIGATORIAS:
├── registrar_garantia(id_prestamo, datos_garantia)
│   ├── GARANTÍAS REALES:
│   │   ├── inmueble
│   │   │   ├── tipo (casa/departamento/terreno/local_comercial/bodega/oficina)
│   │   │   ├── direccion_completa
│   │   │   ├── superficie_terreno_m2
│   │   │   ├── superficie_construccion_m2
│   │   │   ├── numero_escritura
│   │   │   ├── notaria
│   │   │   ├── registro_publico_propiedad
│   │   │   ├── folio_real
│   │   │   ├── libre_gravamen (si/no)
│   │   │   ├── valor_catastral
│   │   │   ├── valor_comercial_avaluo
│   │   │   ├── perito_valuador
│   │   │   ├── fecha_avaluo
│   │   │   └── coordenadas_gps
│   │   │
│   │   ├── vehiculo
│   │   │   ├── tipo (auto/camioneta/camion/motocicleta/maquinaria)
│   │   │   ├── marca
│   │   │   ├── modelo
│   │   │   ├── año
│   │   │   ├── numero_serie (VIN)
│   │   │   ├── numero_motor
│   │   │   ├── placas
│   │   │   ├── tarjeta_circulacion
│   │   │   ├── factura_original (si/no)
│   │   │   ├── valor_factura
│   │   │   ├── valor_comercial_libro_azul
│   │   │   ├── valor_avaluo
│   │   │   ├── poliza_seguro
│   │   │   └── endoso_aseguradora
│   │   │
│   │   ├── deposito_garantia_liquida
│   │   │   ├── monto_deposito
│   │   │   ├── cuenta_restringida
│   │   │   ├── tasa_rendimiento
│   │   │   └── plazo_bloqueo
│   │   │
│   │   ├── inventario_o_mercancia
│   │   │   ├── descripcion
│   │   │   ├── valor_estimado
│   │   │   ├── ubicacion_almacen
│   │   │   └── poliza_seguro
│   │   │
│   │   └── maquinaria_equipo
│   │       ├── descripcion
│   │       ├── marca_modelo_serie
│   │       ├── valor_adquisicion
│   │       ├── depreciacion_acumulada
│   │       └── valor_actual_avaluo
│   │
│   ├── GARANTÍAS PERSONALES:
│   │   ├── aval_persona_fisica
│   │   │   ├── datos_personales_completos
│   │   │   ├── datos_laborales
│   │   │   ├── ingresos_comprobables
│   │   │   ├── bienes_declarados[]
│   │   │   ├── deudas_declaradas[]
│   │   │   ├── consulta_buro
│   │   │   └── firma_obligacion_solidaria
│   │   │
│   │   ├── aval_persona_moral
│   │   │   ├── razon_social
│   │   │   ├── rfc
│   │   │   ├── representante_legal
│   │   │   ├── acta_constitutiva
│   │   │   ├── poder_notarial
│   │   │   ├── estados_financieros
│   │   │   └── firma_obligacion_solidaria
│   │   │
│   │   └── obligado_solidario
│   │       ├── datos_completos
│   │       └── nivel_responsabilidad (solidario/subsidiario)
│   │
│   ├── GARANTÍAS FIDUCIARIAS:
│   │   ├── fideicomiso_garantia
│   │   │   ├── numero_fideicomiso
│   │   │   ├── fiduciario (banco)
│   │   │   ├── bienes_fideicomitidos[]
│   │   │   └── contrato_fideicomiso
│   │   │
│   │   └── cesion_derechos
│   │       ├── tipo_derechos (cuentas_cobrar/contratos/seguros)
│   │       ├── valor_estimado
│   │       └── contrato_cesion
│   │
│   ├── valor_total_garantias
│   ├── porcentaje_cobertura = valor_garantias / monto_prestamo × 100
│   ├── documentos_soporte[]
│   ├── estado_legal (libre/gravado/en_proceso/ejecutable)
│   └── fecha_registro
│
├── actualizar_avaluo(id_garantia, nuevo_avaluo)
│   ├── perito_valuador
│   ├── fecha_avaluo
│   ├── valor_anterior
│   ├── valor_nuevo
│   ├── motivo_revaluacion
│   └── recalcular_cobertura()
│
├── monitorear_vigencia_avaluos()
│   ├── alertar: avaluos > 1 año antigüedad
│   └── programar_revaluacion()
│
├── monitorear_seguros_garantias()
│   ├── alertar: polizas próximas a vencer
│   ├── verificar_endoso_vigente
│   └── exigir_renovacion
│
├── verificar_cobertura_cartera()
│   ├── total_cartera_vs_total_garantias
│   ├── prestamos_sin_cobertura_suficiente
│   └── recomendaciones_accion
│
├── liberar_garantia(id_garantia, id_prestamo_pagado)
│   ├── verificar_prestamo_liquidado
│   ├── generar_carta_liberacion() → PDF
│   ├── cancelar_gravamen_registro_publico
│   ├── devolver_documentos_originales
│   └── actualizar_estatus_garantia
│
├── ejecutar_garantia(id_garantia, proceso)
│   ├── iniciar_proceso_legal
│   ├── solicitar_embargo
│   ├── proceso_remate (si aplica)
│   ├── adjudicacion
│   ├── venta_bien_adjudicado
│   ├── aplicar_producto_a_deuda
│   └── devolver_remanente_al_deudor
│
├── transferir_garantia(id_garantia, id_prestamo_origen, id_prestamo_destino)
│   └── Para refinanciamientos o consolidaciones
│
├── sustituir_garantia(id_garantia_actual, datos_nueva_garantia)
│   ├── verificar_equivalencia_valor
│   └── aprobar_sustitucion
│
├── reporte_garantias()
│   ├── cobertura_total_cartera
│   ├── por_tipo_garantia
│   ├── avaluos_vencidos
│   ├── seguros_por_vencer
│   └── garantias_en_proceso_ejecucion
│
└── inventario_bienes_adjudicados()
    ├── bienes_en_custodia
    ├── bienes_en_proceso_venta
    ├── valor_total_adjudicados
    └── antiguedad_promedio
```

### 📊 MÓDULO 10: REPORTES Y ANALÍTICA

```
FUNCIONES OBLIGATORIAS:
├── REPORTES OPERATIVOS (diarios):
│   ├── reporte_desembolsos_dia()
│   ├── reporte_pagos_dia()
│   ├── reporte_mora_dia() → nuevos morosos
│   ├── reporte_gestiones_cobranza_dia()
│   ├── corte_caja_dia(sucursal)
│   ├── conciliacion_bancaria_dia()
│   └── reporte_vencimientos_mañana()
│
├── REPORTES DE CARTERA (semanales/mensuales):
│   ├── reporte_cartera_activa()
│   │   ├── total_colocado
│   │   ├── numero_prestamos_activos
│   │   ├── por_producto
│   │   ├── por_sucursal
│   │   ├── por_promotor
│   │   ├── por_zona_geografica
│   │   ├── por_moneda
│   │   └── crecimiento_vs_periodo_anterior
│   │
│   ├── reporte_morosidad()
│   │   ├── cartera_vigente
│   │   ├── cartera_vencida (por rangos: 1-30, 31-60, 61-90, 91-120, 121-180, >180)
│   │   ├── indice_morosidad = cartera_vencida / cartera_total × 100
│   │   ├── indice_mora_ajustado = (vencida + castigada) / (total + castigada) × 100
│   │   ├── por_producto
│   │   ├── por_sucursal
│   │   ├── por_cosecha (mes de desembolso)
│   │   ├── por_analista_que_aprobó
│   │   ├── por_promotor_que_colocó
│   │   ├── tendencia_12_meses
│   │   └── comparativa_mismo_periodo_año_anterior
│   │
│   ├── reporte_cobranza(periodo)
│   │   ├── monto_recuperado
│   │   ├── tasa_recuperacion
│   │   ├── eficiencia_por_cobrador
│   │   ├── eficiencia_por_canal (llamada/visita/sms/legal)
│   │   ├── costo_cobranza
│   │   ├── costo_por_peso_recuperado
│   │   ├── promesas_cumplidas_vs_incumplidas
│   │   └── cartera_migrada_entre_rangos (roll_rates)
│   │
│   ├── reporte_desembolsos(periodo)
│   │   ├── total_desembolsado
│   │   ├── numero_operaciones
│   │   ├── ticket_promedio
│   │   ├── plazo_promedio
│   │   ├── tasa_promedio_ponderada
│   │   ├── por_producto
│   │   ├── por_sucursal
│   │   ├── por_promotor
│   │   ├── por_canal_captacion
│   │   └── meta_vs_logro
│   │
│   ├── reporte_rentabilidad()
│   │   ├── ingresos_intereses_ordinarios
│   │   ├── ingresos_intereses_moratorios
│   │   ├── ingresos_comisiones
│   │   ├── (-) gasto_fondeo
│   │   ├── (-) provision_cartera
│   │   ├── (-) castigos
│   │   ├── (-) gastos_operativos
│   │   ├── (-) gastos_cobranza
│   │   ├── (=) utilidad_neta_cartera
│   │   ├── ROA = utilidad / activos_promedio
│   │   ├── ROE = utilidad / capital
│   │   ├── margen_financiero = (ingresos_int - gasto_fondeo) / cartera_promedio
│   │   ├── spread = tasa_activa_promedio - costo_fondeo_promedio
│   │   └── por_producto / por_sucursal
│   │
│   └── reporte_provision_cartera()
│       ├── clasificacion_cartera
│       │   ├── normal (al_corriente): provision 0-1%
│       │   ├── con_riesgo_potencial (1-30 días): provision 1-5%
│       │   ├── substandard (31-60 días): provision 10-25%
│       │   ├── dudoso (61-120 días): provision 25-50%
│       │   ├── perdida (121-365 días): provision 50-100%
│       │   └── irrecuperable (>365 días): provision 100%
│       │
│       ├── provision_total_requerida
│       ├── provision_actual_registrada
│       ├── exceso_o_insuficiencia
│       └── ajuste_contable_requerido
│
├── REPORTES DE GESTIÓN (mensuales):
│   ├── reporte_concentracion()
│   │   ├── por_cliente (top 10, top 50)
│   │   ├── por_sector_economico
│   │   ├── por_zona_geografica
│   │   ├── HHI (Herfindahl-Hirschman Index)
│   │   └── alertas_concentracion_excesiva
│   │
│   ├── reporte_originacion()
│   │   ├── solicitudes_recibidas
│   │   ├── solicitudes_aprobadas (tasa_aprobacion)
│   │   ├── solicitudes_rechazadas (motivos_principales)
│   │   ├── tiempo_promedio_respuesta
│   │   ├── embudo_conversion: solicitud→evaluacion→aprobacion→desembolso
│   │   └── abandono_por_etapa
│   │
│   ├── reporte_productos()
│   │   ├── penetracion_por_producto
│   │   ├── rentabilidad_por_producto
│   │   ├── morosidad_por_producto
│   │   └── recomendaciones_ajuste
│   │
│   └── reporte_sucursales()
│       ├── colocacion_por_sucursal
│       ├── cartera_por_sucursal
│       ├── morosidad_por_sucursal
│       ├── eficiencia_por_sucursal
│       └── ranking_sucursales
│
├── REPORTES REGULATORIOS:
│   ├── reporte_R04_CNBV() // México: Cartera de crédito
│   ├── reporte_R12_CNBV() // México: Calificación de cartera
│   ├── reporte_PLD() // Prevención lavado de dinero
│   ├── reporte_operaciones_relevantes() // > umbral regulatorio
│   ├── reporte_operaciones_inusuales()
│   ├── reporte_tasas_promedio_ponderadas()
│   ├── reporte_CAT_por_producto()
│   ├── reporte_quejas_CONDUSEF()
│   └── generar_formato_regulatorio(tipo, periodo) → XML/JSON/XBRL
│
├── DASHBOARD EJECUTIVO (tiempo real):
│   ├── cartera_total
│   ├── cartera_vigente / cartera_vencida
│   ├── indice_morosidad (gauge)
│   ├── desembolsos_mes_actual vs meta
│   ├── cobranza_mes_actual vs meta
│   ├── flujo_neto = desembolsos - pagos
│   ├── provisiones
│   ├── ROA / ROE (trend)
│   ├── clientes_activos
│   ├── tasa_aprobacion (trend)
│   ├── ticket_promedio
│   ├── dias_promedio_mora
│   ├── cosecha_mas_reciente_morosidad
│   ├── mapa_calor_por_zona
│   ├── alertas_criticas
│   └── predicciones_ML (cartera_esperada_30_60_90_dias)
│
├── ANALÍTICA AVANZADA:
│   ├── analisis_cosechas(vintage_analysis)
│   │   └── morosidad_por_mes_de_desembolso a lo largo del tiempo
│   ├── analisis_roll_rates()
│   │   └── migración de cartera entre rangos de mora
│   ├── analisis_survival() → curva de supervivencia de préstamos
│   ├── modelo_expected_loss() → pérdida esperada = PD × LGD × EAD
│   ├── stress_testing(escenarios[])
│   │   ├── escenario_base
│   │   ├── escenario_adverso (recesión leve)
│   │   ├── escenario_severamente_adverso (crisis)
│   │   └── impacto_en: morosidad, provisiones, capital
│   ├── backtesting_modelos_scoring() → validación de modelos
│   ├── analisis_elasticidad_tasa() → cómo cambia demanda según tasa
│   ├── analisis_canibalización_productos()
│   └── prediccion_demanda_credito(horizonte_meses)
│
├── EXPORTACIÓN:
│   ├── exportar_reporte(formato: PDF/Excel/CSV/JSON/XML/XBRL)
│   ├── programar_reportes_automaticos(frecuencia, hora, destinatarios[], formato)
│   ├── enviar_reporte_por_email(id_reporte, destinatarios[])
│   └── API_reportes() → endpoints para BI externo (PowerBI/Tableau/Metabase)
│
└── AUDITORÍA DE REPORTES:
    ├── registrar_quien_genero(id_reporte, usuario, timestamp)
    ├── registrar_quien_descargo(id_reporte, usuario, timestamp)
    └── versionado_reportes() → mantener histórico
```

### 👥 MÓDULO 11: GESTIÓN DE USUARIOS Y ROLES

```
FUNCIONES OBLIGATORIAS:
├── crear_usuario(datos)
│   ├── nombre_completo
│   ├── email_corporativo
│   ├── telefono
│   ├── sucursal_asignada
│   ├── departamento
│   ├── puesto
│   ├── jefe_directo
│   ├── fecha_ingreso
│   ├── foto_perfil
│   └── estado (activo/inactivo/suspendido)
│
├── asignar_rol(id_usuario, rol)
│   ├── SUPER_ADMIN
│   │   ├── acceso: TOTAL sin restricciones
│   │   ├── puede: configurar sistema, crear roles, ver auditoría
│   │   └── restriccion: máximo 2 usuarios con este rol
│   │
│   ├── DIRECTOR_GENERAL
│   │   ├── acceso: dashboards ejecutivos, reportes consolidados
│   │   ├── puede: aprobar excepciones, definir políticas
│   │   └── no_puede: operar directamente
│   │
│   ├── GERENTE_CREDITO
│   │   ├── acceso: solicitudes, aprobaciones, reportes de cartera
│   │   ├── puede: aprobar préstamos hasta su límite, asignar analistas
│   │   ├── limites: monto_max_aprobacion, quita_max_autorizable
│   │   └── no_puede: configurar sistema
│   │
│   ├── GERENTE_COBRANZA
│   │   ├── acceso: módulo cobranza completo, reportes mora
│   │   ├── puede: aprobar acuerdos_pago, asignar cartera, condonar_parcial
│   │   ├── limites: condonacion_max, descuento_max
│   │   └── no_puede: aprobar préstamos
│   │
│   ├── ANALISTA_CREDITO
│   │   ├── acceso: solicitudes asignadas, consulta buró, evaluación
│   │   ├── puede: evaluar, recomendar, aprobar (según límite)
│   │   ├── limites: monto_max_aprobacion
│   │   └── no_puede: desembolsar, reversar pagos
│   │
│   ├── PROMOTOR_VENTAS
│   │   ├── acceso: captura solicitudes, consulta clientes propios
│   │   ├── puede: registrar clientes, capturar solicitudes
│   │   └── no_puede: aprobar, evaluar, ver cartera ajena
│   │
│   ├── CAJERO
│   │   ├── acceso: módulo pagos, desembolsos
│   │   ├── puede: registrar pagos, ejecutar desembolsos aprobados
│   │   ├── limites: monto_max_efectivo_dia
│   │   └── no_puede: reversar pagos (requiere supervisor)
│   │
│   ├── COBRADOR_TELEFONICO
│   │   ├── acceso: cartera asignada, gestiones, promesas
│   │   ├── puede: registrar gestiones, programar recordatorios
│   │   └── no_puede: ofrecer quitas, modificar montos
│   │
│   ├── COBRADOR_CAMPO
│   │   ├── acceso: cartera asignada (app móvil), rutas
│   │   ├── puede: gestionar, recibir pagos campo, geolocalización
│   │   └── no_puede: ofrecer quitas sin autorización
│   │
│   ├── CONTADOR
│   │   ├── acceso: módulo contable, provisiones, conciliación
│   │   ├── puede: registrar provisiones, generar pólizas contables
│   │   └── no_puede: operar préstamos
│   │
│   ├── LEGAL
│   │   ├── acceso: expedientes legales, garantías, demandas
│   │   ├── puede: gestionar procesos legales, ejecución garantías
│   │   └── no_puede: modificar condiciones financieras
│   │
│   ├── AUDITOR
│   │   ├── acceso: SOLO LECTURA a TODO el sistema
│   │   ├── puede: generar reportes, consultar auditoría, exportar
│   │   └── no_puede: crear/modificar/eliminar NADA
│   │
│   ├── COMPLIANCE / PLD
│   │   ├── acceso: módulo PLD, listas, alertas, reportes regulatorios
│   │   ├── puede: bloquear cuentas sospechosas, generar ROS
│   │   └── no_puede: operar préstamos
│   │
│   └── CLIENTE (portal autoservicio)
│       ├── acceso: solo sus datos, sus préstamos, sus pagos
│       ├── puede: consultar, pagar online, solicitar, subir documentos
│       └── no_puede: ver datos de otros clientes ni operar backend
│
├── configurar_permisos_granulares(rol, permisos[])
│   ├── por_modulo: [crear, leer, actualizar, eliminar, exportar, imprimir]
│   ├── por_sucursal: restricción geográfica
│   ├── por_producto: solo productos asignados
│   ├── por_monto: límites de operación
│   └── por_horario: horarios permitidos
│
├── crear_rol_personalizado(nombre, descripcion, permisos[])
├── duplicar_rol(id_rol_base, nombre_nuevo)
│
├── registrar_auditoria(evento) → AUTOMÁTICO en CADA acción
│   ├── timestamp
│   ├── usuario_id
│   ├── nombre_usuario
│   ├── rol_usuario
│   ├── sucursal
│   ├── ip_address
│   ├── user_agent
│   ├── modulo
│   ├── accion (crear/leer/actualizar/eliminar/aprobar/reversar/exportar/login/logout)
│   ├── entidad_afectada (cliente/prestamo/pago/etc)
│   ├── id_entidad
│   ├── datos_anteriores (JSON snapshot)
│   ├── datos_nuevos (JSON snapshot)
│   ├── resultado (exitoso/fallido/denegado)
│   └── motivo_si_fallido
│
├── consultar_auditoria(filtros) → búsqueda avanzada con todos los campos
├── exportar_auditoria(filtros, formato)
├── alertas_auditoria()
│   ├── múltiples intentos fallidos login
│   ├── accesos fuera de horario
│   ├── operaciones inusuales (monto, frecuencia)
│   ├── acceso a datos no propios de su cartera
│   └── exportaciones masivas de datos
│
├── listar_actividad_usuario(id_usuario, periodo)
├── sesiones_activas() → quién está conectado ahora
├── forzar_logout(id_usuario, motivo)
├── bloquear_usuario(id, motivo, duracion)
├── desbloquear_usuario(id, autorizador)
├── resetear_contraseña(id)
├── configurar_politica_contraseñas()
│   ├── longitud_minima: 12
│   ├── requiere_mayuscula: si
│   ├── requiere_minuscula: si
│   ├── requiere_numero: si
│   ├── requiere_simbolo: si
│   ├── no_reutilizar_ultimas: 5
│   ├── expiracion_dias: 90
│   └── bloqueo_intentos_fallidos: 5
│
├── configurar_2FA(id_usuario)
│   ├── TOTP (Google Authenticator / Authy)
│   ├── SMS
│   ├── Email
│   └── Biometría (huella / facial)
│
├── configurar_SSO() → integración Single Sign-On
├── configurar_LDAP() → integración directorio corporativo
└── reporte_accesos_y_permisos() → matriz usuario × permiso
```

### 🔔 MÓDULO 12: NOTIFICACIONES Y COMUNICACIÓN

```
FUNCIONES OBLIGATORIAS:
├── CANALES DE COMUNICACIÓN:
│   ├── enviar_sms(destinatario, mensaje, template_id)
│   │   ├── proveedor: Twilio / Clickatell / Nexmo / local
│   │   ├── limite: 160 caracteres (o concatenar)
│   │   ├── registro_entrega: enviado/entregado/fallido
│   │   └── opt_out: respetar solicitudes de no recibir SMS
│   │
│   ├── enviar_email(destinatario, asunto, cuerpo_html, adjuntos[])
│   │   ├── proveedor: SendGrid / SES / SMTP propio
│   │   ├── template_html responsive
│   │   ├── tracking: apertura, clicks
│   │   ├── bounce_handling
│   │   └── unsubscribe_link
│   │
│   ├── enviar_whatsapp(destinatario, mensaje, template_aprobado)
│   │   ├── proveedor: WhatsApp Business API / Twilio
│   │   ├── templates pre-aprobados por Meta
│   │   ├── mensajes_interactivos (botones, listas)
│   │   ├── envio_documentos (recibos, estados cuenta)
│   │   └── chatbot_respuesta_automatica
│   │
│   ├── enviar_notificacion_push(id_usuario, titulo, mensaje, accion)
│   │   ├── Firebase Cloud Messaging (Android)
│   │   ├── Apple Push Notification (iOS)
│   │   └── Web Push
│   │
│   ├── llamada_automatizada(destinatario, mensaje_audio)
│   │   ├── IVR con opciones (presione 1 para...)
│   │   ├── grabación de respuesta
│   │   └── transferencia a agente si requiere
│   │
│   └── carta_fisica(destinatario, contenido) → PDF para impresión
│       ├── carta_simple
│       ├── carta_certificada
│       └── notificación_notarial
│
├── TEMPLATES DE NOTIFICACIÓN (personalizables):
│   ├── CICLO DE VIDA DEL PRÉSTAMO:
│   │   ├── bienvenida_cliente
│   │   │   └── "¡Bienvenido {nombre}! Tu cuenta ha sido creada..."
│   │   ├── solicitud_recibida
│   │   │   └── "Tu solicitud {num_solicitud} ha sido recibida. Tiempo estimado: {dias} días"
│   │   ├── documentos_pendientes
│   │   │   └── "Para continuar con tu solicitud necesitamos: {lista_documentos}"
│   │   ├── solicitud_en_evaluacion
│   │   │   └── "Tu solicitud está siendo evaluada por nuestro equipo"
│   │   ├── solicitud_aprobada
│   │   │   └── "¡Felicidades! Tu préstamo por {monto} ha sido aprobado. Tasa: {tasa}%, Cuota: {cuota}"
│   │   ├── solicitud_rechazada
│   │   │   └── "Lamentamos informarte que tu solicitud no fue aprobada. Motivo: {motivo}. Recomendaciones: {recomendaciones}"
│   │   ├── contraoferta
│   │   │   └── "Te ofrecemos una alternativa: {monto_nuevo} a {plazo_nuevo} meses..."
│   │   ├── desembolso_realizado
│   │   │   └── "Se han depositado {monto_neto} en tu cuenta {cuenta}. Tu primera cuota vence el {fecha}"
│   │   ├── primer_cuota_proxima
│   │   │   └── "Tu primera cuota de {monto} vence el {fecha}. ¡No olvides tenerla lista!"
│   │   └── prestamo_liquidado
│   │       └── "¡Felicidades! Has liquidado tu préstamo {num}. Tu carta de no adeudo está disponible"
│   │
│   ├── RECORDATORIOS DE PAGO:
│   │   ├── recordatorio_5_dias_antes
│   │   │   └── "Recordatorio: tu cuota #{num} de {monto} vence el {fecha}"
│   │   ├── recordatorio_3_dias_antes
│   │   │   └── "En 3 días vence tu cuota. Monto: {monto}. Paga fácil en: {link_pago}"
│   │   ├── recordatorio_1_dia_antes
│   │   │   └── "⚠️ MAÑANA vence tu cuota de {monto}. Evita recargos pagando hoy"
│   │   ├── dia_vencimiento
│   │   │   └── "HOY es tu fecha de pago. Cuota: {monto}. Paga aquí: {link}"
│   │   └── confirmacion_pago
│   │       └── "✅ Pago recibido por {monto}. Folio: {folio}. Nuevo saldo: {saldo}. Próxima cuota: {fecha}"
│   │
│   ├── COBRANZA (progresivo):
│   │   ├── mora_dia_1
│   │   │   └── "Tu pago de {monto} venció ayer. Realízalo hoy para evitar intereses moratorios"
│   │   ├── mora_dia_3
│   │   │   └── "Tienes {dias} días de atraso. Has acumulado {moratorios} en recargos. Paga ahora: {link}"
│   │   ├── mora_dia_7
│   │   │   └── "AVISO IMPORTANTE: Tu cuenta tiene {dias} días de atraso. Monto adeudado: {total}. Contáctanos: {telefono}"
│   │   ├── mora_dia_15
│   │   │   └── "SEGUNDO AVISO: {dias} días de mora. Total: {total}. Es importante regularizar tu situación. Opciones: {opciones}"
│   │   ├── mora_dia_30
│   │   │   └── "AVISO FORMAL: Llevas {dias} días de atraso en tu préstamo {num}. Notificamos a tu(s) aval(es). Comunícate al {telefono}"
│   │   ├── mora_dia_60_prejudicial
│   │   │   └── "CARTA PREJUDICIAL: De no recibir tu pago en {dias_plazo} días, procederemos con acciones legales..."
│   │   └── mora_dia_90_ultima_oportunidad
│   │       └── "ÚLTIMA OPORTUNIDAD: Antes de proceder legalmente, te ofrecemos un plan especial: {plan}. Responde antes del {fecha}"
│   │
│   ├── MARKETING Y RETENCIÓN:
│   │   ├── oferta_nuevo_prestamo
│   │   │   └── "Tienes pre-aprobado un crédito de hasta {monto} con tasa preferencial de {tasa}%"
│   │   ├── felicitacion_buen_pagador
│   │   │   └── "¡Eres un cliente estrella! Gracias por tus pagos puntuales. Te hemos mejorado tu línea..."
│   │   ├── felicitacion_cumpleaños
│   │   │   └── "¡Feliz cumpleaños {nombre}! Como regalo, te ofrecemos..."
│   │   ├── encuesta_satisfaccion
│   │   │   └── "¿Cómo fue tu experiencia? Ayúdanos a mejorar: {link_encuesta}"
│   │   ├── referidos
│   │   │   └── "Recomienda a un amigo y gana {beneficio}. Tu código: {codigo}"
│   │   └── reactivacion_cliente_inactivo
│   │       └── "¡Te extrañamos! Tenemos nuevos productos especiales para ti..."
│   │
│   └── OPERATIVAS INTERNAS:
│       ├── alerta_solicitud_nueva (para analista)
│       ├── alerta_solicitud_pendiente_aprobacion (para gerente)
│       ├── alerta_pago_recibido (para cobrador asignado)
│       ├── alerta_promesa_vencida (para cobrador)
│       ├── alerta_cliente_nueva_mora (para cobrador)
│       ├── alerta_limite_aprobacion_excedido
│       ├── alerta_pld_operacion_inusual
│       └── alerta_sistema (errores, caídas, backups)
│
├── PROGRAMACIÓN Y AUTOMATIZACIÓN:
│   ├── programar_notificacion(tipo, destinatario, fecha_hora, canal, mensaje)
│   ├── crear_campaña_masiva(segmento, canal, template, fecha_envio)
│   ├── configurar_reglas_automaticas()
│   │   ├── trigger: evento → acción
│   │   ├── ej: "al_desembolsar" → enviar_email_bienvenida + sms_confirmacion
│   │   ├── ej: "dia_antes_vencimiento" → enviar_recordatorio
│   │   └── ej: "al_recibir_pago" → enviar_recibo
│   ├── cola_mensajes() → gestión de envíos pendientes
│   ├── reintentar_fallidos(max_intentos, intervalo)
│   └── horarios_permitidos_envio(canal) // No enviar SMS después de 9pm
│
├── HISTORIAL Y ESTADÍSTICAS:
│   ├── historial_comunicaciones(id_cliente) → timeline completo
│   ├── estadisticas_comunicacion(periodo)
│   │   ├── total_enviados_por_canal
│   │   ├── tasa_entrega
│   │   ├── tasa_apertura (email)
│   │   ├── tasa_click (email)
│   │   ├── tasa_respuesta (whatsapp)
│   │   ├── tasa_conversion (acción deseada)
│   │   ├── costo_por_canal
│   │   ├── mejor_horario_apertura
│   │   └── templates_mas_efectivos
│   │
│   └── A_B_testing(template_A, template_B, segmento, metrica_objetivo)
│
└── CUMPLIMIENTO:
    ├── gestionar_opt_out(id_cliente, canal) // Derecho a no ser contactado
    ├── registro_consentimiento_comunicaciones()
    ├── lista_robinson() // No contactar
    └── cumplimiento_horarios_cobranza() // Marco regulatorio de cada país
```

### ⚙️ MÓDULO 13: CONFIGURACIÓN DEL SISTEMA

```
FUNCIONES OBLIGATORIAS:
├── configurar_empresa(datos_empresa)
│   ├── razon_social
│   ├── nombre_comercial
│   ├── rfc_ruc_nit
│   ├── direccion_fiscal
│   ├── telefono_principal
│   ├── email_oficial
│   ├── sitio_web
│   ├── logo (diferentes resoluciones)
│   ├── tipo_entidad (banco/financiera/SOFOM/cooperativa/fintech/persona_fisica)
│   ├── numero_licencia_regulatoria
│   ├── organo_regulador
│   ├── representante_legal
│   ├── datos_notariales_constitucion
│   └── datos_fiscales_facturacion
│
├── configurar_sucursales()
│   ├── crear_sucursal(nombre, direccion, gerente, horario, telefono)
│   ├── modificar_sucursal()
│   ├── desactivar_sucursal()
│   └── asignar_usuarios_sucursal()
│
├── configurar_parametros_financieros()
│   ├── moneda_principal
│   ├── monedas_secundarias[]
│   ├── tipo_cambio_actualizacion (manual/automatico/API_banco_central)
│   ├── dias_laborables (L-V / L-S / personalizado)
│   ├── calendario_feriados[] // Por país/región
│   ├── dias_año_calculo (360/365/actual)
│   ├── convencion_dias_mes (30/actual)
│   ├── tasa_referencia_mercado (TIIE/DTF/TAMN/etc)
│   ├── tasa_referencia_valor_actual
│   ├── tasa_referencia_actualizacion (manual/automatica)
│   ├── redondeo_centavos (truncar/redondear/al_peso)
│   ├── IVA_porcentaje (16% México / 19% Colombia / etc)
│   ├── IVA_aplica_a_intereses (si/no según regulación)
│   ├── IVA_aplica_a_comisiones (si/no)
│   ├── IVA_aplica_a_moratorios (si/no)
│   ├── tasa_maxima_legal (usura) → bloquear configuración superior
│   └── monto_maximo_efectivo (PLD) → alertar si se excede
│
├── configurar_provision_cartera()
│   ├── METODOLOGÍA ESTÁNDAR (por días de mora):
│   │   ├── normal: 0 días → 0-1%
│   │   ├── vigilancia_especial: 1-30 días → 1-5%
│   │   ├── subnormal: 31-60 días → 5-25%
│   │   ├── dudoso: 61-120 días → 25-50%
│   │   ├── pérdida: 121-365 días → 50-100%
│   │   └── castigo: > 365 días → 100% (write-off contable)
│   │
│   ├── METODOLOGÍA PÉRDIDA ESPERADA (avanzada):
│   │   ├── PD (Probability of Default) por scoring
│   │   ├── LGD (Loss Given Default) por tipo garantía
│   │   ├── EAD (Exposure at Default)
│   │   └── PE = PD × LGD × EAD
│   │
│   └── frecuencia_calculo (diario/semanal/mensual)
│
├── configurar_contabilidad()
│   ├── plan_cuentas_contable
│   │   ├── cartera_vigente
│   │   ├── cartera_vencida
│   │   ├── intereses_por_cobrar
│   │   ├── intereses_moratorios_por_cobrar
│   │   ├── comisiones_por_cobrar
│   │   ├── provision_cartera (contra-activo)
│   │   ├── ingresos_intereses
│   │   ├── ingresos_comisiones
│   │   ├── ingresos_moratorios
│   │   ├── gasto_provision
│   │   ├── castigos
│   │   └── recuperacion_cartera_castigada
│   │
│   ├── polizas_automaticas()
│   │   ├── al_desembolsar → cargo cartera_vigente, abono bancos
│   │   ├── al_devengar_intereses → cargo int_por_cobrar, abono ingreso_int
│   │   ├── al_recibir_pago → cargo bancos, abono cartera + int_cobrar
│   │   ├── al_vencer_cuota → cargo cartera_vencida, abono cartera_vigente
│   │   ├── al_provisionar → cargo gasto_provision, abono provision
│   │   ├── al_castigar → cargo castigo + provision, abono cartera
│   │   └── al_recuperar_castigado → cargo bancos, abono ingreso_extraordinario
│   │
│   └── integracion_sistema_contable (SAP/QuickBooks/CONTPAQi/Alegra/etc)
│
├── configurar_integraciones()
│   ├── BURÓ DE CRÉDITO:
│   │   ├── proveedor (Buró de Crédito MX / TransUnion / Experian / Equifax)
│   │   ├── credenciales_API
│   │   ├── frecuencia_consulta
│   │   └── costo_por_consulta
│   │
│   ├── PASARELA DE PAGO:
│   │   ├── proveedor (Stripe/MercadoPago/PayPal/Conekta/OpenPay/SPEI)
│   │   ├── credenciales_API
│   │   ├── webhook_confirmacion
│   │   └── comisiones
│   │
│   ├── BANCA / CORE BANCARIO:
│   │   ├── banco_dispersor (para desembolsos masivos)
│   │   ├── SPEI/ACH (transferencias interbancarias)
│   │   ├── domiciliacion_bancaria
│   │   └── conciliacion_automatica
│   │
│   ├── COMUNICACIONES:
│   │   ├── SMS: Twilio / Clickatell / proveedor_local
│   │   ├── Email: SendGrid / Amazon SES / SMTP
│   │   ├── WhatsApp: Business API / Twilio
│   │   └── Push: Firebase / OneSignal
│   │
│   ├── ALMACENAMIENTO:
│   │   ├── documentos: AWS S3 / Google Cloud Storage / Azure Blob
│   │   ├── firma_electronica: DocuSign / Adobe Sign / proveedor_local
│   │   └── backup: automatizado + cifrado
│   │
│   ├── GEOLOCALIZACIÓN:
│   │   ├── Google Maps API
│   │   └── geocodificación de direcciones
│   │
│   ├── FACTURACIÓN ELECTRÓNICA:
│   │   ├── PAC (México): Finkok / Facturama
│   │   └── DIAN (Colombia) / SUNAT (Perú) / SII (Chile)
│   │
│   └── IDENTIDAD DIGITAL:
│       ├── INE/IFE validación (México)
│       ├── RENIEC (Perú)
│       ├── CURP validación
│       └── OCR documentos
│
├── configurar_workflows_aprobacion()
│   ├── REGLA 1: monto <= $50,000 AND scoring >= 75 → APROBACIÓN_AUTOMÁTICA
│   ├── REGLA 2: monto <= $50,000 AND scoring 55-74 → UN_APROBADOR (analista_senior)
│   ├── REGLA 3: monto $50,001-$200,000 → UN_APROBADOR (gerente_credito)
│   ├── REGLA 4: monto $200,001-$500,000 → DOS_APROBADORES (gerente + director)
│   ├── REGLA 5: monto > $500,000 → COMITÉ_CRÉDITO (mínimo 3 votos)
│   ├── REGLA 6: excepciones_politica → COMITÉ_CRÉDITO + justificación
│   ├── REGLA 7: clientes_vinculados → aprobación_nivel_superior
│   └── personalizar_reglas(condiciones[], aprobadores[], escalamiento)
│
├── configurar_numeracion_automatica()
│   ├── formato_solicitudes: SOL-{YYYY}-{NNNNN}
│   ├── formato_prestamos: PRE-{YYYY}-{NNNNN}
│   ├── formato_pagos: PAG-{YYYY}-{NNNNN}
│   ├── formato_contratos: CON-{YYYY}-{NNNNN}
│   └── formato_recibos: REC-{YYYY}-{NNNNN}
│
├── configurar_horarios_operacion()
│   ├── horario_atencion_publico
│   ├── horario_operaciones_sistema
│   ├── horario_procesos_batch
│   └── horario_cobranza_permitido
│
├── configurar_limites_operativos()
│   ├── limite_desembolso_diario_por_sucursal
│   ├── limite_desembolso_diario_por_usuario
│   ├── limite_efectivo_sin_reporte_pld
│   ├── limite_reversos_diarios
│   └── limite_consultas_buro_diarias
│
├── backup_sistema()
│   ├── backup_completo (diario, automático)
│   ├── backup_incremental (cada 6 horas)
│   ├── almacenamiento_externo (nube)
│   ├── verificar_integridad_backup()
│   ├── prueba_restauracion (mensual)
│   └── retencion: 7 años mínimo (regulatorio)
│
├── configurar_alertas_sistema()
│   ├── espacio_disco < 20%
│   ├── cpu > 90% sostenido
│   ├── error_rate > umbral
│   ├── integracion_caida
│   ├── backup_fallido
│   └── certificado_ssl_proximo_vencer
│
└── log_cambios_configuracion()
    ├── quien_cambio
    ├── que_cambio
    ├── valor_anterior
    ├── valor_nuevo
    └── fecha_hora
```

### 🏪 MÓDULO 14: PORTAL DE AUTOSERVICIO (CLIENTE)

```
FUNCIONES OBLIGATORIAS:
├── AUTENTICACIÓN:
│   ├── login_cliente(email/telefono, contraseña)
│   ├── login_biometrico(huella/facial)
│   ├── login_2FA(codigo)
│   ├── recuperar_contraseña(email/sms)
│   ├── registro_nuevo_cliente()
│   └── cerrar_sesion()
│
├── MI DASHBOARD:
│   ├── resumen_prestamos_activos
│   │   ├── por_cada_prestamo: saldo, proxima_cuota, fecha, estado
│   │   └── semaforo: verde(al_dia) / amarillo(proximo_vencer) / rojo(vencido)
│   ├── calendario_pagos (vista mensual con cuotas marcadas)
│   ├── historial_pagos_recientes (últimos 5)
│   ├── notificaciones_pendientes
│   └── ofertas_personalizadas
│
├── MIS PRÉSTAMOS:
│   ├── ver_lista_prestamos(activos/liquidados/todos)
│   ├── ver_detalle_prestamo(id)
│   │   ├── datos_generales (monto, tasa, plazo, fecha_inicio, fecha_fin)
│   │   ├── tabla_amortizacion_completa (con pagos realizados marcados)
│   │   ├── saldo_actual_desglosado
│   │   ├── proxima_cuota (monto, fecha, días restantes)
│   │   ├── grafica_avance (% pagado vs pendiente)
│   │   └── historial_movimientos
│   │
│   ├── ver_historial_pagos(id_prestamo)
│   │   └── por_cada_pago: fecha, monto, metodo, folio, desglose_aplicacion
│   │
│   ├── descargar_estado_cuenta(id_prestamo, periodo) → PDF
│   ├── descargar_tabla_amortizacion(id_prestamo) → PDF/Excel
│   ├── descargar_recibo_pago(id_pago) → PDF
│   ├── descargar_contrato(id_prestamo) → PDF
│   ├── descargar_carta_no_adeudo(id_prestamo) → PDF (si liquidado)
│   └── descargar_constancia_intereses(id_prestamo, año) → PDF (fiscal)
│
├── SOLICITAR NUEVO PRÉSTAMO:
│   ├── simulador_prestamo(monto, plazo, producto)
│   │   └── muestra: cuota_estimada, interes_total, CAT, tabla_ejemplo
│   ├── iniciar_solicitud()
│   │   ├── paso_1: seleccionar_producto
│   │   ├── paso_2: monto_y_plazo
│   │   ├── paso_3: datos_personales (pre-llenados si ya es cliente)
│   │   ├── paso_4: datos_laborales
│   │   ├── paso_5: referencias
│   │   ├── paso_6: subir_documentos
│   │   ├── paso_7: revisión_final
│   │   └── paso_8: firmar_y_enviar
│   ├── guardar_borrador_solicitud()
│   ├── consultar_estado_solicitud(id)
│   │   └── timeline: recibida → en_evaluación → documentos_pendientes → aprobada/rechazada
│   └── aceptar_o_rechazar_oferta_aprobada()
│
├── REALIZAR PAGOS:
│   ├── pagar_cuota(id_prestamo)
│   │   ├── metodos_disponibles:
│   │   │   ├── tarjeta_debito_credito
│   │   │   ├── transferencia_SPEI
│   │   │   ├── pago_tienda_conveniencia (generar referencia)
│   │   │   ├── domiciliacion (configurar/cancelar)
│   │   │   └── wallet (MercadoPago/PayPal)
│   │   ├── pagar_monto_exacto_cuota
│   │   ├── pagar_monto_diferente
│   │   └── pagar_varias_cuotas_adelantadas
│   │
│   ├── pago_anticipado_total() → liquidar préstamo
│   │   └── mostrar: saldo_liquidacion + penalizacion_si_hay
│   │
│   ├── configurar_domiciliacion(datos_cuenta_bancaria)
│   ├── configurar_pago_recurrente(metodo, dia_mes)
│   └── ver_linea_captura() → para pago en banco/tienda
│
├── SOLICITAR SERVICIOS:
│   ├── solicitar_refinanciamiento()
│   │   └── simulador_opciones → seleccionar → enviar_solicitud
│   ├── solicitar_carta_no_adeudo()
│   ├── solicitar_constancia_intereses(año)
│   ├── solicitar_estado_cuenta_certificado()
│   ├── solicitar_copia_contrato()
│   └── solicitar_cambio_fecha_pago()
│
├── MIS DATOS:
│   ├── ver_perfil()
│   ├── actualizar_datos_contacto(telefono, email, direccion)
│   ├── actualizar_datos_laborales()
│   ├── subir_documentos_actualizados()
│   ├── cambiar_contraseña()
│   ├── configurar_2FA()
│   ├── configurar_notificaciones(canales[], frecuencia)
│   └── descargar_mis_datos() → ARCO (derecho acceso datos personales)
│
├── COMUNICACIÓN:
│   ├── ver_notificaciones()
│   ├── enviar_consulta_soporte(asunto, mensaje, adjuntos[])
│   ├── ver_historial_consultas()
│   ├── chat_en_vivo(con_agente)
│   ├── chatbot_inteligente()
│   │   ├── responder_preguntas_frecuentes
│   │   ├── consultar_saldo
│   │   ├── fecha_proxima_cuota
│   │   ├── generar_linea_captura
│   │   └── escalar_a_humano_si_no_resuelve
│   └── calificar_atencion(estrellas, comentario)
│
└── PROGRAMA DE REFERIDOS:
    ├── ver_codigo_referido()
    ├── compartir_enlace_referido(canal: whatsapp/email/sms/social)
    ├── ver_estado_referidos(pendientes/activos/premiados)
    └── ver_beneficios_acumulados()
```

### 💼 MÓDULO 15: CONTABILIDAD E INTEGRACIÓN FINANCIERA (NUEVO)

```
FUNCIONES OBLIGATORIAS:
├── DEVENGAMIENTO DE INTERESES:
│   ├── proceso_devengo_diario()
│   │   ├── para_cada_prestamo_activo:
│   │   │   ├── interes_dia = saldo_capital × tasa_diaria
│   │   │   ├── registrar_devengamiento
│   │   │   └── generar_poliza_contable
│   │   └── ejecutar: diario a las 23:59
│   │
│   ├── suspender_devengamiento(id_prestamo)
│   │   └── cuando mora > X días, dejar de reconocer ingreso
│   │
│   └── revertir_devengamiento_suspendido(id_prestamo)
│
├── PROVISIONES:
│   ├── proceso_calculo