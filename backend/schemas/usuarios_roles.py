from pydantic import BaseModel
from typing import Optional

class UsuariosRolesBase(BaseModel):
    Usuario_ID: int
    Role_ID: int

    class Config:
        orm_mode = True

class UsuariosRolesCreate(UsuariosRolesBase):
    pass

class UsuariosRolesUpdate(UsuariosRolesBase):
    id: Optional[int]

class UsuariosRolesInDB(UsuariosRolesBase):
    id: int

class UsuariosRoles(UsuariosRolesBase):
    pass
