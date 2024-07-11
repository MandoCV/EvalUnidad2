from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.roles
import schemas.roles
from config.db import SessionLocal, engine
from typing import List
from datetime import datetime
import models.roles  # Agrega la importación del módulo models.roles

role = APIRouter()

# Crea las tablas en la base de datos si no existen
models.roles.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@role.get("/roles/", response_model=List[schemas.roles.Role], tags=["Roles"])
def read_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    roles = crud.roles.get_roles(db=db, skip=skip, limit=limit)
    return roles

@role.post("/roles/", response_model=schemas.roles.Role, tags=["Roles"])
def create_role(role: schemas.roles.RoleCreate, db: Session = Depends(get_db)):
    return crud.roles.create_role(db=db, role=role)

@role.put("/role/{id}", response_model=schemas.roles.Role, tags=["Roles"])
def update_role(id: int, role: schemas.roles.RoleUpdate, db: Session = Depends(get_db)):
    return crud.roles.update_role(db=db, id=id, role=role)

@role.delete("/role/{id}", response_model=schemas.roles.Role, tags=["Roles"])
def delete_role(id: int, db: Session = Depends(get_db)):
    return crud.roles.delete_role(db=db, id=id)
