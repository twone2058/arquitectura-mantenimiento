# E08 - Modularidad, dependencias y SOLID

**Solicitud empresarial:**
Analizar la cohesión y el acoplamiento entre los módulos del backend para identificar puntos de mejora en la mantenibilidad del sistema.

**Versión/fecha/entorno:**
- Fecha: 2026-10-24
- Entorno: Local (Windows 10/11, PowerShell, Python 3.11, Flask 3.x)
- Herramientas: VS Code (navegación de código con Ctrl+clic), revisión estática de archivos Python.

**Archivos y componentes observados:**
- backend/app/ordenes/controladores.py: Funciones consultar() y crear().
- backend/app/ordenes/servicios.py: Funciones listar() y registrar(datos).
- backend/app/ordenes/repositorios.py: Funciones listar_todas() y guardar(equipo, descripcion).
- backend/app/ordenes/modelos.py: Clase Orden con SQLAlchemy.
- backend/app/extensiones.py: Instancia db de SQLAlchemy.

**Acciones reproducidas, paso a paso:**
1. Se abrió controladores.py y se localizó el método crear(): su responsabilidad es leer la solicitud JSON, delegar al servicio y devolver la respuesta HTTP (201 o 400).
2. Se usó Ctrl+clic en servicios.registrar para navegar al archivo servicios.py. Se observó que valida los campos (tipo texto, obligatoriedad, longitud) y delega la inserción a repositorios.guardar.
3. Se abrió repositorios.guardar y se localizó db.session.add y db.session.commit. Se confirmó que las reglas de negocio están separadas del mecanismo de persistencia.
4. Se documentó el mapa de dependencias: Controlador -> Servicio -> Repositorio -> ORM -> SQL.
5. Se aplicaron los principios SOLID como preguntas sobre la estructura real del código.

**Mapa de dependencias observado:**

Controlador (HTTP)
    | delega
    v
Servicio (Reglas de negocio)
    | llama
    v
Repositorio (Acceso a datos)
    | usa
    v
ORM SQLAlchemy
    | persiste
    v
Base de datos SQLite

**Análisis SOLID aplicado como preguntas:**

| Principio | Pregunta práctica | Hallazgo en el código |
|---|---|---|
| S - Responsabilidad única | ¿El módulo cambia por motivos independientes? | Cumple. controladores.py solo coordina HTTP; servicios.py solo valida reglas; repositorios.py solo accede a datos. |
| O - Abierto/cerrado | ¿La ampliación requiere modificar varias partes sin necesidad? | Parcialmente cumple. Para cambiar de SQLite a MySQL solo se modifica .env (DATABASE_URL) y se instala PyMySQL. |
| L - Sustitución | ¿Una implementación respeta el comportamiento prometido por el contrato? | Hallazgo. No existen interfaces de repositorio. El servicio depende directamente de la implementación concreta repositorios.guardar(). |
| I - Segregación de interfaces | ¿El consumidor depende de capacidades que no utiliza? | Cumple. El servicio solo usa listar() y guardar(), no métodos innecesarios del repositorio. |
| D - Inversión de dependencias | ¿Las reglas principales están atadas a detalles técnicos? | Hallazgo aceptable a esta escala. El servicio importa directamente repositorios (detalle de infraestructura). |

**Interpretación arquitectónica:**
La separación de responsabilidades observada favorece la cohesión y facilita pruebas unitarias. El controlador no contiene SQL ni reglas de negocio; el servicio no conoce HTTP; el repositorio no valida campos.

**Clasificación:** VERIFICADO EN CÓDIGO (Análisis estático de archivos Python reales).

**Riesgo, alternativa y pendiente:**
- Pendiente: Confirmar si el crecimiento del sistema justificará introducir interfaces de repositorio.
- Riesgo: Asumir que la dependencia directa servicio -> repositorio será sostenible.
- Alternativa: Introducir una abstracción IRepositorioOrdenes si aparece un driver real.

**Criterio de aceptación comprobado:**
- [x] El mapa de dependencias cita funciones reales del código.
- [x] SOLID se aplicó como preguntas de revisión, no como lista mecánica.
- [x] Los hallazgos incluyen interpretación y condiciones de mejora.
