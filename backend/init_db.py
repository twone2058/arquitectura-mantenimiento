from app import create_app
from app.extensiones import db
from app.ordenes.modelos import Orden

app = create_app()
with app.app_context():
    db.create_all()
    if db.session.query(Orden).count() == 0:
        db.session.add_all([
            Orden(equipo='Montacargas M-01', descripcion='Inspeccion del sistema hidraulico'),
            Orden(equipo='Banda B-02', descripcion='Revision preventiva de rodillos')
        ])
        db.session.commit()
        print('Ordenes disponibles:', db.session.query(Orden).count())
