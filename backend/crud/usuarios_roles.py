from sqlalchemy.orm import Session
import models.usuarios_roles
import schemas.usuarios_roles

def get_usuarios_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.usuarios_roles.UsuariosRoles).offset(skip).limit(limit).all()

def create_usuarios_roles(db: Session, usuarios_roles: schemas.usuarios_roles.UsuariosRolesCreate):
    db_usuarios_roles = models.usuarios_roles.UsuariosRoles(**usuarios_roles.dict())
    db.add(db_usuarios_roles)
    db.commit()
    db.refresh(db_usuarios_roles)
    return db_usuarios_roles

def update_usuarios_roles(db: Session, id: int, usuarios_roles: schemas.usuarios_roles.UsuariosRolesUpdate):
    db_usuarios_roles = db.query(models.usuarios_roles.UsuariosRoles).filter(models.usuarios_roles.UsuariosRoles.id == id).first()
    if db_usuarios_roles:
        for key, value in usuarios_roles.dict().items():
            setattr(db_usuarios_roles, key, value)
        db.commit()
        db.refresh(db_usuarios_roles)
    return db_usuarios_roles

def delete_usuarios_roles(db: Session, id: int):
    db_usuarios_roles = db.query(models.usuarios_roles.UsuariosRoles).filter(models.usuarios_roles.UsuariosRoles.id == id).first()
    if db_usuarios_roles:
        db.delete(db_usuarios_roles)
        db.commit()
    return db_usuarios_roles
