# E07 - RAR y escenarios de calidad

**Solicitud empresarial:** 
Definir atributos de calidad relevantes y escenarios medibles para evaluar el comportamiento del sistema ante crecimiento de datos e indisponibilidad de la API.

**Versión/fecha/entorno:** 
- Fecha: 2026-10-24
- Entorno: Local (Windows 10/11, PowerShell, Python 3.11, Flask 3.x)
- Herramientas: DevTools del navegador (Network), PowerShell, VS Code.

**Archivos y componentes observados:**
- `backend/app/ordenes/repositorios.py`: Función `listar_todas()` sin límite de registros.
- `frontend/app.js`: Manejo de errores en la función `consultarOrdenes()`.
- Evidencias E01, E02, E06 (contexto, recursos, alternativas).

**Acciones reproducidas, paso a paso:**
1. Se identificaron tres preocupaciones de calidad: integridad del registro, crecimiento del listado y comportamiento ante indisponibilidad de la API.
2. Se relacionó cada RAR con elementos del diagrama C4 Container (SPA, API, Almacén SQL).
3. Se redactaron dos escenarios completos (EC-01 y EC-02) con fuente, estímulo, ambiente, artefacto, respuesta y medida.
4. Se verificó que no se inventaron SLA, concurrencia o tiempos aprobados; los umbrales se marcan como "pendientes de aprobación".
5. Se documentó el método de captura de evidencia para cada escenario.

**Matriz RAR (Requisitos Arquitectónicos Relevantes):**
| RAR | Descripción | Elemento C4 afectado | Estado |
|---|---|---|---|
| RAR-01 · Integridad | Conservar órdenes tras reiniciar el backend. | Almacén SQL | Implementado |
| RAR-02 · Crecimiento | Mantener respuesta consultable ante aumento de volumen. | API Flask, Almacén SQL | Pendiente de validar |
| RAR-03 · Disponibilidad | Informar error al usuario cuando la API no responde. | SPA navegador, API Flask | Implementado (parcial) |

**Escenarios de calidad:**

**EC-01 · Crecimiento del listado**
- **Fuente:** Área de Operaciones.
- **Estímulo:** Incremento del número de órdenes en la base de datos.
- **Ambiente:** Entorno de prueba con conjunto de datos documentado.
- **Artefacto:** API Flask (`GET /api/ordenes`) y repositorio (`listar_todas()`).
- **Respuesta esperada:** Entregar resultados completos según el contrato JSON aprobado, sin errores de timeout o memoria.
- **Medida:** Latencia (ms) y tamaño de respuesta (KB) con carga documentada; umbral pendiente de aprobación con el negocio.
- **Método de evidencia:** DevTools Network para capturar duración y tamaño; consulta SQL para contar registros.

**EC-02 · Indisponibilidad de la API**
- **Fuente:** Suspensión del backend Flask (detención del proceso).
- **Estímulo:** Solicitud de consulta desde la interfaz web sin conexión a la API.
- **Ambiente:** Navegador con página ya cargada, backend detenido.
- **Artefacto:** Cliente HTTP (`fetch()` en `app.js`).
- **Respuesta esperada:** Mostrar mensaje de error al usuario sin afirmar pérdida de datos; no colgar la interfaz.
- **Medida:** Error observable en Network (falla de red) y recuperación posterior al reiniciar Flask.
- **Método de evidencia:** Captura de pantalla de DevTools mostrando error de red; mensaje visible en `#estado`.

**EC-03 · Integridad tras reinicio** (Verificación de RN-01)
- **Fuente:** Reinicio del proceso Flask.
- **Estímulo:** Cierre y arranque del backend (`Ctrl+C` → `python app.py`).
- **Ambiente:** Entorno local con SQLite en `backend/instance/mantenimiento.db`.
- **Artefacto:** Almacén SQL y repositorio.
- **Respuesta esperada:** Las órdenes creadas antes del reinicio deben aparecer en la consulta posterior.
- **Medida:** Conteo de registros antes y después del reinicio; coincidencia exacta.
- **Método de evidencia:** GET `/api/ordenes` antes y después; verificación del archivo SQLite.

**Interpretación arquitectónica:**
Los escenarios EC-01 y EC-02 permiten evaluar la evolución del sistema sin inventar métricas. EC-01 está vinculado al driver INV-01 (crecimiento del listado) y justificaría la paginación si se confirma un volumen alto. EC-02 valida la degradación controlada del cliente cuando la API falla.

**Clasificación:** DOCUMENTADO (Escenarios definidos con método de verificación).

**Riesgo, alternativa y pendiente:**
- **Pendiente:** Aprobar umbrales de latencia y volumen máximo con el área de Operaciones.
- **Riesgo:** Asumir que el escenario EC-01 se cumple sin pruebas de carga reales; la consulta actual (`all()`) podría degradarse con miles de registros.

**Criterio de aceptación comprobado:**
- [x] Los escenarios contienen estímulo, entorno, artefacto, respuesta y método de medida.
- [x] No hay cifras inventadas ni funcionalidades de seguridad supuestas.
- [x] Cada RAR está vinculado a un elemento C4 y a una necesidad del negocio.
