from typing import List
from src.api_clients.rick_and_morty_client import RickMortyApiClient


def test_rickandmorty_get_characters():
    """
    Test para validar la obtención de personajes desde la API de Rick and Morty.
    """

    # 1. ARRANGE: Crea una instancia del cliente de Rick and Morty.
    rick_morty_client = RickMortyApiClient(base_url="https://rickandmortyapi.com/api/")

    # 2. ACT: Llama al método para obtener personajes.
    print("Obteniendo personajes de Rick and Morty...")
    response = rick_morty_client.get_characters(page=1)

    # 3. ASSERT: Verifica que la respuesta es correcta.
    assert response is not None
    assert hasattr(response, 'info')
    assert hasattr(response, 'results')
    assert isinstance(response.results, List)
    assert len(response.results) > 0
    print(f"-> Número de personajes obtenidos: {len(response.results)}")