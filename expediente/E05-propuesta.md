# E05 - Primera propuesta arquitectónica provisional

**Solicitud empresarial:** 
Mantener la capacidad de registrar y consultar órdenes de mantenimiento, evaluando la organización actual del código frente a una alternativa más simple, antes de considerar evoluciones futuras.

**Versión/fecha/entorno:** 
- Fecha: 2026-10-24
- Entorno: Local (Windows 10/11, PowerShell, Python 3.11, Flask 3.x)
- Herramientas: VS Code, revisión de código fuente y diagramas C4 (E03, E04).

**Archivos y componentes observados:**
- `backend/app/ordenes/controladores.py`, `servicios.py`, `repositorios.py`, `modelos.py`.
- `frontend/app.js`, `frontend/index.html`.
- Diagramas `contexto.drawio` y `contenedores.drawio`.

**Acciones reproducidas, paso a paso:**
1. Se revisaron E01 a E04 para asegurar que negocio, actores, rutas y diagramas describen la misma versión del producto.
2. Se redactó la decisión actual sustentada: conservar una API Flask modular, frontend ligero y persistencia relacional.
3. Se comparó la arquitectura actual (Opción A) con una alternativa de código concentrado sin separación de capas (Opción B).
4. Se registró la matriz de trazabilidad: necesidad → evidencia → parte C4 → alternativa → riesgo.
5. Se identificó la información pendiente: datos de uso real, operación de soporte, requisitos de seguridad y condiciones de crecimiento.

**Matriz de trazabilidad:**
| Necesidad | Evidencia | Parte C4 | Alternativa | Riesgo |
|---|---|---|---|---|
| Consultar y registrar órdenes | GET/POST /api/ordenes responden 200/201 | API Flask | A: Modular por capas | Requiere disciplina de límites internos |
| Conservar órdenes tras reinicio | SQLite persiste en `instance/mantenimiento.db` | Almacén SQL | B: Código concentrado | Cambios y pruebas más acoplados |
| Interfaz web ligera | `app.js` consume API vía fetch | SPA navegador | A: Modular por capas | Mayor cantidad de archivos al inicio |

**Comparación de alternativas:**
| Alternativa | Ventaja potencial | Riesgo para el caso |
|---|---|---|
| **A · Modular por capas (Actual)** | Separación clara entre HTTP (controladores), reglas (servicios) y persistencia (repositorios). Facilita pruebas unitarias y cambios aislados. | Necesita disciplina de límites internos para no degenerar en acoplamiento. |
| **B · Código concentrado** | Menos archivos y menos indirectación al inicio del proyecto. | Cambios en reglas de negocio o persistencia afectan directamente al controlador; pruebas más acopladas a la infraestructura. |

**Decisión provisional:**
Conservar la **Opción A (Monolito modular por capas)**. La separación de responsabilidades observada en `controladores.py`, `servicios.py` y `repositorios.py` aporta cohesión y facilita la evolución del contrato de la API sin impactar la persistencia, lo cual es consistente con el driver de posible crecimiento del listado (INV-01).

**Información pendiente:**
- Volúmenes reales de órdenes y concurrencia (INV-01).
- Requisitos de autenticación y roles (SEG-01).
- Política de retención de datos y backups.
- SLO de latencia aprobados por el negocio.

**Clasificación:** DOCUMENTADO (Propuesta provisional basada en revisión de código y diagramas).

**Criterio de aceptación comprobado:**
- [x] E05 incluye al menos dos organizaciones plausibles (A y B).
- [x] Incluye matriz de trazabilidad y límites explícitos de la recomendación.
- [x] La propuesta se presenta como provisional, no como dictamen final.
