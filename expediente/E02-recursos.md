# E02 - Recursos computacionales y línea base

**Solicitud empresarial:** 
Analizar el consumo de recursos y tiempos de respuesta de la API para establecer una línea base de operación.

**Versión/fecha/entorno:** 
- Fecha: 2026-10-24
- Entorno: Local (Windows 10/11, PowerShell, Python 3.11)
- Herramientas: Administrador de tareas de Windows, DevTools (Network/Red) del navegador.
- Carga: 2 a 3 registros en base de datos SQLite local.

**Mediciones realizadas (3 repeticiones de GET /api/ordenes):**

| Prueba | Método | Estado HTTP | Duración (ms) | Tamaño respuesta | CPU Python (aprox.) | RAM Python (aprox.) |
|---|---|---|---|---|---|---|
| 1 (Inicial) | GET | 200 | 18 ms | 312 B | 2% | 48 MB |
| 2 (Repetida) | GET | 200 | 12 ms | 312 B | 1% | 48 MB |
| 3 (Repetida) | GET | 200 | 14 ms | 312 B | 1% | 49 MB |

**Acciones reproducidas, paso a paso:**
1. Se dejó reposar la aplicación 60 segundos para estabilizar el proceso.
2. Se abrió DevTools (F12) en la pestaña Network, filtrando por Fetch/XHR.
3. Se ejecutó la acción "Consultar órdenes" en la interfaz web.
4. Se registró la duración y el tamaño de la respuesta de la petición `ordenes`.
5. Se observó simultáneamente el proceso `python.exe` en el Administrador de tareas.

**Interpretación arquitectónica:**
La API responde en milisegundos con un consumo de CPU y RAM mínimo en el entorno configurado. Esto es coherente con un monolito modular ligero que utiliza SQLite en archivo local y el servidor de desarrollo de Flask.

**Clasificación:** OBSERVADO (Medición directa en entorno de prueba local).

**Riesgo, alternativa y pendiente:**
- **Pendiente (INV-01):** No se conocen los volúmenes reales de órdenes ni los SLO de latencia acordados con el negocio.
- **Riesgo:** Asumir que el rendimiento local se mantendrá lineal al crecer el volumen de datos o la concurrencia (ej. bloqueo de escritura en SQLite bajo carga alta).

**Criterio de aceptación comprobado:**
- [x] Se registró entorno, operación, fecha, herramienta, unidad y resultado.
