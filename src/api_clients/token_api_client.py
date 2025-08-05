# src/api_clients/auth_api_client.py (versión corregida)

import requests
from src.api_clients.base_api_client import BaseApiClient
from src.models.token_model import LoginModel

class AuthApiClient(BaseApiClient):
    """Cliente para el endpoint de autenticación."""
    def __init__(self, base_url: str):
        # La clase base ya configura la sesión, pero el token se obtendrá después del login
        super().__init__(base_url)
        self.endpoint = "token"

    def login(self, login_data: LoginModel) -> requests.Response:
        """
        Realiza una petición POST para obtener un token de acceso.
        Se usa el parámetro 'data' para enviar en formato x-www-form-urlencoded.
        """
        # La clase base ya tiene el Content-Type como 'application/json',
        # por lo que debemos sobrescribirlo para esta petición.
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        
        # El payload se serializa como un diccionario y se envía con 'data='
        payload = login_data.model_dump(exclude_none=True)
        
        return self._send_request("POST", self.endpoint, data=payload, headers=headers)