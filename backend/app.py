from fastapi import FastAPI
from routes.persona import persona
from routes.usuario import usuario

app= FastAPI()
app.include_router(persona)
app.include_router(usuario)
print("Bienvenido a mi aplicación")

#Quiero su pene del diego