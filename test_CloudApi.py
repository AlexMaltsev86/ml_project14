from fastapi.testclient import TestClient
from CloudApi import app

client = TestClient(app)


def test_read_CloudApi():
    response = client.get("/", params={"question": "Вопрос", "search_topic": "Контекст"})
    assert response.status_code == 200
    assert response.json() == {"answer": "Контекст"}
