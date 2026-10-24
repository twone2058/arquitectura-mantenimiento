from app.extensiones import db
from .modelos import Orden

def listar_todas():
    consulta = db.select(Orden).order_by(Orden.id)
    return db.session.scalars(consulta).all()

def guardar(equipo, descripcion):
    orden = Orden(equipo=equipo, descripcion=descripcion)
    db.session.add(orden)
    db.session.commit()
    return orden
