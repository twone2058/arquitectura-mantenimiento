from app.extensiones import db

class Orden(db.Model):
    __tablename__ = 'ordenes'
    id = db.Column(db.Integer, primary_key=True)
    equipo = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.String(250), nullable=False)
    estado = db.Column(db.String(20), nullable=False, default='abierta')

    def como_dict(self):
        return {'id': self.id, 'equipo': self.equipo,
                'descripcion': self.descripcion, 'estado': self.estado}
