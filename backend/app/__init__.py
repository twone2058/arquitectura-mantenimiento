import os
from pathlib import Path
from flask import Flask
from dotenv import load_dotenv
from .extensiones import db

def create_app():
    root = Path(__file__).resolve().parents[2]
    load_dotenv(root / 'backend' / '.env')
    app = Flask(__name__, static_folder=str(root / 'frontend'), static_url_path='')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///mantenimiento.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    from .ordenes.controladores import bp
    app.register_blueprint(bp)

    @app.get('/')
    def inicio():
        return app.send_static_file('index.html')

    @app.get('/health')
    def salud():
        return {'status': 'ok'}, 200

    return app
