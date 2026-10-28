
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["model_loaded"] is True


def test_predict():
    payload = {
        "Brand": "Asus",
        "Processor_Speed": 3.8,
        "RAM_Size": 16,
        "Storage_Capacity": 512,
        "Screen_Size": 15.6,
        "Weight": 2.5,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert "predicted_price" in response.json()
    assert isinstance(response.json()["predicted_price"], (int, float))
