from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.usuarios_roles as crud
import schemas.usuarios_roles as schemas  # Asegúrate de que esto esté correcto
from config.db import SessionLocal, engine
from models.usuarios_roles import UsuariosRoles
from models.roles import Role
from typing import List

usuarios_roles = APIRouter()

UsuariosRoles.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@usuarios_roles.get("/usuarios_roles/", response_model=List[schemas.UsuariosRoles], tags=["UsuariosRoles"])
def read_usuarios_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    usuarios_roles = crud.get_usuarios_roles(db=db, skip=skip, limit=limit)
    return usuarios_roles

@usuarios_roles.post("/usuarios_roles/", response_model=schemas.UsuariosRoles, tags=["UsuariosRoles"])
def create_usuarios_roles(usuarios_roles: schemas.UsuariosRoles, db: Session = Depends(get_db)):
    return crud.create_usuarios_roles(db=db, usuarios_roles=usuarios_roles)

@usuarios_roles.put("/usuarios_roles/{id}", response_model=schemas.UsuariosRoles, tags=["UsuariosRoles"])
def update_usuarios_roles(id: int, usuarios_roles: schemas.UsuariosRoles, db: Session = Depends(get_db)):
    return crud.update_usuarios_roles(db=db, id=id, usuarios_roles=usuarios_roles)

@usuarios_roles.delete("/usuarios_roles/{id}", response_model=schemas.UsuariosRoles, tags=["UsuariosRoles"])
def delete_usuarios_roles(id: int, db: Session = Depends(get_db)):
    return crud.delete_usuarios_roles(db=db, id=id)
