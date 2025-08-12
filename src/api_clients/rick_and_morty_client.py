from src.api_clients.base_api_client import BaseApiClient
from src.models.character_model import CharacterResponseModel


class RickMortyApiClient(BaseApiClient):
    def get_characters(self, page: int = 1) -> CharacterResponseModel:
        response = self._send_request("GET", f"character")
        return CharacterResponseModel(**response.json())
