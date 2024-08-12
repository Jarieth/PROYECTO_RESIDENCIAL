from extensions import db, bcrypt
from models import Usuario, Rol
from app import create_app
from datetime import datetime

app = create_app()
app.app_context().push()

# Crear roles
rol_admin = Rol(nombre="Admin", descripcion="Administrator role")
rol_user = Rol(nombre="User", descripcion="Regular user role")
db.session.add(rol_admin)
db.session.add(rol_user)
db.session.commit()

# Crear usuarios
admin_username = "admin"
admin_password = "adminpassword"
hashed_password = bcrypt.generate_password_hash(admin_password).decode('utf-8')

nuevo_admin = Usuario(
    nombre="Admin",
    apellido="User",
    username=admin_username,
    password=hashed_password,
    email="admin@example.com",
    rolId=rol_admin.idRol,
    fecha_registro=datetime.utcnow()
)

db.session.add(nuevo_admin)
db.session.commit()

print("Usuarios y roles creados con éxito")
