# E09 - Integración HTTP, sincronía y persistencia

**Solicitud empresarial:**
Documentar el contrato real de la API, el flujo sincrónico de las operaciones y verificar la persistencia de los datos tras reiniciar el backend.

**Versión/fecha/entorno:**
- Fecha: 2026-10-24
- Entorno: Local (Windows 10/11, PowerShell, Python 3.11, Flask 3.x, SQLite)
- Herramientas: Navegador (DevTools Network), PowerShell (Invoke-RestMethod), VS Code.

**Archivos y componentes observados:**
- backend/app/ordenes/controladores.py: Endpoints GET y POST.
- backend/app/ordenes/servicios.py: Validación de reglas de negocio.
- backend/app/ordenes/repositorios.py: Acceso a datos mediante SQLAlchemy.
- frontend/app.js: Cliente HTTP que consume la API mediante fetch().
- backend/instance/mantenimiento.db: Almacén de persistencia local.

**Acciones reproducidas, paso a paso:**
1. Se verificó la operación de lectura: GET /api/ordenes respondió con HTTP 200 y un JSON con la estructura {success: true, data: [...]}.
2. Se verificó la operación de escritura válida: POST /api/ordenes con payload JSON correcto respondió con HTTP 201 y el objeto creado.
3. Se verificó la validación de entrada: POST /api/ordenes con payload inválido (ej. objetos o listas en lugar de texto) respondió con HTTP 400 y no insertó ningún registro en la base de datos.
4. Se comprobó la persistencia (RN-01): Se detuvo el servidor Flask (Ctrl+C), se volvió a iniciar y se ejecutó GET /api/ordenes. Los registros creados previamente seguían presentes.
5. Se documentó el carácter sincrónico del flujo: el cliente espera la respuesta HTTP antes de continuar con la siguiente instrucción en app.js.

**Contrato HTTP observado:**
| Operación | Ruta | Método | Código Éxito | Código Error | Payload Esperado |
|---|---|---|---|---|---|
| Consultar | /api/ordenes | GET | 200 | N/A | Ninguno |
| Registrar | /api/ordenes | POST | 201 | 400 | {equipo: string, descripcion: string} |

**Interpretación arquitectónica:**
La integración sigue un patrón cliente-servidor sincrónico sobre HTTP/REST. El navegador (cliente) envía una solicitud y bloquea la ejecución hasta recibir la respuesta del servidor Flask. La separación de responsabilidades es clara: el controlador maneja el protocolo HTTP, el servicio valida las reglas y el repositorio se encarga de la persistencia. La base de datos SQLite garantiza la conservación de los datos entre reinicios del proceso, cumpliendo con RN-01.

**Clasificación:** OBSERVADO (Pruebas de API ejecutadas) y VERIFICADO EN CÓDIGO (Recorrido de funciones confirmado).

**Riesgo, alternativa y pendiente:**
- **Pendiente:** Definir política de reintentos o caché en el frontend si la API tarda en responder (INV-02).
- **Riesgo:** Asumir que la sincronía es adecuada para operaciones que en el futuro podrían tardar varios segundos (ej. generación de reportes pesados).
- **Alternativa:** Introducir asincronía (colas de mensajes) solo si aparecen drivers de negocio que lo justifiquen (ej. procesamiento en segundo plano).

**Criterio de aceptación comprobado:**
- [x] E09 incluye método, ruta, contrato, error y responsables del flujo.
- [x] Se distingue la sincronía actual de una asincronía propuesta.
- [x] Se verificó la persistencia de datos tras reiniciar el backend.
