import pytest
from typing import List

# Importamos solo los modelos consolidados
from src.api_clients.task_api_client import TaskApiClient
from src.models.task_model import TaskCreateModel, TaskModel, TaskResponseModel, TaskStatus
from src.api_clients.rick_and_morty_client import RickMortyApiClient


# Asumimos que los fixtures están en conftest.py o los defines aquí
from .conftest import auth_api_client, task_api_client, valid_user_token, base_api_url

def test_task_complete_lifecycle(task_api_client: TaskApiClient):
    """
    Test que valida el ciclo de vida de una tarea:
    Creación -> Actualización -> Verificación -> Eliminación.
    """
    print("\n--- Test de Ciclo de Vida de Tarea ---")

    # 1. ARRANGE (Preparación): Define los datos iniciales de la tarea.
    initial_task_data = TaskCreateModel(
        description="Hola mundo3",
        status=TaskStatus.DRAFT,
        created_by="tester"
    )
    
    # 2. ACT (Acción): Crea la tarea.
    print("Creando una nueva tarea...")
    created_task = task_api_client.create_task(initial_task_data)

    # 3. ASSERT (Validación): Verifica el objeto creado.
    assert isinstance(created_task, TaskModel)
    assert created_task.description == initial_task_data.description
    assert created_task.status == initial_task_data.status
    assert created_task.id is not None
    
    print(f"-> Tarea creada con ID: {created_task.id} y estado: {created_task.status}")

    # --- Actualización de la Tarea ---
    # 4. ARRANGE (Preparación): Modificamos el objeto de la tarea creada.
    created_task.status = TaskStatus.IN_PROGRESS

    # 5. ACT (Acción): Actualiza la tarea con el objeto completo modificado.
    print(f"Actualizando la tarea con ID {created_task.id} a estado 'Complete'...")
    updated_task = task_api_client.update_task(created_task.id, created_task)

    # 6. ASSERT (Validación): Verifica que la actualización fue exitosa.
    assert isinstance(updated_task, TaskResponseModel)
    assert updated_task.status == TaskStatus.IN_PROGRESS
    
    print(f"-> Tarea con ID {created_task.id} actualizada con éxito.")

def test_create_task_success(task_api_client: TaskApiClient):
    """
    Escenario positivo: creación exitosa de una tarea.
    """
    # 1. ARRANGE: Prepara los datos de la tarea.
    initial_task_data = TaskCreateModel(
        description="Tarea positiva",
        status=TaskStatus.DRAFT,
        created_by="tester"
    )

    # 2. ACT: Crea la tarea.
    created_task = task_api_client.create_task(initial_task_data)

    # 3. ASSERT: Verifica que la tarea fue creada correctamente.
    assert isinstance(created_task, TaskModel)
    assert created_task.description == initial_task_data.description
    assert created_task.status == initial_task_data.status
    assert created_task.id is not None
    print(f"-> Tarea creada con ID: {created_task.id}")

