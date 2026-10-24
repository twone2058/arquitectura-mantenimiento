# Índice de Evidencias del Expediente Arquitectónico

| ID Evidencia | Archivo / Ruta | Afirmación que respalda | Estado |
|--------------|----------------|--------------------------|--------|
| E01-CTX-01 | `expediente/E01-contexto.md` | El sistema cumple con RF-01, RF-02 y RN-01 en entorno local. | OBSERVADO |
| E01-CTX-02 | `backend/app/ordenes/servicios.py` | La validación de tipos previene inserción de datos corruptos (HTTP 400). | VERIFICADO EN CÓDIGO |
| E02-REC-01 | `expediente/E02-recursos.md` | La API responde en milisegundos con consumo mínimo en entorno local (línea base). | OBSERVADO |
| E03-C4-01 | `expediente/diagramas/contexto.drawio` | El diagrama muestra el sistema como una caja única con dos actores externos y sus operaciones. | DOCUMENTADO |
| E03-C4-02 | `expediente/E03-contexto-c4.md` | La frontera del producto está delimitada y no expone componentes internos. | DOCUMENTADO |
| E04-CONT-01 | `expediente/diagramas/contenedores.drawio` | El diagrama muestra tres contenedores (SPA, API Flask, Almacén SQL) con sus protocolos de comunicación. | DOCUMENTADO |
| E04-CONT-02 | `expediente/E04-contenedores.md` | El backend es un monolito modular con separación de capas (presentación, aplicación, dominio, infraestructura). | DOCUMENTADO |
| E05-PROP-01 | `expediente/E05-propuesta.md` | La propuesta provisional es conservar el monolito modular por capas (Opción A) frente a código concentrado (Opción B). | DOCUMENTADO |
| E06-ALT-01 | `expediente/E06-alternativas.md` | Se compararon Monolito modular, SOA, Microservicios y Eventos. Se decide conservar el monolito por ausencia de drivers distribuidos. | DOCUMENTADO |
| E06-ALT-01 | `expediente/E06-alternativas.md` | Se compararon Monolito modular, SOA, Microservicios y Eventos. Se decide conservar el monolito por ausencia de drivers distribuidos. | DOCUMENTADO |
| E07-CAL-01 | `expediente/E07-calidad.md` | Se definieron 3 RAR y 2 escenarios de calidad (Crecimiento y Fallo de API) con medidas pendientes de aprobación. | DOCUMENTADO |
| E07-CAL-01 | `expediente/E07-calidad.md` | Se definieron tres RAR (integridad, crecimiento, disponibilidad) y dos escenarios medibles (EC-01, EC-02). | DOCUMENTADO |

| E08-MOD-01 | expediente/E08-modularidad.md | Análisis SOLID confirma cohesión adecuada; L y D tienen hallazgos aceptables. | VERIFICADO EN CÓDIGO |
| E08-MOD-01 | expediente/E08-modularidad.md | Análisis SOLID confirma cohesión adecuada; L y D tienen hallazgos aceptables. | VERIFICADO EN CÓDIGO |

| E09-INT-01 | expediente/E09-integracion.md | Contrato HTTP documentado, flujo sincrónico verificado y persistencia confirmada tras reinicio. | OBSERVADO / VERIFICADO EN CÓDIGO |

| E10-RIES-01 | expediente/E10-riesgos.md | Degradación controlada ante caída del backend verificada; límites de seguridad y escalamiento documentados. | OBSERVADO / DOCUMENTADO |

| E11-DEC-01 | expediente/E11-decision.md | Decisión sobre evolución de consulta documentada con trade-offs claros. | DOCUMENTADO |
| ADR-001 | expediente/decisiones/ADR-001.md | Registro formal de la decisión de paginación como PROPUESTO, con condiciones de validación. | DOCUMENTADO |
