import pytest
from typing import List

# Importamos solo los modelos consolidados
from src.api_clients.task_api_client import TaskApiClient
from src.models.task_model import TaskCreateModel, TaskModel, TaskResponseModel, TaskStatus

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
        description="Aprender Pytest",
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
    created_task.status = TaskStatus.COMPLETE

    # 5. ACT (Acción): Actualiza la tarea con el objeto completo modificado.
    print(f"Actualizando la tarea con ID {created_task.id} a estado 'Complete'...")
    updated_task = task_api_client.update_task(created_task.id, created_task)

    # 6. ASSERT (Validación): Verifica que la actualización fue exitosa.
    assert isinstance(updated_task, TaskResponseModel)
    assert updated_task.status == TaskStatus.COMPLETE
    
    print(f"-> Tarea con ID {created_task.id} actualizada con éxito.")

    # --- Verificación de la Tarea Actualizada ---
    # 7. ACT (Acción): Obtén la tarea para verificar el cambio.
    print(f"Obteniendo la tarea con ID {created_task.id} para verificar...")
    retrieved_task = task_api_client.get_task_by_id(created_task.id)

    # 8. ASSERT (Validación): Confirma que el estado se actualizó correctamente.
    assert isinstance(retrieved_task, TaskResponseModel)
    assert retrieved_task.status == TaskStatus.COMPLETE
    
    print("-> Verificación de la actualización exitosa.")

    # --- Limpieza (Eliminación) ---
    # 9. ACT (Acción): Elimina la tarea creada para no dejar datos residuales.
    print(f"Eliminando la tarea con ID {created_task.id}...")
    response_delete = task_api_client.delete_task(created_task.id)

    # 10. ASSERT (Validación): Verifica que la eliminación fue exitosa.
    assert response_delete.status_code == 204
    
    print("-> Tarea eliminada correctamente.")
    print("--- Test Finalizado con Éxito ---")