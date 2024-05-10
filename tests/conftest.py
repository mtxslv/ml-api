import pytest_asyncio
from httpx import AsyncClient

from src.service.entrypoints.api import app


@pytest_asyncio.fixture()
async def client():
    async with AsyncClient(app=app, base_url=f"http://localhost:8080") as client:
        yield client