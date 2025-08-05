# src/api_clients/user_api_client.py (versión ajustada)

import requests
from src.api_clients.base_api_client import BaseApiClient
from src.models.user_model import UserCreateModel, UserModel
from typing import Optional, List

class UserApiClient(BaseApiClient):
    """Cliente para la gestión de usuarios."""
    
    def __init__(self, base_url: str, token: Optional[str] = None):
        super().__init__(base_url, token=token)
        self.endpoint = "user"
        
    def get_all_users(self) -> List[UserModel]:
        """Obtiene una lista de todos los usuarios."""
        response = self._send_request("GET", self.endpoint)
        
        # Deserializa la respuesta como una lista de objetos UserModel
        return [UserModel(**user) for user in response.json()]
    
        
    def get_user_by_username(self, username: str) -> UserModel:
        """Obtiene un usuario por su nombre de usuario."""
        response = self._send_request("GET", f"{self.endpoint}/{username}")
        return UserModel(**response.json())
        
    def get_current_user(self) -> UserModel:
        """Obtiene los datos del usuario logueado."""
        response = self._send_request("GET", f"{self.endpoint}/me")
        return UserModel(**response.json())
        
    def update_user(self, username: str, user_data: UserModel) -> UserModel:
        """Actualiza un usuario por su nombre de usuario."""
        response = self._send_request("PUT", f"{self.endpoint}/{username}", json=user_data.model_dump(exclude_none=True))
        return UserModel(**response.json())
        
    def delete_user(self, user_id: int) -> requests.Response:
        """Elimina un usuario por su ID."""
        return self._send_request("DELETE", f"{self.endpoint}/{user_id}")