import pytest
from api.client.api_client import ApiClient as APIClient
from Utils.config_reader import API_BASEURL as BASE_URL

@pytest.fixture
def api_client():
    print("BASE URL =", BASE_URL)
    return APIClient(BASE_URL)

