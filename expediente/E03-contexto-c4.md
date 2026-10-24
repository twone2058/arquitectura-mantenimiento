# E03 - Responsabilidades, cliente-servidor y C4 Context

**Solicitud empresarial:** 
Definir las responsabilidades del sistema y sus límites con los actores externos para establecer el diagrama de C4 Context.

**Versión/fecha/entorno:** 
- Fecha: 2026-10-24
- Entorno: Local (Windows 10/11, PowerShell)
- Herramientas: diagrams.net (archivo .drawio generado), VS Code.

**Archivos y componentes observados:**
- `frontend/index.html` y `frontend/app.js`: Interfaz que consume la API.
- `backend/app/ordenes/controladores.py`: Endpoints que reciben las solicitudes.
- `expediente/diagramas/contexto.drawio`: Diagrama de contexto C4.

**Acciones reproducidas, paso a paso:**
1. Se identificaron los actores del caso: Operador de operaciones (consulta) y Coordinador de equipos (registra).
2. Se delimitó el sistema como una única caja: "Sistema de gestión de mantenimiento".
3. Se generó el diagrama `contexto.drawio` conectando los actores con el sistema mediante flechas etiquetadas ("Consulta órdenes" y "Registra órdenes").
4. Se verificó que no se incluyeron componentes internos (como la base de datos) ni servicios externos no confirmados (como correo o pagos).

**Resultado observado:**
El diagrama muestra claramente la frontera del producto. Los actores interactúan con el sistema para cumplir los requisitos RF-01 (Registrar órdenes) y RF-02 (Consultar órdenes).

**Interpretación arquitectónica:**
El sistema opera bajo un modelo cliente-servidor donde el navegador actúa como cliente ligero y Flask como servidor de la API. En C4 Context, no se exponen detalles internos como controladores o tablas, manteniendo la vista enfocada en el negocio.

**Clasificación:** DOCUMENTADO (Diagrama y descripción generados).

**Riesgo, alternativa y pendiente:**
- **Pendiente:** Confirmar si existen otros sistemas externos (ej. ERP o inventario) que deban integrarse en el futuro.
- **Riesgo:** Asumir que los actores actuales son los únicos consumidores de la API.

**Criterio de aceptación comprobado:**
- [x] El Context presenta un límite consistente, actores reconocibles y relaciones con propósito.
- [x] No se expusieron clases, tablas ni rutas de archivos internos.
