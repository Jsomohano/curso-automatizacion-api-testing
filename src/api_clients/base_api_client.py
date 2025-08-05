# src/api_clients/base_api_client.py

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from typing import Optional, Any

class BaseApiClient:
    """Clase base que centraliza la configuración de la sesión HTTP."""
    
    def __init__(self, base_url: str, token: Optional[str] = None):
        if not base_url:
            raise ValueError("La URL base no puede ser nula.")
        
        self.base_url = base_url
        self.session = requests.Session()
        
        self.session.headers.update({"Content-Type": "application/json", "Accept": "application/json"})
        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})
            
        retry_strategy = Retry(
            total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "PUT", "DELETE", "OPTIONS", "TRACE"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        
    def _get_url(self, endpoint: str) -> str:
        return f"{self.base_url}/{endpoint.lstrip('/')}"
        
    def _send_request(self, method: str, endpoint: str, **kwargs: Any) -> requests.Response:
        url = self._get_url(endpoint)
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response