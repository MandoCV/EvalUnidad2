from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base, engine  # Asegúrate de importar 'engine' desde 'config.db'

class UsuariosRoles(Base):
    __tablename__ = "usuarios_roles"

    id = Column(Integer, primary_key=True, index=True)
    Usuario_ID = Column(Integer, ForeignKey("users.id"))  # Referencia a la tabla users
    Role_ID = Column(Integer, ForeignKey("roles.id"))  # Referencia a la tabla roles

    # Define las relaciones
    usuario = relationship("User", back_populates="roles")
    role = relationship("Role", back_populates="usuarios_roles")

# Asegúrate de que todas las tablas se creen al inicio de la aplicación
Base.metadata.create_all(bind=engine)
