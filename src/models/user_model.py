# src/models/user_model.py (versión actualizada)

from pydantic import BaseModel, Field
from typing import Optional

class UserCreateModel(BaseModel):
    """Modelo para crear un nuevo usuario. Debería incluir una contraseña."""
    username: str = Field(..., description="El nombre de usuario único.")
    email: str = Field(..., description="El correo electrónico del usuario.")
    full_name: str = Field(..., description="El nombre completo del usuario.")
    password: str = Field(..., description="La contraseña para el nuevo usuario.")

class UserModel(BaseModel):
    """Modelo completo de un usuario, para la respuesta de la API."""
    username: str
    email: str
    full_name: str
    disabled: Optional[bool] # 'null' se mapea a None, y por Pydantic a Optional[bool]