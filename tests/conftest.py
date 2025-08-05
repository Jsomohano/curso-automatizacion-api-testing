import pytest
from typing import List

# Importamos todos los clientes y modelos que hemos creado
from src.api_clients.token_api_client import AuthApiClient
from src.api_clients.task_api_client import TaskApiClient
from src.api_clients.user_api_client import UserApiClient
from src.models.token_model import LoginModel, TokenModel

# --- 🛠 Configuración del Test (Fixtures) ---

# URL de la API de prueba (idealmente, esto vendría de un archivo .env o settings)
API_BASE_URL = "https://8000-djwester-todolisttestin-scho82zu6a3.ws-us120.gitpod.io/"

@pytest.fixture(scope="session")
def base_api_url():
    """Fixture que retorna la URL base de la API para toda la sesión de pruebas."""
    return API_BASE_URL

@pytest.fixture(scope="session")
def auth_api_client(base_api_url):
    """Fixture que retorna una instancia del cliente de autenticación."""
    return AuthApiClient(base_api_url)

@pytest.fixture(scope="session")
def valid_user_token(auth_api_client) -> str:
    """
    Fixture que se encarga del login para obtener un token de autenticación.
    Este token se usa una sola vez por toda la sesión de pruebas.
    """
    # En un test real, podrías crear el usuario de prueba aquí,
    # pero para este ejemplo, asumimos que "testuser" ya existe.
    login_data = LoginModel(username="user1", password="12345")
    response = auth_api_client.login(login_data)
    
    # Validamos que el login fue exitoso. Si falla, el test no continuará.
    assert response.status_code == 200
    token_response = TokenModel(**response.json())
    
    return token_response.access_token

@pytest.fixture(scope="session")
def task_api_client(base_api_url, valid_user_token) -> TaskApiClient:
    """
    Fixture que retorna una instancia del cliente de tareas.
    Depende de otros fixtures para obtener la URL y el token.
    """
    return TaskApiClient(base_api_url, token=valid_user_token)

@pytest.fixture(scope="session")
def user_api_client(base_api_url, valid_user_token) -> UserApiClient:
    """
    Fixture que retorna una instancia del cliente de usuarios.
    Depende de otros fixtures para obtener la URL y el token.
    """
    return UserApiClient(base_api_url, token=valid_user_token)