from flask import Blueprint, request, jsonify
from models import CatalogoProducto, CatalogoProductoSchema
from extensions import db

catalogo_producto_bp = Blueprint('catalogoProducto', __name__)

# Esquema
catalogo_producto_schema = CatalogoProductoSchema()
catalogo_productos_schema = CatalogoProductoSchema(many=True)

# Crear un nuevo producto
@catalogo_producto_bp.route('/catalogo_producto', methods=['POST'])
def add_producto():
    data = request.get_json()
    nombre = data.get('nombre')
    descripcion = data.get('descripcion')
    precio = data.get('precio')
    categoria = data.get('categoria')
    marca = data.get('marca')
    fecha_registro = data.get('fecha_registro')
    costo = data.get('costo')
    idProveedor = data.get('idProveedor')

    nuevo_producto = CatalogoProducto(
        nombre=nombre, descripcion=descripcion, precio=precio, categoria=categoria,
        marca=marca, fecha_registro=fecha_registro, costo=costo, idProveedor=idProveedor
    )

    db.session.add(nuevo_producto)
    db.session.commit()

    return catalogo_producto_schema.jsonify(nuevo_producto), 201

# Obtener todos los productos
@catalogo_producto_bp.route('/catalogo_producto', methods=['GET'])
def get_productos():
    productos = CatalogoProducto.query.all()
    return catalogo_productos_schema.jsonify(productos), 200

# Obtener un producto por ID
@catalogo_producto_bp.route('/catalogo_producto/<int:id>', methods=['GET'])
def get_producto(id):
    producto = CatalogoProducto.query.get_or_404(id)
    return catalogo_producto_schema.jsonify(producto), 200

# Actualizar un producto por ID
@catalogo_producto_bp.route('/catalogo_producto/<int:id>', methods=['PUT'])
def update_producto(id):
    producto = CatalogoProducto.query.get_or_404(id)
    data = request.get_json()
    producto.nombre = data.get('nombre', producto.nombre)
    producto.descripcion = data.get('descripcion', producto.descripcion)
    producto.precio = data.get('precio', producto.precio)
    producto.categoria = data.get('categoria', producto.categoria)
    producto.marca = data.get('marca', producto.marca)
    producto.fecha_registro = data.get('fecha_registro', producto.fecha_registro)
    producto.costo = data.get('costo', producto.costo)
    producto.idProveedor = data.get('idProveedor', producto.idProveedor)

    db.session.commit()
    return catalogo_producto_schema.jsonify(producto), 200

# Eliminar un producto por ID
@catalogo_producto_bp.route('/catalogo_producto/<int:id>', methods=['DELETE'])
def delete_producto(id):
    producto = CatalogoProducto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return '', 204
