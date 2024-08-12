from flask import Blueprint, request, jsonify
from models import Usuario, UsuarioSchema
from extensions import db, bcrypt, jwt
from flask_jwt_extended import create_access_token
from datetime import datetime  # Importar el módulo datetime


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    idRol = data.get('idRol')

    # Validación simple
    if not username or not email or not password or not nombre or not apellido or not idRol:
        return jsonify({"msg": "Missing required fields"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    fecha_registro = datetime.now().date()

    new_user = Usuario(
        username=username,
        email=email,
        password=hashed_password,
        nombre=nombre,
        apellido=apellido,
        idRol=idRol,
        fecha_registro=fecha_registro
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = Usuario.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.idUsuario)  # Cambia a 'user.idUsuario'
        return jsonify({"token": access_token}), 200

    return jsonify({"msg": "Bad username or password"}), 401