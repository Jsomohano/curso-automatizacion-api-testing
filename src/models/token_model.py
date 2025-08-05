# src/models/token_model.py

from pydantic import BaseModel, Field
from typing import Optional

class LoginModel(BaseModel):
    """
    Modelo de datos para el payload de la petición POST del endpoint /token.
    Define los campos 'username' y 'password'.
    """
    username: str = Field(..., description="El nombre de usuario para el login.")
    password: str = Field(..., description="La contraseña del usuario.")

class TokenModel(BaseModel):
    """
    Modelo de datos para la respuesta exitosa del endpoint /token.
    Define los campos 'access_token' y 'token_type'.
    """
    access_token: str = Field(..., description="El token de acceso JWT proporcionado por la API.")
    token_type: str = "bearer"