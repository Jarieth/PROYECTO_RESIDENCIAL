from extensions import db, ma

class Rol(db.Model):
    __tablename__ = 'Roles'
    idRol = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))

class RolSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Rol
        load_instance = True
