# tests/test_health.py
from httpx import AsyncClient
from fastapi_project.main import create_app   # adjust import to your actual factory

async def test_healthcheck():
    app = create_app()
    async with AsyncClient(app=app, base_url="http://test") as client:
        resp = await client.get("/health")
    assert resp.status_code == 200
