from flask import Blueprint, jsonify, request
from . import servicios

bp = Blueprint('ordenes', __name__, url_prefix='/api/ordenes')

@bp.get('')
def consultar():
    return jsonify({'success': True, 'data': servicios.listar()}), 200

@bp.post('')
def crear():
    datos = request.get_json(silent=True)
    if not isinstance(datos, dict):
        return jsonify({'success': False, 'error': 'Se requiere un objeto JSON'}), 400
    try:
        orden = servicios.registrar(datos)
    except ValueError as error:
        return jsonify({'success': False, 'error': str(error)}), 400
    return jsonify({'success': True, 'data': orden}), 201
