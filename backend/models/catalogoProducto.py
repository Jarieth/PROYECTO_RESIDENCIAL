from extensions import db, ma

class CatalogoProducto(db.Model):
    __tablename__ = 'CatalogoProducto'
    idProducto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255), nullable=True)
    precio = db.Column(db.Numeric(20, 2), nullable=False)
    categoria = db.Column(db.String(50), nullable=True)
    marca = db.Column(db.String(50), nullable=True)
    fecha_registro = db.Column(db.Date, nullable=True)
    costo = db.Column(db.Numeric(20, 2), nullable=False)
    idProveedor = db.Column(db.Integer, db.ForeignKey('Proveedores.idProveedor'), nullable=True)

    def __init__(self, nombre, descripcion, precio, categoria, marca, fecha_registro, costo, idProveedor):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria
        self.marca = marca
        self.fecha_registro = fecha_registro
        self.costo = costo
        self.idProveedor = idProveedor

class CatalogoProductoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CatalogoProducto
        load_instance = True
