# E01 - Comprensión del problema, requisitos y alcance

**Solicitud empresarial:** 
El área de Operaciones necesita registrar órdenes de mantenimiento de equipos de bodega (montacargas, bandas) y consultarlas posteriormente.

**Versión/fecha/entorno:** 
- Fecha: 2026-10-24
- Entorno: Local (Windows 10/11)
- Stack: Python 3.x, Flask 3.x, SQLite, HTML/JS vanilla.
- URL de prueba: http://127.0.0.1:5000

**Archivos y componentes observados:**
- `frontend/index.html` y `frontend/app.js`: Interfaz de usuario y consumo de API.
- `backend/app/ordenes/controladores.py`: Endpoints GET y POST en `/api/ordenes`.
- `backend/app/ordenes/servicios.py`: Validación de reglas de negocio (texto obligatorio, longitudes máximas).
- `backend/app/ordenes/modelos.py`: Esquema de persistencia (id, equipo, descripcion, estado).

**Acciones reproducidas, paso a paso:**
1. Inicio del servidor Flask (`python app.py`).
2. Ejecución de `GET /api/ordenes` → Respuesta 200 con listado inicial.
3. Ejecución de `POST /api/ordenes` con datos válidos → Respuesta 201 y persistencia.
4. Ejecución de `POST /api/ordenes` con payload inválido (objetos/listas en lugar de texto) → Respuesta 400 sin inserción en BD.
5. Consulta de `/health` → Respuesta 200 `{"status": "ok"}`.

**Resultado observado:**
- La API responde correctamente a las operaciones CRUD básicas solicitadas.
- La validación de tipos en el servicio rechaza entradas no textuales, devolviendo HTTP 400 y protegiendo la integridad de la base de datos.
- Los datos se conservan tras las operaciones (RN-01 cumplido).

**Interpretación arquitectónica:**
El sistema actual es un monolito modular que separa claramente la interfaz (SPA ligera), la lógica de transporte (controladores), las reglas de negocio (servicios) y la persistencia (repositorios + SQLAlchemy). Cumple con los requisitos funcionales RF-01 y RF-02 en el alcance local definido.

**Clasificación:** 
- OBSERVADO (Pruebas de API ejecutadas y reproducidas).
- VERIFICADO EN CÓDIGO (Validación de tipos y longitud en `servicios.py`).

**Riesgo, alternativa y pendiente:**
- **Pendiente (INV-01):** No se conocen volúmenes reales de órdenes ni SLO de latencia. La consulta actual (`listar_todas`) no tiene paginación.
- **Pendiente (INV-02):** Comportamiento del cliente cuando la API está indisponible (se observó error en red, pero falta política de reintento o caché).
- **Pendiente (SEG-01):** No existe autenticación ni control de acceso. El endpoint es público en este entorno de prueba.

**Criterio de aceptación comprobado:**
- [x] RF-01: Registro de órdenes con equipo y descripción no vacíos.
- [x] RF-02: Consulta de órdenes y su estado desde la aplicación web.
- [x] RN-01: Conservación de órdenes tras reiniciar el backend (verificado por persistencia SQLite).
