# E11 - Decisión final, trade-offs y ADR-001

**Solicitud empresarial:**
Documentar la decisión arquitectónica sobre la evolución de la consulta de órdenes, evaluando los trade-offs entre mantener la simplicidad actual y preparar el sistema para un crecimiento futuro.

**Versión/fecha/entorno:**
- Fecha: 2026-10-24
- Entorno: Local (Windows 10/11, PowerShell, Python 3.11, Flask 3.x)
- Herramientas: VS Code, revisión de código (repositorios.py), evidencias E01 a E10.

**Archivos y componentes observados:**
- backend/app/ordenes/repositorios.py: Función listar_todas() que ejecuta db.session.scalars(consulta).all() sin límite.
- backend/app/ordenes/controladores.py: Endpoint GET /api/ordenes que devuelve la lista completa.
- expediente/decisiones/ADR-001.md: Registro formal de la decisión arquitectónica.

**Acciones reproducidas, paso a paso:**
1. Se revisó el código de repositorios.py y se confirmó que la consulta actual no impone un límite (LIMIT/OFFSET) a los registros devueltos.
2. Se evaluó el impacto: para volúmenes pequeños, el rendimiento es óptimo y la simplicidad es máxima. Para volúmenes grandes, el consumo de memoria y la latencia aumentarían linealmente.
3. Se compararon dos alternativas: A) Mantener el contrato actual; B) Diseñar una extensión paginada compatible, pendiente de validar con volúmenes reales.
4. Se redactó el ADR-001 documentando el contexto, los drivers condicionales, las alternativas, la decisión propuesta y las condiciones de revisión.
5. Se verificó que la propuesta se clasifica como "PROPUESTO", no como "IMPLEMENTADO", respetando la regla de no afirmar mejoras no medidas.

**Interpretación arquitectónica:**
La decisión de no implementar paginación de inmediato se alinea con el principio de evitar soluciones prematuras ante la ausencia de drivers de negocio confirmados (volúmenes, SLO). Sin embargo, se deja la puerta abierta mediante un ADR que define exactamente qué se debe validar antes de ejecutar el cambio, equilibrando agilidad actual con gobernanza futura.

**Clasificación:** DOCUMENTADO (Decisión y trade-offs registrados formalmente).

**Riesgo, alternativa y pendiente:**
- **Riesgo:** Que el crecimiento de datos supere las expectativas antes de que se aprueben las mediciones.
- **Alternativa:** Implementar paginación desde el día uno, asumiendo el costo de complejidad sin tener la necesidad confirmada.
- **Pendiente:** Definir el conjunto representativo de datos, los consumidores afectados y los SLO de latencia para validar la alternativa B.

**Criterio de aceptación comprobado:**
- [x] E11 conecta las evidencias E01-E10 con una decisión concreta.
- [x] Se documentan explícitamente los trade-offs (simplicidad vs. escalabilidad).
- [x] El ADR-001 está creado y clasificado correctamente como PROPUESTO.
