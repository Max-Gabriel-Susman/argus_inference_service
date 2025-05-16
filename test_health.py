# tests/test_health.py
import pytest
from httpx import AsyncClient
from app import app          # ← your real module

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as client:
        resp = await client.get("/")
    assert resp.status_code == 200
    assert resp.json() == "Hello, Docker!"
