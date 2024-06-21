from fastapi import FastAPI
from routes.persona import persona
from routes.usuario import usuario

app = FastAPI()

app.include_router(persona, prefix="/persona", tags=["persona"])
app.include_router(usuario, prefix="/usuario", tags=["usuario"])

print("Bienvenido a mi aplicación")
