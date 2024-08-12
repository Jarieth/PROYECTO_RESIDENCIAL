from functools import wraps
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import request, jsonify
from models import Usuario

def role_required(roles):
    def wrapper(fn):
        @wraps(fn)
        @jwt_required()
        def decorator(*args, **kwargs):
            user_id = get_jwt_identity()
            usuario = Usuario.query.get(user_id)
            if usuario.role.nombre not in roles:
                return jsonify({"msg": "Access denied"}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper
