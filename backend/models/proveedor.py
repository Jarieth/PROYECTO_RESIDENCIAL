from extensions import db, ma

class Proveedor(db.Model):
    __tablename__ = 'Proveedores'
    idProveedor = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(255), nullable=True)
    telefono = db.Column(db.String(15), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    periodo_llegada = db.Column(db.String(100), nullable=True)
    fecha_llegada = db.Column(db.String(100), nullable=True)

    def __init__(self, nombre, direccion, telefono, email, periodo_llegada, fecha_llegada):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.periodo_llegada = periodo_llegada
        self.fecha_llegada = fecha_llegada

class ProveedorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Proveedor
        load_instance = True
