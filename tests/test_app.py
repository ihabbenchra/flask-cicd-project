from app import app

client = app.test_client()

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_sante():
    response = client.get("/sante")
    assert response.status_code == 200

def test_connexion_success():
    response = client.post(
        "/connexion",
        json={"key": "admin123"}
    )

    assert response.status_code == 200

def test_connexion_fail():
    response = client.post(
        "/connexion",
        json={"key": "wrong"}
    )

    assert response.status_code == 401
    