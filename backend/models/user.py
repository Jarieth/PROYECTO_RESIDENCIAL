from extensions import db, ma

class Usuario(db.Model):
    __tablename__ = 'Usuarios'  # Asegúrate de que este es el nombre correcto de la tabla en tu base de datos

    idUsuario = db.Column(db.Integer, primary_key=True)  # Define la columna 'idUsuario' como la clave primaria
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    idRol = db.Column(db.Integer, db.ForeignKey('Roles.idRol'), nullable=False) # Esta es la llave foranea de la tabla Roles
    fecha_registro = db.Column(db.Date, nullable=False)

    def __init__(self, nombre, apellido, username, password, email, idRol, fecha_registro):
        self.nombre = nombre
        self.apellido = apellido
        self.username = username
        self.password = password
        self.email = email
        self.idRol = idRol
        self.fecha_registro = fecha_registro

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        load_instance = True
