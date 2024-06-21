from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

usuario = APIRouter()
usuarios = []

class ModelUsuarios(BaseModel):
    id: int
    usuario: str
    contrasena: str
    id_persona: str
    estatus: bool = False    
    created_at: datetime = datetime.now()

@usuario.get("/")
def bienvenida():
    return "Bienvenido al API de Usuarios"

@usuario.get("/usuarios")
def get_usuarios():
    return usuarios

@usuario.post("/usuarios")
def save_usuario(usuario_data: ModelUsuarios):
    usuarios.append(usuario_data)
    return "Usuario creado correctamente"

@usuario.get("/usuarios/{usuario_id}")
def get_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@usuario.put("/usuarios/{usuario_id}")
def update_usuario(usuario_id: int, usuario_data: ModelUsuarios):
    for index, usuario in enumerate(usuarios):
        if usuario.id == usuario_id:
            usuarios[index] = usuario_data
            return "Usuario actualizado correctamente"
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@usuario.delete("/usuarios/{usuario_id}")
def delete_usuario(usuario_id: int):
    for index, usuario in enumerate(usuarios):
        if usuario.id == usuario_id:
            usuarios.pop(index)
            return "Usuario eliminado correctamente"
    raise HTTPException(status_code=404, detail="Usuario no encontrado")