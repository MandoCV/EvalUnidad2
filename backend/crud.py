from sqlalchemy.orm import Session
from models import Usuario
from schemas import UsuarioCreate

def get_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def get_usuario_by_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()

def get_usuarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Usuario).offset(skip).limit(limit).all()

def create_usuario(db: Session, usuario: UsuarioCreate):
    fake_hashed_password = usuario.password + "notreallyhashed"
    db_usuario = Usuario(nombre=usuario.nombre, email=usuario.email, hashed_password=fake_hashed_password)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario
