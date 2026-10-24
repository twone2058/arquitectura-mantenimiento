# E10 - Rendimiento, disponibilidad, seguridad y costos

**Solicitud empresarial:**
Analizar el comportamiento del sistema ante un fallo reversible (indisponibilidad de la API), evaluar límites de seguridad del entorno de prueba y considerar implicaciones de costo/escalamiento.

**Versión/fecha/entorno:**
- Fecha: 2026-10-24
- Entorno: Local (Windows 10/11, PowerShell, Python 3.11, Flask 3.x, SQLite)
- Herramientas: Navegador (DevTools Network), Terminal de PowerShell.

**Archivos y componentes observados:**
- frontend/app.js: Manejo de errores en la función consultarOrdenes() con bloque try/catch.
- backend/app.py: Servidor Flask en modo desarrollo (debug=False).
- backend/instance/mantenimiento.db: Almacén de datos persistente.

**Acciones reproducidas, paso a paso:**
1. Con el servidor Flask activo, se abrió la interfaz web en http://127.0.0.1:5000 y se verificó que la consulta de órdenes funcionaba (HTTP 200).
2. Se detuvo el servidor Flask en la terminal usando Ctrl+C (simulando una caída o reinicio del backend).
3. Sin recargar la página completa del navegador, se hizo clic en el botón "Consultar órdenes".
4. Se observó en DevTools (Network) un error de red (falla de conexión, sin código HTTP 5xx porque el servidor no respondió).
5. Se observó en la interfaz el mensaje de error controlado: "No fue posible consultar: Failed to fetch" (o similar, según el navegador), sin que la aplicación se colgara.
6. Se reinició el servidor Flask (py app.py) y se verificó que la consulta volvía a funcionar y los datos persistían (HTTP 200).

**Resultado observado:**
El sistema presenta una degradación controlada. El cliente (SPA) maneja la ausencia de respuesta de la API mostrando un mensaje al usuario en lugar de bloquear la interfaz. Al reiniciar el backend, la operación se recupera inmediatamente y los datos no se pierden, cumpliendo con RN-01.

**Interpretación arquitectónica:**
- **Disponibilidad:** La caída del backend es un punto único de fallo (SPOF) en esta arquitectura local. La recuperación es rápida al ser un proceso ligero, pero no hay alta disponibilidad (HA) configurada.
- **Seguridad:** El endpoint /api/ordenes es público en este entorno de prueba (SEG-01 pendiente). No existe autenticación, autorización ni rate limiting. No debe exponerse a Internet sin un API Gateway, autenticación (JWT/OAuth) y validación de origen (CORS).
- **Costo/Escalamiento:** Mantener este monolito modular tiene un costo operativo bajo. Escalar horizontalmente requeriría externalizar la base de datos SQLite a un motor compartido (ej. MySQL/PostgreSQL) y usar un balanceador de carga, lo cual incrementa la complejidad y el costo de infraestructura.

**Clasificación:** OBSERVADO (Prueba de fallo reversible ejecutada) y DOCUMENTADO.

**Riesgo, alternativa y pendiente:**
- **Riesgo:** Exponer este demo en red sin controles de seguridad.
- **Pendiente:** Definir SLO de disponibilidad y políticas de autenticación para un entorno productivo.
- **Alternativa:** Para producción, migrar a un RDS (MySQL/PostgreSQL) y agregar un proxy inverso (Nginx) con autenticación.

**Criterio de aceptación comprobado:**
- [x] Se registró el incidente reversible, su impacto y recuperación.
- [x] Se distinguieron los fallos de red (sin respuesta HTTP) de los errores del servidor (4xx/5xx).
- [x] Se documentaron los límites de seguridad y costos de escalamiento sin inventar cifras.
