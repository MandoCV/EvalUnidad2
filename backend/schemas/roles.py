from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RoleBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    estatus: Optional[bool] = False

class RoleCreate(RoleBase):
    pass

class RoleUpdate(RoleBase):
    pass

class Role(RoleBase):
    id: int
    fecha_registro: Optional[datetime]
    fecha_actualizacion: Optional[datetime]

    class Config:
        orm_mode = True
