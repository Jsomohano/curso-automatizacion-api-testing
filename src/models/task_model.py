from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

# Modelo de enumeración para los estados de la tarea.
class TaskStatus(str, Enum):
    DRAFT = "Draft"
    IN_PROGRESS = "In Progress"
    COMPLETE = "Complete"

# Modelo de creación (para POST)
class TaskCreateModel(BaseModel):
    description: str = Field(..., description="La descripción de la tarea, obligatoria.")
    status: Optional[TaskStatus] = Field(TaskStatus.DRAFT, description="El estado de la tarea.")
    created_by: Optional[str] = Field("anonymous", description="El usuario que crea la tarea.")

# Modelo para respuestas completas (del POST y GET de lista)
class TaskModel(BaseModel):
    id: int
    description: str
    status: TaskStatus
    created_by: str

# Modelo para la respuesta del PUT y GET por ID (respuestas parciales)
class TaskResponseModel(BaseModel):
    id: int
    description: str
    status: TaskStatus