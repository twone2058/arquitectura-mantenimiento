# Arquitectura de Software - Sistema de Gestion de Mantenimiento

**Diagnostico arquitectonico completo** segun el Manual de Fundamentos y Manual Paso a Paso (octubre 2026).

## Autores
- **Angel Reina**
- **Juan Jose Pineda**

---

## Descripcion del Proyecto

Caso empresarial: Una empresa de distribucion administra equipos de bodega (montacargas, bandas y otros activos). El area de Operaciones necesita registrar ordenes de mantenimiento y consultarlas posteriormente.

## Requisitos Funcionales

- **RF-01**: Registrar ordenes con equipo y descripcion no vacios
- **RF-02**: Consultar ordenes y su estado desde la aplicacion web
- **RN-01**: Conservar ordenes tras reiniciar el backend

## Arquitectura

- **Backend**: Python 3.11 + Flask 3.x (monolito modular)
- **Frontend**: HTML5 + JavaScript vanilla (SPA ligera)
- **Persistencia**: SQLite + SQLAlchemy ORM

## Estructura del Expediente

El directorio expediente/ contiene 11 evidencias (E01 a E11) que documentan el diagnostico arquitectonico completo.

## Instalacion y Ejecucion

git clone https://github.com/twone2058/arquitectura-mantenimiento.git
cd arquitectura-mantenimiento/backend
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
py init_db.py
py app.py

Acceder a: http://127.0.0.1:5000

## Decision Arquitectonica (ADR-001)

**Estado**: PROPUESTO
**Decision**: Disenar variante paginada del endpoint GET /api/ordenes, pero NO implementarla inmediatamente.

## Estado del Proyecto

- Completado: Expediente de ingenieria ARQ-01 a ARQ-11
- Completado: Diagramas C4 Context y Container
- Completado: ADR-001 documentado

---

*Proyecto academico - Octubre 2026*
