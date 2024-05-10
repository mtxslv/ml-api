import pytest
from src.service.config.logger import get_logger

from src.service.entrypoints.api import app

logger = get_logger()

@pytest.mark.asyncio
async def test_healthcheck(client):
    response = await client.get(
        f"/healthcheck"
    )
    assert response.status_code == 200
    assert response.json() == {'message': 'API is running!'}