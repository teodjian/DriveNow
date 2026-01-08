from uuid import uuid4

from fastapi.testclient import TestClient

from car_inventory_service.src.initialize import create_app

# Arrange
app = create_app()
client = TestClient(app)

def test_create_car_api():
    # Act
    response = client.post("/car_inventory/car", json={
        "id": str(uuid4()),
        "model": "Toyota Camry",
        "year": 2022,
        "status": "available"
    })
    assert response.status_code == 200 # or 201

def test_get_car_not_found():
    # Act
    response = client.get("car_inventory/car_by_id/9c3c0e1b-6c4d-4baf-9f8a-1f1c1c8b2e7d")
    assert response.status_code == 404


def test_create_car_validation_error():
    # 1. ACT: Send incomplete data (Missing 'model')
    response = client.post("/car_inventory/car", json={
        "car_id": str(uuid4()),
        # "model": "Tesla, <--- MISSING
        "year": 2022
    })

    # 2. ASSERT
    assert response.status_code == 422  # Unprocessable Entity

    # Check that the error message mentions the missing field
    errors = response.json()["detail"]
    # assert errors[0]["loc"] == ["body", "model"]
    assert errors[0]["msg"] == "Field required"