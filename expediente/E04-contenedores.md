# E04 - Capas, monolito modular y C4 Container

**Solicitud empresarial:** 
Documentar la organización interna del sistema en contenedores (aplicaciones y almacenes) para comprender cómo colaboran los componentes.

**Versión/fecha/entorno:** 
- Fecha: 2026-10-24
- Entorno: Local (Windows 10/11, PowerShell)
- Herramientas: diagrams.net (archivo .drawio generado), VS Code.

**Archivos y componentes observados:**
- `frontend/index.html` y `frontend/app.js`: SPA ligera que consume la API.
- `backend/app/__init__.py`: Fábrica de Flask que registra el blueprint de órdenes.
- `backend/app/ordenes/controladores.py`: Endpoints HTTP (GET/POST).
- `backend/app/ordenes/servicios.py`: Validación de reglas de negocio.
- `backend/app/ordenes/repositorios.py`: Acceso a datos mediante SQLAlchemy.
- `backend/app/ordenes/modelos.py`: Definición de la entidad Orden.
- `backend/instance/mantenimiento.db`: Almacén SQLite local.

**Acciones reproducidas, paso a paso:**
1. Se identificaron los tres contenedores principales: SPA navegador, API Flask y almacén SQL.
2. Se verificó que la SPA se comunica con la API mediante HTTP/JSON (fetch en `app.js`).
3. Se verificó que la API utiliza SQLAlchemy (ORM) para interactuar con SQLite.
4. Se generó el diagrama `contenedores.drawio` mostrando las conexiones y protocolos.
5. Se confirmó que el backend es un monolito modular (una sola aplicación Flask con capas internas), no un conjunto de microservicios.

**Resultado observado:**
El diagrama muestra claramente la separación entre la interfaz de usuario (SPA), la lógica de negocio y persistencia (API Flask con capas) y el almacén de datos (SQLite). Las conexiones están etiquetadas con sus protocolos (HTTP/JSON y ORM/SQL).

**Interpretación arquitectónica:**
El sistema sigue un patrón de monolito modular con separación de responsabilidades:
- **Capa de presentación:** HTML/JavaScript en el navegador.
- **Capa de aplicación:** Controladores Flask que reciben solicitudes HTTP.
- **Capa de dominio:** Servicios que validan reglas de negocio.
- **Capa de infraestructura:** Repositorios y ORM que acceden a la base de datos.

Esta organización permite cambiar la persistencia (ej. de SQLite a MySQL) modificando solo el repositorio y la configuración, sin afectar la lógica de negocio ni la interfaz.

**Clasificación:** DOCUMENTADO (Diagrama y descripción generados).

**Riesgo, alternativa y pendiente:**
- **Pendiente:** Validar si la separación de capas es suficiente para escalar o si se requiere una abstracción adicional (ej. interfaces de repositorio).
- **Riesgo:** Asumir que el monolito modular será suficiente si el sistema crece significativamente en complejidad o equipos de desarrollo.

**Criterio de aceptación comprobado:**
- [x] El diagrama Container representa el mismo sistema que el Context sin contradecir las fronteras.
- [x] Las responsabilidades y protocolos aparecen rotulados correctamente (HTTP/JSON, ORM/SQL).
- [x] No se dibujaron controladores y repositorios como servidores separados.
