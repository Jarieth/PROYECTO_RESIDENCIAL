from flask import Flask
from flask_cors import CORS
from extensions import db, ma, bcrypt, jwt
from routes.auth import auth_bp
from routes.proveedor import proveedor_bp
from routes.catalogo_producto import catalogo_producto_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Configurar CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(proveedor_bp, url_prefix='/api/proveedor')
    app.register_blueprint(catalogo_producto_bp,url_prefix='/api/catalogoProducto')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)