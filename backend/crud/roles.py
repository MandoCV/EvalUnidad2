from sqlalchemy.orm import Session
import models.roles
import schemas.roles
from datetime import datetime

def get_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.roles.Role).offset(skip).limit(limit).all()

def create_role(db: Session, role: schemas.roles.RoleCreate):
    db_role = models.roles.Role(**role.dict(), fecha_registro=datetime.utcnow())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def update_role(db: Session, id: int, role: schemas.roles.RoleUpdate):
    db_role = db.query(models.roles.Role).filter(models.roles.Role.id == id).first()
    if db_role:
        update_data = role.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_role, key, value)
        db_role.fecha_actualizacion = datetime.utcnow()
        db.commit()
        db.refresh(db_role)
    return db_role

def delete_role(db: Session, id: int):
    db_role = db.query(models.roles.Role).filter(models.roles.Role.id == id).first()
    if db_role:
        db.delete(db_role)
        db.commit()
    return db_role
