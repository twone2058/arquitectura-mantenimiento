# E06 - Comparación de SOA, microservicios y eventos

**Solicitud empresarial:** 
Evaluar la evolución arquitectónica del sistema ante un posible crecimiento del volumen de órdenes, comparando la arquitectura actual con alternativas distribuidas.

**Versión/fecha/entorno:** 
- Fecha: 2026-10-24
- Entorno: Local (Windows 10/11, PowerShell)
- Herramientas: VS Code, revisión de código fuente y evidencias E01 a E05.

**Archivos y componentes observados:**
- Estructura de carpetas `backend/app/ordenes/` (controladores, servicios, repositorios).
- Evidencias E01 a E05 (contexto, recursos, C4, propuesta inicial).

**Acciones reproducidas, paso a paso:**
1. Se revisaron las evidencias E01 a E05 para identificar si existe un driver que exija despliegue separado (diferencias de escalamiento, propiedad de datos, límites de equipo o integración externa confirmada).
2. Se creó una matriz comparativa con cuatro opciones: Monolito modular, SOA, Microservicios y Orientación a eventos.
3. Para cada opción se describieron contratos, autonomía de datos, coordinación, manejo de fallos, costos operativos y complejidad.
4. Se compararon las consecuencias con las restricciones del escenario actual: uso local, un dominio sencillo y ausencia de datos de carga reales.
5. Se documentó la decisión provisional basada en los drivers observados.

**Matriz de alternativas:**
| Opción | Posible aporte | Costo o riesgo para el caso |
|---|---|---|
| **Monolito modular (Actual)** | Menos servicios operativos; límites internos claros; despliegue unitario simple. | Dependencias mal delimitadas podrían causar crecimiento descontrolado de la unidad. |
| **SOA (Arquitectura Orientada a Servicios)** | Servicios por capacidades con contratos reutilizables por otras aplicaciones. | Requiere gobierno, gestión de versiones, orquestación e integración compleja. |
| **Microservicios** | Autonomía total por capacidades, escalamiento y despliegue independiente. | Red distribuida, observabilidad compleja, consistencia de datos, fallos en cascada. |
| **Orientada a eventos** | Desacoplamiento temporal y distribución eficiente de sucesos. | Duplicados, reintentos, consistencia eventual y trazabilidad compleja. |

**Interpretación arquitectónica:**
No se ha identificado hoy un driver que exija despliegue separado. El dominio es sencillo (órdenes de mantenimiento), el uso es local y no hay datos de carga que justifiquen la complejidad de una red distribuida. Introducir microservicios o eventos ahora añadiría costos operativos y de complejidad humana sin un beneficio verificable.

**Decisión provisional:**
Conservar la unidad modular (Monolito modular). Reabrir el análisis de alternativas distribuidas únicamente ante un driver comprobado (ej. necesidad de escalamiento independiente de módulos, equipos de desarrollo separados con ciclos distintos, o integración confirmada con sistemas externos que requieran contratos reutilizables).

**Clasificación:** DOCUMENTADO (Análisis comparativo basado en restricciones del caso).

**Riesgo, alternativa y pendiente:**
- **Pendiente:** Confirmar volúmenes reales de órdenes y concurrencia (INV-01).
- **Riesgo:** Asumir que el monolito modular escalará indefinidamente sin revisar los límites de la base de datos o del servidor web.

**Criterio de aceptación comprobado:**
- [x] Las alternativas consideran beneficios y costos concretos.
- [x] La recomendación está vinculada a drivers observados o pendientes, no a preferencias tecnológicas ("más moderno").
