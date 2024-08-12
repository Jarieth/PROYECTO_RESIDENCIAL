from flask import Blueprint, request, jsonify
from extensions import db
from models import Proveedor, ProveedorSchema

proveedor_bp = Blueprint('proveedor', __name__)

proveedor_schema = ProveedorSchema()
proveedores_schema = ProveedorSchema(many=True)

# Crear un nuevo proveedor
@proveedor_bp.route('/proveedores', methods=['POST'])
def create_proveedor():
    data = request.get_json()
    errors = proveedor_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    new_proveedor = Proveedor(
        nombre=data['nombre'],
        direccion=data.get('direccion'),
        telefono=data.get('telefono'),
        email=data.get('email'),
        periodo_llegada=data.get('periodo_llegada'),
        fecha_llegada=data.get('fecha_llegada')
    )
    db.session.add(new_proveedor)
    db.session.commit()
    return proveedor_schema.jsonify(new_proveedor), 201

# Obtener todos los proveedores
@proveedor_bp.route('/proveedores', methods=['GET'])
def get_proveedores():
    proveedores = Proveedor.query.all()
    return proveedores_schema.jsonify(proveedores), 200

# Obtener un proveedor por ID
@proveedor_bp.route('/proveedores/<int:id>', methods=['GET'])
def get_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    return proveedor_schema.jsonify(proveedor), 200

# Actualizar un proveedor
@proveedor_bp.route('/proveedores/<int:id>', methods=['PUT'])
def update_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    data = request.get_json()
    errors = proveedor_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    proveedor.nombre = data['nombre']
    proveedor.direccion = data.get('direccion', proveedor.direccion)
    proveedor.telefono = data.get('telefono', proveedor.telefono)
    proveedor.email = data.get('email', proveedor.email)
    proveedor.periodo_llegada = data.get('periodo_llegada', proveedor.periodo_llegada)
    proveedor.fecha_llegada = data.get('fecha_llegada', proveedor.fecha_llegada)
    db.session.commit()
    return proveedor_schema.jsonify(proveedor), 200

# Borrar un proveedor
@proveedor_bp.route('/proveedores/<int:id>', methods=['DELETE'])
def delete_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    db.session.delete(proveedor)
    db.session.commit()
    return '', 204
