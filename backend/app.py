from fastapi import FastAPI
from config.db import engine, Base
from routes.user import user
from routes.person import person
from routes.role import role
from routes.usuarios_roles import usuarios_roles

app = FastAPI(
    title="PRIVILEGE CARE",
)

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir las rutas y dependencias
app.include_router(user)
app.include_router(person)
app.include_router(role)
app.include_router(usuarios_roles)

print("Hola, bienvenido a mi backend")
