# src/api_clients/task_api_client.py

import requests
from src.api_clients.base_api_client import BaseApiClient
# La siguiente línea estaba causando el error y debe eliminarse.
# from src.api_clients.task_api_client import TaskApiClient
from src.models.task_model import TaskCreateModel, TaskModel, TaskStatus, TaskResponseModel
from typing import List, Optional

class TaskApiClient(BaseApiClient):
    """
    Cliente de API para el recurso de tareas (tasks).
    """
    def __init__(self, base_url: str, token: Optional[str] = None):
        super().__init__(base_url, token)
        self.endpoint = "tasks"

    def create_task(self, task_data: TaskCreateModel) -> TaskModel:
        """
        Realiza una petición POST para crear una nueva tarea.
        Retorna la tarea creada como un objeto TaskModel.
        """
        payload = task_data.model_dump(exclude_none=True)
        response = self._send_request("POST", "tasks", json=payload)
        return TaskModel(**response.json())
        
    def get_all_tasks(self) -> List[TaskModel]:
        """
        Obtiene la lista completa de tareas y la deserializa a List[TaskModel].
        """
        response = self._send_request("GET", "tasks")
        return [TaskModel(**task) for task in response.json()]

    def get_task_by_id(self, task_id: int) -> TaskResponseModel:
        """
        Obtiene una tarea por su ID y la deserializa a un objeto TaskResponseModel.
        """
        response = self._send_request("GET", f"{self.endpoint}/{task_id}")
        return TaskResponseModel(**response.json())

    def update_task(self, task_id: int, task_data: TaskModel) -> TaskResponseModel:
        """
        Actualiza una tarea por su ID. La API requiere el objeto completo (TaskModel) para el PUT.
        Retorna la respuesta parcial del PUT usando TaskResponseModel.
        """
        payload = task_data.model_dump(exclude_none=True)
        response = self._send_request("PUT", f"tasks/{task_id}", json=payload)
        return TaskResponseModel(**response.json())

    def delete_task(self, task_id: int) -> requests.Response:
        """
        Elimina una tarea por su ID.
        """
        return self._send_request("DELETE", f"{self.endpoint}/{task_id}")