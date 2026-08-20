from app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "running heathyly"
    assert data["version"] == "1.0"


def test_report():
    client = app.test_client()

    response = client.get("/report")

    assert response.status_code == 200

    data = response.get_json()

    assert data["service"] == "GCP Resource Reporter"
    assert data["status"] == "report generated"
