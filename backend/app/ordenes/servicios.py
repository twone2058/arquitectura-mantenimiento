from . import repositorios

def listar():
    return [orden.como_dict() for orden in repositorios.listar_todas()]

def registrar(datos):
    equipo = datos.get('equipo')
    descripcion = datos.get('descripcion')
    if not isinstance(equipo, str) or not isinstance(descripcion, str):
        raise ValueError('Equipo y descripcion deben ser textos')
    equipo = equipo.strip()
    descripcion = descripcion.strip()
    if not equipo or not descripcion:
        raise ValueError('Equipo y descripcion son obligatorios')
    if len(equipo) > 80 or len(descripcion) > 250:
        raise ValueError('Los campos exceden el limite permitido')
    return repositorios.guardar(equipo, descripcion).como_dict()
