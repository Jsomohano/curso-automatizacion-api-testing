from optparse import Option
from pydantic import AnyUrl, BaseModel, Field, HttpUrl, field_validator
from typing import List, Optional



class LocationModel(BaseModel):
    name: str
    url: Optional[AnyUrl] = None

    @field_validator("url", mode="before")
    def allow_empty_url(cls, v):
        if v == "":
            return None
        return v

# Submodelo para la paginación
class InfoModel(BaseModel):
    count: int
    pages: int
    next: Optional[HttpUrl] = None
    prev: Optional[HttpUrl] = None

# Modelo de cada personaje
class CharacterModel(BaseModel):
    id: int
    name: str
    status: str
    species: str
    type: str
    gender: str
    origin: LocationModel
    location: LocationModel
    image: HttpUrl
    episode: List[HttpUrl]
    url: HttpUrl
    created: str  # puedes usar datetime si quieres validación de fecha

# Modelo raíz para la respuesta completa
class CharacterResponseModel(BaseModel):
    info: InfoModel
    results: List[CharacterModel]
